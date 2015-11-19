# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inflation',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='interest',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='unemployment',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
