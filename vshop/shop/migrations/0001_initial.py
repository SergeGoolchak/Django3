# Generated by Django 3.0.3 on 2020-04-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('currency', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
            ],
        ),
    ]
