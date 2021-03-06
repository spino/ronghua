# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20171128_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrange',
            name='fri',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='mon',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='sat',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='sun',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='thu',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='tue',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
        migrations.AddField(
            model_name='arrange',
            name='wed',
            field=models.CharField(choices=[('MO', '上午'), ('AF', '下午'), ('WH', '全天'), ('DA', '休息')], default='DA', max_length=10),
        ),
    ]
