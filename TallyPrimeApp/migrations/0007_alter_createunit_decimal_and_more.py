# Generated by Django 4.0.4 on 2022-06-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0006_creategodown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createunit',
            name='decimal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='createunit',
            name='formal_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='createunit',
            name='symbol',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createunit',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
