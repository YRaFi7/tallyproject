# Generated by Django 4.0.4 on 2022-07-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0016_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accno', models.CharField(max_length=50)),
                ('ifsc_Code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
    ]
