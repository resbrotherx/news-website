# Generated by Django 4.1.7 on 2023-02-27 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_emails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emails',
            new_name='Email',
        ),
    ]