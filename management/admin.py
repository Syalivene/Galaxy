from django.contrib import admin
from django.db.models.functions import Lower
from django.utils.html import format_html
from .models import Person, Resources, Projects, Finance, Comptes, Stock



admin.site.site_header = 'KAVATSI Agri System'
admin.site.site_title = 'management'
admin.site.index_title = 'Index Title'
###########################################################

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'position', 'job_description', 'birth_date', 'sex', 'education', 'address', 'email', 'mobile_number', 'whatsapp_number', 'created_at')
    search_fields = ['first_name']
    ordering = [Lower('first_name')]


admin.site.register(Person, PersonAdmin)
#################################################################


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('resource_name', 'type', 'description', 'location', 'manager_name', 'acquisition_date')
    search_fields = ('resource_name', 'type', 'description', 'location', 'acquisition_date')

admin.site.register(Resources, ResourcesAdmin)
#####################################################################################



class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_code', 'type', 'location', 'description', 'initiation_date', 'end_date', 'project_manager', 'get_project_personel_names')
    search_fields = ('project_name', 'project_code', 'type', 'location', 'description', 'initiation_date', 'end_date')
    filter_horizontal = ('project_personel_names',)
    def get_project_personel_names(self, obj):
        return ', '.join([personel.first_name for personel in obj.project_personel_names.all()])

    get_project_personel_names.short_description = 'Project_Personel'  # Set a custom column header



admin.site.register(Projects, ProjectsAdmin)
#####################################################################################




class FinanceAdmin(admin.ModelAdmin):
    list_display = ('code', 'type_transaction', 'account', 'amount_in_usd', 'origin_location', 'origin_person', 'origin_project', 'destination_location', 'destination_person', 'destination_project', 'argument_explaination', 'authorizer_boss', 'authorizer_manager', 'authorizer_secretary', 'created_at')
    search_fields = ('code', 'type_transaction', 'account', 'amount_in_usd', 'origin_location', 'destination_location', 'argument_explaination')

admin.site.register(Finance, FinanceAdmin)
#####################################################################################


class ComptesAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'nom', 'amount_in_usd', 'justification', 'authorizer_secretary', 'contracted_at')
    search_fields = ['~nom__first_name__icontains']
    min_length = 4
    max_length = 30
admin.site.register(Comptes, ComptesAdmin)



#class StockAdmin(admin.ModelAdmin):
 #   list_display = ('transaction', 'nom_produit', 'unite_produit', 'quantite', 'prix_unitaire', 'date')
 #   search_fields = ['~nom_produit__icontains']

#admin.site.register(Stock, StockAdmin)
class StockAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'nom_produit', 'unite_produit', 'quantite', 'prix_unitaire', 'date')
    search_fields = ['nom_produit']

    class Media:
        css = {
            'all': ('admin/custom_admin.css',)
        }
        js = ('admin/custom_admin.js',)

admin.site.register(Stock, StockAdmin)