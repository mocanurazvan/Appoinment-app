# Generated by Django 5.1.4 on 2025-01-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_rename_date_programare_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serviciu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('descriere', models.TextField(blank=True, null=True)),
                ('pret', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Programare',
        ),
    ]