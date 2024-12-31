# Generated by Django 4.1.2 on 2024-06-27 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundzero', '0004_alter_usuariocliente_numero_de_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('precio', models.IntegerField()),
                ('tecnica', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='Productos')),
            ],
        ),
    ]