# Generated by Django 3.2.6 on 2023-10-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20231026_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoomparticipant',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
