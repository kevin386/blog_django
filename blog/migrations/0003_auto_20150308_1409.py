# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150308_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='digest',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name='\u6807\u9898', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='cat_sub',
            field=models.ForeignKey(verbose_name='\u5b50\u5206\u7c7b', blank=True, to='blog.CategorySub', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65e5\u671f', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name='\u6807\u9898'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='votes',
            field=models.IntegerField(default=0, null=True, verbose_name='\u6295\u7968'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='referencefrom',
            name='url',
            field=models.URLField(null=True, verbose_name='\u6765\u81ea', blank=True),
            preserve_default=True,
        ),
    ]
