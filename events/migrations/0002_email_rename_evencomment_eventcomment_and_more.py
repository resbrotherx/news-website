# Generated by Django 4.1.7 on 2023-02-28 05:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emais', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='EvenComment',
            new_name='EventComment',
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='little_discription',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
