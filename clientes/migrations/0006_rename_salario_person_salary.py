# Generated by Django 3.2 on 2021-04-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_rename_salary_person_salario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='salario',
            new_name='salary',
        ),
    ]
