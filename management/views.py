from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewFinanceForm
from .models import Finance
from .models import Person
from .models import Resources, Stock
from .models import Projects, Comptes
from django.db.models import Sum
from django.db.models import Q


def welcome(request):
    return render(request, 'management/welcome.html')

def synthetic_report(request):
    resources = Resources.objects.all()
    projects = Projects.objects.all()
    output = Finance.objects.filter(type_transaction='OP')
    input = Finance.objects.filter(type_transaction='IP')
    ouvriers = Person.objects.filter(position='B')
    personel_bureau = Person.objects.filter(position='A')
    locataire_nziapanda = Person.objects.filter(position='E')
    compte_kavatsi_input = Finance.objects.filter(account='Kasereka_Kavatsi', type_transaction='IP')
    compte_kavatsi_output = Finance.objects.filter(account='Kasereka_Kavatsi', type_transaction='OP')
    compte_bureau_input= Finance.objects.filter(account='Bureau_Central', type_transaction='IP')
    compte_bureau_output= Finance.objects.filter(account='Bureau_Central', type_transaction='OP')
    compte_autre = Finance.objects.exclude(account='Kasereka_Kavatsi')
    compte_autre = compte_autre.exclude(account='Bureau_Central')
    compte_autre_output = compte_autre.filter(type_transaction='OP')
    compte_autre_input = compte_autre.filter(type_transaction='IP')

    ##########  KILI ############
    kili_input = input.filter(origin_location='KL')
    kili_output = output.filter(destination_location='KL')
    kili_resources = resources.filter(location='KI')
    total_kili_input = kili_input.aggregate(total_kili_input=Sum('amount_in_usd'))['total_kili_input']
    total_kili_output = kili_output.aggregate(total_kili_output=Sum('amount_in_usd'))['total_kili_output']
    total_kili_resources = kili_resources.count()
    #######################################

    number_output = output.count()
    total_output = output.aggregate(total_output=Sum('amount_in_usd'))['total_output']

    number_input = input.count()
    total_input = input.aggregate(total_input=Sum('amount_in_usd'))['total_input']

    number_resources = resources.count()
    number_projects = projects.count()

    caisse = total_input-total_output
    total_compte_kavatsi_input = compte_kavatsi_input.aggregate(total_compte_kavatsi_input=Sum('amount_in_usd'))['total_compte_kavatsi_input'] 
    total_compte_bureau_input = compte_bureau_input.aggregate(total_compte_bureau_input=Sum('amount_in_usd'))['total_compte_bureau_input']
    total_compte_kavatsi_output = compte_kavatsi_output.aggregate(total_compte_kavatsi_output=Sum('amount_in_usd'))['total_compte_kavatsi_output'] 
    total_compte_bureau_output = compte_bureau_output.aggregate(total_compte_bureau_output=Sum('amount_in_usd'))['total_compte_bureau_output']
    total_compte_autre_input = compte_autre_input.aggregate(total_compte_autre_input=Sum('amount_in_usd'))['total_compte_autre_input']
    total_compte_autre_output = compte_autre_output.aggregate(total_compte_autre_output=Sum('amount_in_usd'))['total_compte_autre_output']
    
    nombre_ouvriers = ouvriers.count() + personel_bureau.count()
    nombre_locataire_nziapanda = locataire_nziapanda.count()

    compte_kavatsi_balance = total_compte_kavatsi_input - total_compte_kavatsi_output
    compte_bureau_balance = total_compte_bureau_input - total_compte_bureau_output
    compte_autre_balance = total_compte_autre_input - total_compte_autre_output

    return render(request, 'management/synthetic_report.html', {
        'number_output': number_output,
        'number_input' : number_input,
        'total_output' : total_output,
        'total_input' : total_input,
        'caisse' : caisse,
        'nombre_ouvriers': nombre_ouvriers,
        'nombre_locataire_nziapanda': nombre_locataire_nziapanda,
        'number_resources': number_resources,
        'number_projects': number_projects,
        'total_compte_kavatsi_input': total_compte_kavatsi_input,
        'total_compte_bureau_input': total_compte_bureau_input,
        'total_compte_kavatsi_output': total_compte_kavatsi_output,
        'total_compte_bureau_output': total_compte_bureau_output,
        'compte_kavatsi_balance': compte_kavatsi_balance,
        'compte_bureau_balance': compte_bureau_balance,
        'total_compte_autre_output': total_compte_autre_output,
        'total_compte_autre_input': total_compte_autre_input,
        'compte_autre_balance': compte_autre_balance,
        'total_kili_input': total_kili_input,
        'total_kili_output': total_kili_output,
        'total_kili_resources': total_kili_resources,
        })



def accounts(request):
    query = request.GET.get('query')
    persons = Person.objects.all()
    agents_bureau = persons.filter(position='A')
    labour = persons.filter(position='B')
    locataires = persons.filter(position='E' or 'F')

    if query:
        persons = persons.filter(
            Q(first_name__icontains=query) | Q(job_description__icontains=query) | Q(address__icontains=query))

    return render(request, 'management/accounts.html', {
        'persons': persons,
        'agents_bureau': agents_bureau,
        'labour': labour,
        'locataires': locataires,
        'query': query if query is not None else '',
    })


def finances_outputs(request):
    query = request.GET.get('query_finance')
    finance_affairs = Finance.objects.all()
    outputs = finance_affairs.filter(type_transaction='OP')
    finances = outputs

    if query:
        finances = outputs.filter(Q(code__icontains=query) | Q(account__icontains=query))

    return render(request, 'management/finances_outputs.html', {
        'query': query if query is not None else '',
        'finances': finances,
})


def finances_inputs(request):
    query = request.GET.get('query_finance')
    finance_affairs = Finance.objects.all()
    inputs = finance_affairs.filter(type_transaction='IP')
    finances = inputs

    if query:
        finances = inputs.filter(Q(code__icontains=query))

    return render(request, 'management/finances_inputs.html', {
        'query': query if query is not None else '',
        'finances': finances,
})



def accounts_balance(request):
    kavatsi_input = Finance.objects.filter(account='Kasereka_Kavatsi', type_transaction='IP')
    kavatsi_output = Finance.objects.filter(account='Kasereka_Kavatsi', type_transaction='OP')
    total_kavatsi_input = kavatsi_input.aggregate(total_kavatsi_input=Sum('amount_in_usd'))['total_kavatsi_input'] 
    total_kavatsi_output = kavatsi_output.aggregate(total_kavatsi_output=Sum('amount_in_usd'))['total_kavatsi_output'] 

    syalivene_input = Finance.objects.filter(account='Katembo_Syalivene', type_transaction='IP')
    syalivene_output = Finance.objects.filter(account='Katembo_Syalivene', type_transaction='OP')
    total_syalivene_input = syalivene_input.aggregate(total_syalivene_input=Sum('amount_in_usd'))['total_syalivene_input'] 
    total_syalivene_output = syalivene_output.aggregate(total_syalivene_output=Sum('amount_in_usd'))['total_syalivene_output'] 

    vikoma_input = Finance.objects.filter(account='Kahindo_Vikoma', type_transaction='IP')
    vikoma_output = Finance.objects.filter(account='Kahindo_Vikoma', type_transaction='OP')
    total_vikoma_input = vikoma_input.aggregate(total_vikoma_input=Sum('amount_in_usd'))['total_vikoma_input'] 
    total_vikoma_output = vikoma_output.aggregate(total_vikoma_output=Sum('amount_in_usd'))['total_vikoma_output']

    outputs = Comptes.objects.filter(transaction='OP')
    inputs = Comptes.objects.filter(transaction='IP')
    persons =  Person.objects.all()
    query = request.GET.get('query')
    if query:
        persons = persons.filter(Q(first_name__icontains=query))
    persons_with_finances = []

    for person in persons:
        output = outputs.filter(nom=person)
        input = inputs.filter(nom=person)
        total_outputs = output.aggregate(total_outputs=Sum('amount_in_usd'))['total_outputs'] 
        total_inputs = input.aggregate(total_inputs=Sum('amount_in_usd'))['total_inputs']
        
        if person.first_name == 'Kasereka_Kavatsi':
            kavatsi_outputs = total_outputs + total_kavatsi_input
            kavatsi_inputs = total_inputs + total_kavatsi_output
            kavatsi_balance = kavatsi_outputs - kavatsi_inputs
            persons_with_finances.append({'person': person, 'total_outputs': kavatsi_outputs, 'total_inputs': kavatsi_inputs, 'total_balance': kavatsi_balance})
        
        elif person.first_name == 'Katembo_Syalivene':
            syalivene_outputs = total_outputs + total_syalivene_input
            syalivene_inputs = total_inputs + total_syalivene_output
            syalivene_balance = syalivene_outputs - syalivene_inputs
            persons_with_finances.append({'person': person, 'total_outputs': syalivene_outputs, 'total_inputs': syalivene_inputs, 'total_balance': syalivene_balance})

        elif person.first_name == 'Kahindo_Vikoma':
            vikoma_outputs = total_outputs + total_vikoma_input
            vikoma_inputs = total_inputs + total_vikoma_output
            vikoma_balance = vikoma_outputs - vikoma_inputs
            persons_with_finances.append({'person': person, 'total_outputs': vikoma_outputs, 'total_inputs': vikoma_inputs, 'total_balance': vikoma_balance})

        elif total_outputs is None or total_inputs is None:
            persons_with_finances.append({'person': person, 'total_outputs': 0, 'total_inputs': 0, 'total_balance': 0})
        else:
            total_balance = total_outputs - total_inputs
            persons_with_finances.append({'person': person, 'total_outputs': total_outputs, 'total_inputs': total_inputs, 'total_balance': total_balance})

    return render(request, 'management/accounts_balance.html', {
        'persons_with_finances': persons_with_finances,
        'query': query if query is not None else '',
})



def account_details(request, pk):
    account_detail = get_object_or_404(Person, pk=pk)
    return render(request, 'management/account_details.html', {
        'account_details': account_detail,
    })


def transaction_details(request, pk):
    transaction_detail = get_object_or_404(Person, pk=pk)
    account = Comptes.objects.filter(nom=transaction_detail.pk)
    finances = Finance.objects.filter(account=transaction_detail.first_name)
    if account is not None:
        outputs = account.filter(transaction='OP')
        sum_outputs = outputs.aggregate(sum_outputs=Sum('amount_in_usd'))['sum_outputs']
        inputs = account.filter(transaction='IP')
        sum_inputs = inputs.aggregate(sum_inputs=Sum('amount_in_usd'))['sum_inputs']
    else:
        outputs = 0
        sum_outputs = 0
        inputs = 0
        sum_inputs = 0

    if finances is not None:
        finance_outputs = finances.filter(type_transaction='OP')
        sum_finance_outputs = finance_outputs.aggregate(sum_finance_outputs=Sum('amount_in_usd'))['sum_finance_outputs']
        finance_inputs = finances.filter(type_transaction='IP')
        sum_finance_inputs = finance_inputs.aggregate(sum_finance_inputs=Sum('amount_in_usd'))['sum_finance_inputs']
    else:
        finance_outputs = 0
        finance_inputs = 0
        sum_finance_inputs = 0
        sum_finance_outputs = 0

    return render(request, 'management/transaction_details.html', {
        'transaction_detail': transaction_detail,
        'outputs': outputs,
        'sum_outputs': sum_outputs,
        'inputs': inputs,
        'sum_inputs': sum_inputs,
        'finance_outputs': finance_outputs,
        'finance_inputs': finance_inputs,
        'sum_finance_outputs': sum_finance_outputs,
        'sum_finance_inputs': sum_finance_inputs,
    })



@login_required
def new_finance(request):
    if request.method == 'POST':
        form = NewFinanceForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('management:synthetic_report')
    else:
        form = NewFinanceForm()

    return render(request, 'management/forms.html', {
        'form': form,
        'title': 'Nouvel enregistrement'
    })