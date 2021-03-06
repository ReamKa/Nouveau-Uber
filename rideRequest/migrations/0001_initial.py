# Generated by Django 3.2.8 on 2021-11-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceEstimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_latitude', models.BigIntegerField()),
                ('start_longitude', models.BigIntegerField()),
                ('end_latitude', models.BigIntegerField()),
                ('end_longitude', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeEstimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_latitude', models.BigIntegerField()),
                ('start_longitude', models.BigIntegerField()),
            ],
        ),
    ]
