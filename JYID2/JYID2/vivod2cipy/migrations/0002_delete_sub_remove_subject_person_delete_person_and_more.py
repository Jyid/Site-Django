# Generated by Django 4.1.7 on 2023-05-11 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vivod', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='person',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
