# Generated by Django 5.0.1 on 2024-01-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_alter_finance_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='account',
            field=models.CharField(blank=True, choices=[('Bureau_Central', 'Bureau_Central'), ('Katembo_Syalivene', 'Katembo_Syalivene'), ('Kasereka_Kavatsi', 'Kasereka_Kavatsi'), ('Louange_Vikoma', 'Louange_Vikoma')], max_length=25, null=True),
        ),
    ]
