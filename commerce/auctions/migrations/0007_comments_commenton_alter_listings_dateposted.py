# Generated by Django 4.0.3 on 2022-03-19 18:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listings_dateposted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='commentOn',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.listings'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listings',
            name='datePosted',
            field=models.DateField(default=datetime.datetime(2022, 3, 19, 23, 50, 35, 410193)),
        ),
    ]
