# Generated by Django 3.0.7 on 2022-11-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20221129_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
