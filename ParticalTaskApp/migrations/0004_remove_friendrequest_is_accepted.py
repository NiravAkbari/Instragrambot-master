# Generated by Django 4.2.3 on 2023-07-19 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParticalTaskApp', '0003_friendrequest_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='is_accepted',
        ),
    ]
