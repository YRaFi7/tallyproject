# Generated by Django 4.0.4 on 2022-07-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0011_alter_unitcrt_conversion_alter_unitcrt_first_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pancin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan', models.CharField(max_length=30)),
                ('cin', models.CharField(max_length=30)),
            ],
        ),
    ]
