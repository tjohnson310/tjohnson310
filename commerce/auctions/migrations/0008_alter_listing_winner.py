# Generated by Django 4.2.14 on 2024-07-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='winner',
            field=models.CharField(default='No winner', max_length=100),
        ),
    ]
