# Generated by Django 4.0.4 on 2022-07-18 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0014_employee_crt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_crt',
            old_name='function',
            new_name='function_name',
        ),
    ]
