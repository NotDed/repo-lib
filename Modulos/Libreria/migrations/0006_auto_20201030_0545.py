# Generated by Django 3.1.2 on 2020-10-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libreria', '0005_auto_20201030_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipoUser',
        ),
        migrations.AddField(
            model_name='usuario',
            name='adm',
            field=models.BooleanField(default=False),
        ),
    ]
