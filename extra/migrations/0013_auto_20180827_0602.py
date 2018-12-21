# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0012_auto_20180823_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runtimerelation',
            name='collection_many',
        ),
        migrations.RemoveField(
            model_name='runtimerelation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='runtimerelation',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='runtimerelation',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='RuntimeRelation',
        ),
    ]
