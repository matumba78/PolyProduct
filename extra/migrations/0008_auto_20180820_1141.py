# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0007_auto_20180820_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runtimerelation',
            old_name='collection1',
            new_name='collection',
        ),
        migrations.RenameField(
            model_name='runtimerelation',
            old_name='collection2',
            new_name='container_name',
        ),
    ]
