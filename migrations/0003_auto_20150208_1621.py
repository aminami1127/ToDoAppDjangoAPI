# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20150127_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2015, 2, 8)),
            preserve_default=True,
        ),
    ]
