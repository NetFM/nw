# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-09 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20180109_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carouselitem',
            old_name='page',
            new_name='visitor_express_page',
        ),
    ]
