# Generated by Django 3.1.7 on 2021-03-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vakcinisani', '0009_auto_20210327_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakcinisan',
            name='jmbg',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
