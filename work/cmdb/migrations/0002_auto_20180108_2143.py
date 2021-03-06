# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='LoginFail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loginlog',
            name='LoginIP',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loginlog',
            name='LoginStatus',
            field=models.CharField(blank=True, choices=[('T', 'Success'), ('F', 'Fail')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Sex',
            field=models.CharField(blank=True, choices=[('M', '男'), ('F', '女')], max_length=4, null=True),
        ),
    ]
