# Generated by Django 3.1.2 on 2020-11-04 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='titlehead',
        ),
    ]
