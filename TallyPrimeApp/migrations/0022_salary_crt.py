# Generated by Django 4.0.4 on 2022-07-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0021_payhead_crt'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('per', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]