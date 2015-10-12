# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20151008_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(null=True, to='address.Profile', blank=True),
        ),
    ]
