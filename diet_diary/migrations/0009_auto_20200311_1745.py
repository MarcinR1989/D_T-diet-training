# Generated by Django 3.0.4 on 2020-03-11 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0008_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodproduct',
            name='carbs_per_100ml',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='fat_per_100ml',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='kcal_per_100ml',
        ),
        migrations.RemoveField(
            model_name='foodproduct',
            name='protein_per_100ml',
        ),
    ]
