# Generated by Django 5.1.4 on 2025-01-04 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_clienta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('ora', models.TimeField()),
                ('clienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.clienta')),
                ('serviciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.serviciu')),
            ],
        ),
    ]