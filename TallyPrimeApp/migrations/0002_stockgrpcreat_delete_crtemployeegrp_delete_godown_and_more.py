# Generated by Django 4.0.4 on 2022-06-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockGrpCreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under_name', models.CharField(max_length=50)),
                ('quantities', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CrtEmployeeGrp',
        ),
        migrations.DeleteModel(
            name='Godown',
        ),
        migrations.DeleteModel(
            name='Primary',
        ),
        migrations.DeleteModel(
            name='StockGroupCrt',
        ),
        migrations.DeleteModel(
            name='StockGrpCateg',
        ),
        migrations.DeleteModel(
            name='UnitCrt',
        ),
    ]