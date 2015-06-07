# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data_details', '0002_notes_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes_details',
            name='pdf_id',
            field=models.CharField(default=datetime.datetime(2015, 6, 7, 9, 14, 7, 573720, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
