# Generated by Django 5.1.6 on 2025-03-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_ingredient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
    ]
