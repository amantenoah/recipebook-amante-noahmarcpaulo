# Generated by Django 5.1.6 on 2025-03-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
