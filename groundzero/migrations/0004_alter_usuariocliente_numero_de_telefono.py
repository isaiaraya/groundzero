# Generated by Django 5.0.6 on 2024-06-27 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundzero', '0003_usuariocliente_delete_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocliente',
            name='Numero_de_telefono',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]
