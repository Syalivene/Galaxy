# Generated by Django 5.0.1 on 2024-01-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_comptes_amount_in_usd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='account',
            field=models.CharField(choices=[('MN', 'Main'), ('KG', 'Katembo_Syalivene'), ('KS', 'Kavatsi'), ('LV', 'Louange_Vikoma'), ('OT', 'Other')], max_length=25),
        ),
    ]
