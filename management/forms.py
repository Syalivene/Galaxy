from django import forms
from .models import Finance, Person
#from dal import autocomplete



INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSES_B = 'w-2/3 py-2 px-3 rounded-xl border'

class NewFinanceForm(forms.ModelForm):
    amount_in_usd = forms.CharField(widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'montant...ex. 24'
            }))
    created_at = forms.DateField(widget=forms.DateInput(attrs={
                'required': True,
                'class': INPUT_CLASSES_B,
                'type': 'date'
            }))

    class Meta:        
        model = Finance
        fields = ('type_transaction', 'account', 'amount_in_usd', 'origin_location', 'origin_person', 'origin_project', 'destination_location', 'destination_person', 'destination_project', 'argument_explaination', 'authorizer_boss', 'authorizer_manager', 'authorizer_secretary', 'created_at')

        widgets = {
            'account': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True
            }),

            'type_transaction': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': True,
            }),
            'origin_location': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir milieu de provenance'
            }),
            'origin_person': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir expediteur'
            }),
            'origin_project': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir project generateur'
            }),
            'destination_location': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir milieu de destination'
            }),
            'destination_person': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir personne destinataire'
            }),
            'destination_project': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
                'placeholder': 'Choisir projet de destination'
            }),
            'argument_explaination': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. restauration bureau'
            }),
            'authorizer_boss': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': False,
            }),
            'authorizer_manager': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': False
            }),
            'authorizer_secretary': forms.Select(attrs={
                'class': INPUT_CLASSES_B,
                'required': False
            }),
        }
