# Generated by Django 3.2 on 2023-03-01 07:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_event_end_date_event_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='discription',
            field=tinymce.models.HTMLField(),
        ),
    ]
