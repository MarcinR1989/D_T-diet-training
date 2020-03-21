# Generated by Django 3.0.4 on 2020-03-11 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0003_auto_20200311_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodproduct',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='volume_kcal',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='weight_kcal',
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='carbs_per_100g',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='carbs_per_100ml',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='fat_per_100g',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='fat_per_100ml',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='kcal_per_100g',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='kcal_per_100ml',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='protein_per_100g',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='protein_per_100ml',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]