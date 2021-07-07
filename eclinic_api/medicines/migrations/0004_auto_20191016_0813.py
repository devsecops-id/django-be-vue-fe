# Generated by Django 2.2.6 on 2019-10-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_recipe_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipeitem',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipeitem',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
