# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.ForeignKey(to='data_details.branches')),
                ('chapter', models.ForeignKey(to='data_details.chapters')),
                ('college', models.ForeignKey(to='data_details.colleges')),
                ('subject', models.ForeignKey(to='data_details.subjects')),
            ],
        ),
    ]
