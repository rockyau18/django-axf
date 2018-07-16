# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-12 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=64)),
                ('o_status', models.IntegerField(default=0)),
                ('o_create', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.UserModel')),
            ],
        ),
        migrations.AddField(
            model_name='ordergoodsmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.OrderModel'),
        ),
    ]