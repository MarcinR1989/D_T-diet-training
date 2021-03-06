# Generated by Django 3.0.4 on 2020-03-11 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0007_auto_20200311_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dish_kcal', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
