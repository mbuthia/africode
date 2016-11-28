# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(max_length=80)),
                ('google_id', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('counrty', models.CharField(max_length=80)),
                ('zip_code', models.CharField(max_length=80)),
                ('mobile', models.CharField(max_length=80)),
                ('about_me', models.CharField(max_length=500)),
                ('avatar', models.CharField(max_length=80)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('screen_shot', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=500)),
                ('demo', models.CharField(max_length=200)),
                ('download', models.IntegerField()),
                ('reviews', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('payment_date', models.CharField(max_length=80)),
                ('payment_type', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('deduction', models.IntegerField()),
                ('net', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Item')),
            ],
        ),
    ]