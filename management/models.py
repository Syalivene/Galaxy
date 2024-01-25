from django.db import models
import random
import string
from .variables import LOCATION_CHOICES, UNIT_CHOICES, TYPE_CHOICES_3, TYPE_CHOICES_1, ACCOUNT_CHOICES, GENDER_CHOICES, TYPE_CHOICES_2, JUSTIFICATION_CHOICES, POSITION_CHOICES



class Person(models.Model):

    first_name = models.CharField(max_length=20, null=True, blank = True)
    second_name = models.CharField(max_length=20, null=True, blank = True)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, null=True, blank = True)
    job_description = models.TextField(null=True, blank = True)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank = True)
    education = models.CharField(max_length=100, null=True, blank = True)
    address = models.TextField(null=True, blank = True)
    email = models.EmailField(null=True, blank = True)
    mobile_number = models.CharField(max_length=15, null=True, blank = True) 
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name
##########################################################################################################################
    



class Resources(models.Model):

    resource_name = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES_1)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    description = models.TextField(blank=True, null=True)
    acquisition_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    manager_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ['-registration_date']

    def __str__(self):
        return self.resource_name
 ###############################################################################################################   




class Projects(models.Model):

    project_name = models.CharField(max_length=30)
    project_code = models.CharField(max_length=30, default='P0001')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES_1)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    description = models.TextField()
    initiation_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project_manager = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    project_personel_names = models.ManyToManyField(Person, related_name='project_personel_list', blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ['-registration_date']

    def __str__(self):
        return self.project_name
 #############################################################################################################################   

def generate_unique_code():
    length = 6
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class Finance(models.Model):
 
    type_transaction = models.CharField(max_length=2, choices=TYPE_CHOICES_2)
    account = models.CharField(max_length=25, blank=True, null=True, choices=ACCOUNT_CHOICES)
    amount_in_usd = models.FloatField(blank=True, null=True)
    origin_location = models.CharField(max_length=2, choices=LOCATION_CHOICES, blank=True, null=True)
    origin_person = models.ForeignKey(Person, related_name='finance_origin_person', blank=True, null=True, on_delete=models.CASCADE)
    origin_project = models.ForeignKey(Projects, related_name = 'finance_origin_project', blank=True, null=True, on_delete=models.CASCADE)
    destination_location = models.CharField(max_length=2, choices=LOCATION_CHOICES, blank=True, null=True)
    destination_person = models.ForeignKey(Person, related_name='finance_destination_person', blank=True, null=True, on_delete=models.CASCADE)
    destination_project = models.ForeignKey(Projects, related_name = 'finance_destination_project', blank=True, null=True, on_delete=models.CASCADE)
    argument_explaination = models.TextField(blank=True, null=True)
    authorizer_boss = models.ForeignKey(Person, default=5, related_name='finance_authorizer_boss', blank=True, null=True, on_delete=models.CASCADE)
    authorizer_manager = models.ForeignKey(Person, default=6, related_name='finance_authorizer_manager', blank=True, null=True, on_delete=models.CASCADE)
    authorizer_secretary = models.ForeignKey(Person, default=12, related_name='finance_authorizer_secretary', blank=True, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True, default=generate_unique_code)
    created_at = models.DateField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        ordering = ['-registration_date']

    def save(self, *args, **kwargs):
        if not self.code:
            unique_code = generate_unique_code()
            self.code = unique_code
        super().save(*args, **kwargs)


    def __str__(self):
        return self.type_transaction
    

class Comptes(models.Model):
    
    transaction = models.CharField(max_length=2, choices=TYPE_CHOICES_2)
    nom = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount_in_usd = models.FloatField(blank=True, null=True)
    justification = models.TextField(max_length=2, choices=JUSTIFICATION_CHOICES, blank=True, null=True)
    authorizer_secretary = models.ForeignKey(Person, related_name='Comptes_authorizer_secretary', blank=True, null=True, on_delete=models.CASCADE)
    contracted_at = models.DateField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.transaction





class Stock(models.Model):
    transaction = models.CharField(max_length=2, choices=TYPE_CHOICES_3, blank=True, null=True,)
    nom_produit = models.ForeignKey(Resources, related_name='Stock_product_name', blank=True, null=True, on_delete=models.CASCADE)
    unite_produit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    quantite = models.FloatField(default=0)
    prix_unitaire = models.FloatField(default=0)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.transaction
    
