# Generated by Django 5.1.2 on 2024-10-29 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creador', to='gtareas.usuario'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_tareas', to='gtareas.proyecto'),
        ),
    ]
