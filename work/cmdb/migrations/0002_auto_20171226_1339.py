# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-26 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='Sex',
        ),
        migrations.AlterField(
            model_name='loginlog',
            name='LoginIP',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
    ]
