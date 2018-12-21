# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0005_runtimerelation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runtimerelation',
            name='collection',
        ),
        migrations.AddField(
            model_name='runtimerelation',
            name='collection1',
            field=models.ManyToManyField(related_name='many_to_many', to='extra.CT'),
        ),
        migrations.AddField(
            model_name='runtimerelation',
            name='collection2',
            field=models.ForeignKey(related_name='One_to_one', blank=True, to='extra.CT', null=True),
        ),
    ]
