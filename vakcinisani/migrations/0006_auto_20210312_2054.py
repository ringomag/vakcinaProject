# Generated by Django 3.1.7 on 2021-03-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vakcinisani', '0005_auto_20210311_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakcinisan',
            name='jmbg',
            field=models.IntegerField(),
        ),
    ]