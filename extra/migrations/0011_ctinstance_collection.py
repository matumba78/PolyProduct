# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0010_auto_20180821_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctinstance',
            name='collection',
            field=models.ManyToManyField(related_name='collection_rel_+', to='extra.CTInstance', blank=True),
        ),
    ]
