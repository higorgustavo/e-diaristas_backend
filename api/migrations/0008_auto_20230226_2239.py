# Generated by Django 3.2.8 on 2023-02-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_diaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='complemento',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='diaria',
            name='data_atendimento',
            field=models.DateTimeField(),
        ),
    ]
