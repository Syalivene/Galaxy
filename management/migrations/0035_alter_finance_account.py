# Generated by Django 5.0.1 on 2024-01-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0034_alter_finance_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='account',
            field=models.CharField(blank=True, choices=[('Bureau_Central', 'Bureau_Central'), ('Katembo_Syalivene', 'Katembo_Syalivene'), ('Kasereka_Kavatsi', 'Kasereka_Kavatsi'), ('Kahindo_Vikoma', 'Kahindo_Vikoma')], max_length=25, null=True),
        ),
    ]
