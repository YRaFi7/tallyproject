# Generated by Django 4.0.4 on 2022-07-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TallyPrimeApp', '0013_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under_name', models.CharField(max_length=50)),
                ('doj', models.CharField(max_length=30)),
                ('salary', models.CharField(max_length=50)),
                ('empno', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('function', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('bld_grp', models.CharField(max_length=20)),
                ('father_mother', models.CharField(max_length=20)),
                ('spouse', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('phn', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=50)),
                ('incometax', models.CharField(max_length=20)),
                ('adhar', models.CharField(max_length=20)),
                ('uan', models.CharField(max_length=20)),
                ('pf', models.CharField(max_length=20)),
                ('pr', models.CharField(max_length=20)),
                ('esi', models.CharField(max_length=20)),
            ],
        ),
    ]
