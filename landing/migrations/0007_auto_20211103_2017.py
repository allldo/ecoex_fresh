# Generated by Django 3.2.9 on 2021-11-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20211103_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
        migrations.RemoveField(
            model_name='news',
            name='created',
        ),
    ]