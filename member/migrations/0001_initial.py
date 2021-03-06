# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-10 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('card', models.IntegerField(primary_key=True, serialize=False, verbose_name='卡号')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(max_length=10, verbose_name='性别')),
                ('bir', models.CharField(default=None, max_length=20, verbose_name='生日')),
                ('pwd', models.CharField(max_length=30, verbose_name='密码')),
                ('inte', models.IntegerField(verbose_name='积分')),
                ('money', models.IntegerField(verbose_name='余额')),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
