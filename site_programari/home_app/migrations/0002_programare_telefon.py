# Generated by Django 5.1.4 on 2024-12-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programare',
            name='telefon',
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
    ]