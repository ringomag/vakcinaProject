# Generated by Django 3.1.7 on 2021-03-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vakcinisani', '0003_auto_20210311_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakcinisan',
            name='vakcina',
            field=models.CharField(choices=[('Fajzer', 'Fajzer'), ('Sputnjik', 'Sputnjik'), ('Astra Zeneka', 'Astra Zeneka'), ('Sinofarm', 'Sinofarm'), ('Moderna', 'Moderna')], max_length=100),
        ),
    ]