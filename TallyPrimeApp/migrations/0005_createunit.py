# Generated by Django 4.0.4 on 2022-06-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0004_createstockcateg'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=20)),
                ('formal_name', models.CharField(max_length=50)),
                ('uqc', models.CharField(max_length=50)),
                ('decimal', models.IntegerField()),
            ],
        ),
    ]
