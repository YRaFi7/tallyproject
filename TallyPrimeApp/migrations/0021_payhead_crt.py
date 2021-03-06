# Generated by Django 4.0.4 on 2022-07-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0020_alter_attendance_crt_alias_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payhead_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=100, null=True)),
                ('payhead_type', models.CharField(max_length=100, null=True)),
                ('income_type', models.CharField(max_length=100, null=True)),
                ('under_name', models.CharField(max_length=100, null=True)),
                ('net_salary', models.CharField(max_length=100, null=True)),
                ('pay_slip_name', models.CharField(max_length=100, null=True)),
                ('currency_ledger', models.CharField(max_length=100, null=True)),
                ('calculation_type', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
