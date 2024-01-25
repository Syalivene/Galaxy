# Generated by Django 5.0.1 on 2024-01-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0035_alter_finance_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finance',
            options={'ordering': ['-registration_date']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-registration_date']},
        ),
        migrations.AlterModelOptions(
            name='resources',
            options={'ordering': ['-registration_date']},
        ),
        migrations.AddField(
            model_name='resources',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]