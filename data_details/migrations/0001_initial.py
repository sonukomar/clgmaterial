# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='chapters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='colleges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college_name', models.CharField(max_length=300)),
                ('University', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=300)),
                ('branch', models.ForeignKey(to='data_details.branches')),
            ],
        ),
        migrations.AddField(
            model_name='chapters',
            name='subject',
            field=models.ForeignKey(to='data_details.subjects'),
        ),
    ]
