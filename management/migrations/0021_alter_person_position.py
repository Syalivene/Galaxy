# Generated by Django 5.0.1 on 2024-01-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_alter_finance_account_alter_projects_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(blank=True, choices=[('E', 'Boss'), ('A', 'Agent Bureau'), ('B', 'Ouvrier'), ('E', 'Locataire_nziapanda'), ('F', 'Locataire_Kasiki'), ('C', 'Collaborateur'), ('D', 'Autre')], max_length=1, null=True),
        ),
    ]