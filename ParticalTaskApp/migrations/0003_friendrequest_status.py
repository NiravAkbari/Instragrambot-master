# Generated by Django 4.2.3 on 2023-07-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParticalTaskApp', '0002_friendship_friendrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]