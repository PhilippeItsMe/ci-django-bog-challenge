# Generated by Django 4.2.17 on 2024-12-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]
