# Generated by Django 3.2.8 on 2023-03-03 00:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20230226_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaria',
            name='candidatos',
        ),
        migrations.AddField(
            model_name='diaria',
            name='candidatas',
            field=models.ManyToManyField(blank=True, related_name='candidatas', to=settings.AUTH_USER_MODEL),
        ),
    ]
