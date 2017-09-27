# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='')),
                ('url', models.CharField(max_length=64, verbose_name='')),
                ('status', models.BooleanField(verbose_name='')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='syscfg.Module')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
