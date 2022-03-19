# Generated by Django 4.0.3 on 2022-03-19 18:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comments_commenton_alter_listings_dateposted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentOn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listings'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='datePosted',
            field=models.DateField(default=datetime.datetime(2022, 3, 19, 23, 53, 14, 804031)),
        ),
    ]
