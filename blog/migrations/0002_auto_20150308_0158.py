# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cat_sub',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', blank=True, to='blog.CategorySub', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='blog.Category', null=True),
            preserve_default=True,
        ),
    ]
