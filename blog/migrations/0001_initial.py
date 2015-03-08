# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('votes', models.IntegerField(default=0, verbose_name='\u6295\u7968')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategorySub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5b50\u5206\u7c7b')),
                ('parent', models.ForeignKey(default=blog.models.default_category, verbose_name='\u5206\u7c7b', to='blog.Category')),
            ],
            options={
                'verbose_name': '\u5b50\u5206\u7c7b',
                'verbose_name_plural': '\u5b50\u5206\u7c7b\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=32, verbose_name='\u7528\u6237')),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail', blank=True)),
                ('content', models.CharField(max_length=64, verbose_name='\u8bc4\u8bba')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('votes', models.IntegerField(default=0)),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', blank=True, to='blog.Article', null=True)),
                ('reply', models.ForeignKey(verbose_name='\u56de\u590d', blank=True, to='blog.Comment', null=True)),
            ],
            options={
                'ordering': ['-create_date'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceFrom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, verbose_name='\u5f15\u7528', blank=True)),
                ('excerpt', models.CharField(max_length=128, null=True, verbose_name='\u6458\u81ea', blank=True)),
            ],
            options={
                'verbose_name': '\u5f15\u7528',
                'verbose_name_plural': '\u5f15\u7528\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='cat_sub',
            field=models.ForeignKey(default=blog.models.default_sub_category, verbose_name='\u5206\u7c7b', to='blog.CategorySub'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=blog.models.default_category, verbose_name='\u5206\u7c7b', to='blog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.OneToOneField(null=True, blank=True, to='blog.ReferenceFrom', verbose_name='\u5f15\u7528'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', null=True, verbose_name='\u6807\u7b7e', blank=True),
            preserve_default=True,
        ),
    ]
