# Generated by Django 4.0.4 on 2022-07-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0024_payroll_crt'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll_crt',
            name='activate_voucher',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
