# Generated by Django 5.1.4 on 2024-12-30 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_programare_telefon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programare',
            old_name='date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='programare',
            old_name='time',
            new_name='ora',
        ),
        migrations.RenameField(
            model_name='programare',
            old_name='service',
            new_name='serviciu',
        ),
        migrations.RemoveField(
            model_name='programare',
            name='email',
        ),
        migrations.RemoveField(
            model_name='programare',
            name='name',
        ),
    ]