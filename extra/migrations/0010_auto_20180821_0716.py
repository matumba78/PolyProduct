# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0009_auto_20180821_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runtimerelation',
            old_name='collection_one',
            new_name='parent',
        ),
    ]
