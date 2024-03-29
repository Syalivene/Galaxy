# Generated by Django 5.0.1 on 2024-01-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_alter_person_position_comptes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='destination_location',
            field=models.CharField(blank=True, choices=[('KL', 'Kili'), ('KM', 'Kighali_kaghumo'), ('KW', 'Kisembwe'), ('KS', 'Kipese'), ('BB', 'Butembo'), ('KK', 'Kasiki'), ('KI', 'Kighali_Vitula'), ('OT', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='origin_location',
            field=models.CharField(blank=True, choices=[('KL', 'Kili'), ('KM', 'Kighali_kaghumo'), ('KW', 'Kisembwe'), ('KS', 'Kipese'), ('BB', 'Butembo'), ('KK', 'Kasiki'), ('KI', 'Kighali_Vitula'), ('OT', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='location',
            field=models.CharField(choices=[('KL', 'Kili'), ('KM', 'Kighali_kaghumo'), ('KW', 'Kisembwe'), ('KS', 'Kipese'), ('BB', 'Butembo'), ('KK', 'Kasiki'), ('KI', 'Kighali_Vitula'), ('OT', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='resources',
            name='location',
            field=models.CharField(choices=[('KL', 'Kili'), ('KM', 'Kighali_kaghumo'), ('KW', 'Kisembwe'), ('KS', 'Kipese'), ('BB', 'Butembo'), ('KK', 'Kasiki'), ('KI', 'Kighali_Vitula'), ('OT', 'Other')], max_length=2),
        ),
    ]
