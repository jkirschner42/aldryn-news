# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_news', '0002_newstextlinkplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstextlinkplugin',
            name='name',
            field=models.CharField(default='Link Name', max_length=256, verbose_name='name'),
            preserve_default=False,
        ),
    ]
