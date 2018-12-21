# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctinstance',
            name='ef_values',
        ),
        migrations.AddField(
            model_name='extrafield_values',
            name='ct_instance',
            field=models.ForeignKey(related_name='ct_instance', default=1, to='extra.CTInstance'),
            preserve_default=False,
        ),
    ]
