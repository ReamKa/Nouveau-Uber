# Generated by Django 3.2.8 on 2021-11-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideRequest', '0002_auto_20211112_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodePromo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_promo', models.CharField(max_length=5)),
            ],
        ),
    ]