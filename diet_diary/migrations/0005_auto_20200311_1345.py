# Generated by Django 3.0.4 on 2020-03-11 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0004_auto_20200311_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodproduct',
            name='carbs_per_100g',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='carbs_per_100ml',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='fat_per_100g',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='fat_per_100ml',
            field=models.FloatField(blank=True, default=100, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='kcal_per_100g',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='kcal_per_100ml',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='protein_per_100g',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='foodproduct',
            name='protein_per_100ml',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
