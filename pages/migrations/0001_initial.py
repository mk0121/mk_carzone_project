# Generated by Django 3.0.7 on 2022-11-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=255)),
                ('twitter_link', models.URLField(max_length=255)),
                ('google_plus_link', models.URLField(max_length=255)),
            ],
        ),
    ]
