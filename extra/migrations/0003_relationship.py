# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0002_auto_20180807_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('relation_type', models.SmallIntegerField(default=0, choices=[(0, b'One-to-One'), (1, b'One-to-Many'), (2, b'Many-toMany')])),
                ('created_by', models.ForeignKey(related_name='extra_relationship_updated', to='extra.User')),
                ('destination', models.ForeignKey(related_name='destination_relationships', to='extra.CT')),
                ('source', models.ForeignKey(related_name='source_relationships', to='extra.CT')),
                ('updated_by', models.ForeignKey(related_name='extra_relationship_created', to='extra.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
