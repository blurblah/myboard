# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('memo', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateField(verbose_name=b'date published')),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
    ]
