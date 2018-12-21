# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0003_relationship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='destination',
            new_name='child_id',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='source',
            new_name='parent_id',
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relation_type',
            field=models.SmallIntegerField(default=1, choices=[(1, b'One-to-One'), (2, b'One-to-Many'), (4, b'Many-to-Many'), (3, b'Many-to-One')]),
        ),
    ]
