# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0006_auto_20180820_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtimerelation',
            name='collection1',
            field=models.ManyToManyField(related_name='many_to_many', to='extra.CTInstance'),
        ),
        migrations.AlterField(
            model_name='runtimerelation',
            name='collection2',
            field=models.ForeignKey(related_name='One_to_one', blank=True, to='extra.CTInstance', null=True),
        ),
    ]
