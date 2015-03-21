# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100, default='', blank=True)),
                ('person', models.CharField(max_length=100, default='', blank=True)),
            ],
            options={
                'ordering': ('time',),
            },
            bases=(models.Model,),
        ),
    ]
