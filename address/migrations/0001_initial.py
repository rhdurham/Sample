# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(to='address.Profile'),
        ),
    ]
