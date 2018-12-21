# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0011_ctinstance_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctinstance',
            name='collection',
        ),
        migrations.AddField(
            model_name='ctinstance',
            name='collection_many',
            field=models.ManyToManyField(related_name='collection_many_rel_+', to='extra.CTInstance', blank=True),
        ),
    ]
