# Generated by Django 3.2.6 on 2023-10-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20231026_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zoomparticipant',
            old_name='month',
            new_name='attendance_status',
        ),
        migrations.RemoveField(
            model_name='zoomparticipant',
            name='duration',
        ),
        migrations.AlterField(
            model_name='zoomparticipant',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='zoomparticipant',
            name='participant_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
