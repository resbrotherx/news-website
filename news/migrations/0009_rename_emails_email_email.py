# Generated by Django 4.1.7 on 2023-02-27 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_rename_emais_email_emails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='emails',
            new_name='email',
        ),
    ]
