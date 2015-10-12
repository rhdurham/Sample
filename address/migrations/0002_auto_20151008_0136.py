# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(blank=True, to='address.Profile'),
        ),
    ]
