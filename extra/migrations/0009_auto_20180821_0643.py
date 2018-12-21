# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0008_auto_20180820_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runtimerelation',
            old_name='collection',
            new_name='collection_many',
        ),
        migrations.RenameField(
            model_name='runtimerelation',
            old_name='container_name',
            new_name='collection_one',
        ),
    ]
