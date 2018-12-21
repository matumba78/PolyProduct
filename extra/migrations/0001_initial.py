# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'CT',
            },
        ),
        migrations.CreateModel(
            name='CTInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('ct', models.ForeignKey(to='extra.CT')),
            ],
            options={
                'verbose_name_plural': 'CTInstance',
            },
        ),
        migrations.CreateModel(
            name='ExtraField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(default=1, max_length=10, choices=[(b'INT', b'Number'), (b'CH', b'Character'), (b'DT', b'Date'), (b'DEC', b'Decimal')])),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('container_type', models.ForeignKey(to='extra.CT')),
            ],
            options={
                'verbose_name_plural': 'ExtraField',
            },
        ),
        migrations.CreateModel(
            name='Extrafield_values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value_int', models.IntegerField(null=True, blank=True)),
                ('value_char', models.CharField(max_length=255, null=True, blank=True)),
                ('value_date', models.DateTimeField(null=True, blank=True)),
                ('value_dec', models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)),
                ('extrafield', models.ForeignKey(related_name='ef_values', to='extra.ExtraField')),
            ],
            options={
                'verbose_name_plural': 'Values',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='extrafield',
            name='created_by',
            field=models.ForeignKey(related_name='extra_extrafield_updated', to='extra.User'),
        ),
        migrations.AddField(
            model_name='extrafield',
            name='updated_by',
            field=models.ForeignKey(related_name='extra_extrafield_created', to='extra.User'),
        ),
        migrations.AddField(
            model_name='ctinstance',
            name='ef_values',
            field=models.ForeignKey(to='extra.Extrafield_values'),
        ),
        migrations.AddField(
            model_name='ct',
            name='created_by',
            field=models.ForeignKey(related_name='extra_ct_updated', to='extra.User'),
        ),
        migrations.AddField(
            model_name='ct',
            name='updated_by',
            field=models.ForeignKey(related_name='extra_ct_created', to='extra.User'),
        ),
    ]
