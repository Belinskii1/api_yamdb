# Generated by Django 2.2.16 on 2022-01-19 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220119_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={},
        ),
        migrations.RemoveField(
            model_name='title',
            name='pub_date',
        ),
    ]