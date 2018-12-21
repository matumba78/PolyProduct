# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0004_auto_20180817_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuntimeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, to='extra.CT', null=True)),
                ('created_by', models.ForeignKey(related_name='extra_runtimerelation_updated', to='extra.User')),
                ('updated_by', models.ForeignKey(related_name='extra_runtimerelation_created', to='extra.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
