# Generated by Django 5.1.3 on 2024-11-19 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtareas', '0002_alter_tarea_creador_alter_tarea_proyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
