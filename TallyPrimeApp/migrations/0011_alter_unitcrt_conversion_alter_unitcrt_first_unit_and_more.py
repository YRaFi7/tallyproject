# Generated by Django 4.0.4 on 2022-07-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0010_unitcrt_delete_createunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitcrt',
            name='conversion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='unitcrt',
            name='first_unit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unitcrt',
            name='second_unit',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='unitcrt',
            name='uqc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
