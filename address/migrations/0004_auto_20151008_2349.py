# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20151008_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300)),
                ('modification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('movie_description', models.TextField()),
                ('movie_name', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(null=True, related_name='addresses', to='address.Profile', blank=True),
        ),
    ]
