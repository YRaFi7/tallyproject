# Generated by Django 4.0.4 on 2022-07-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0017_bank_crt'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under_name', models.CharField(max_length=50)),
                ('attendance', models.CharField(max_length=50)),
                ('period', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
    ]
