# Generated by Django 3.2.6 on 2023-10-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoomparticipant',
            name='absent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='zoomparticipant',
            name='leave',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='zoomparticipant',
            name='present',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
