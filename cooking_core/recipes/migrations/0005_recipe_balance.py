# Generated by Django 4.2 on 2023-05-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_created_date_recipe_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='balance',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]