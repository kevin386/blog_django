# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

def default_category():
    return Category.objects.first()

def default_sub_category():
    return CategorySub.objects.first()

class Category(models.Model):
    name = models.CharField(u"分类", max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u"分类"
        verbose_name_plural=u"分类列表"

class CategorySub(models.Model):
    name = models.CharField(u"子分类", max_length=64)
    parent = models.ForeignKey(Category, verbose_name=u"分类", default=default_category)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u"子分类"
        verbose_name_plural=u"子分类列表"

class Tag(models.Model):
    name = models.CharField(u"标签", max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u"标签"
        verbose_name_plural=u"标签列表"

class ReferenceFrom(models.Model):
    url = models.URLField(u'来自', blank=True, null=True)
    excerpt = models.CharField(u'摘自', max_length=128, blank=True, null=True)

    def __unicode__(self):
        return self.excerpt or self.url

    class Meta:
        verbose_name=u"引用"
        verbose_name_plural=u"引用列表"

class Article(models.Model):
    title = models.CharField(u"标题", max_length=128, null=True)
    digest = models.CharField(u"摘要", max_length=255, blank=True, null=True, default='')
    #一个分类有多篇文章（多对一关系）
    category = models.ForeignKey(Category, verbose_name=u"分类", null=True)
    # 子分类
    cat_sub = models.ForeignKey(CategorySub, verbose_name=u"子分类", blank=True, null=True)
    #一篇文章可以有多个标签，一个标签也可以标记多篇文章（多对多关系）
    tags = models.ManyToManyField(Tag, verbose_name=u"标签", blank=True, null=True)
    content = models.TextField(u"内容")
    create_date = models.DateTimeField(u"创建日期", auto_now_add=True, null=True)
    pub_date = models.DateTimeField(u"发布日期", null=True) # auto_now=True,
    # 一篇文章是否摘自其它博客
    reference = models.OneToOneField(ReferenceFrom, verbose_name=u'引用', blank=True, null=True)
    votes = models.IntegerField(u"投票", default=0, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-pub_date']
        verbose_name="文章"
        verbose_name_plural="文章列表"

    def category_disc(self):
        '''
        在admin list_display显示分类
        :return:
        '''
        return self.category.name
    category_disc.short_description = u'分类'

    def cat_sub_disc(self):
        '''
        在admin list_display显示子分类
        :return:
        '''
        return self.cat_sub.name
    cat_sub_disc.short_description = u'子分类'

    def tags_disc(self):
        '''
        在admin list_display显示标签
        :return:
        '''
        return ','.join([tag.name for tag in self.tags.all()])
    tags_disc.short_description = u'标签'

    def digest_disc(self):
        '''
        在list_display显示带html格式化的字段内容
        :return:
        '''
        from django.utils.html import format_html
        color = '00FF00'
        return format_html('<span style="color: #{0};">{1}</span>', color, self.digest)
    digest_disc.short_description = u'摘要'
    # 不使用format_html又不想转意htm标签，把allow_tags = True
    digest_disc.allow_tags = True

    def is_original_disc(self):
        '''
        在list_display显示是否文章原创
        :return:
        '''
        return not self.reference
    is_original_disc.short_description = u'原创'
    # 把True和False显示为勾和叉
    is_original_disc.boolean = True


class Comment(models.Model):
    user_name = models.CharField(u'用户', max_length=32)
    email = models.EmailField(u"E-mail", blank=True)
    content = models.CharField(u"评论", max_length=64)
    create_date = models.DateTimeField(u"创建日期",auto_now_add=True)
    votes = models.IntegerField(default=0)
    reply = models.ForeignKey("self", null=True, blank=True, verbose_name=u"回复")
    #一篇文章有多条评论（多对一关系）
    article = models.ForeignKey(Article, null=True, blank=True, verbose_name=u"文章")

    class Meta:
        ordering=['-create_date']
        verbose_name=u"评论"
        verbose_name_plural=u"评论列表"
