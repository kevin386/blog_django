# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150308_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='digest',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name='\u6458\u8981', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='\u53d1\u5e03\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
