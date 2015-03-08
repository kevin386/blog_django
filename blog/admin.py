# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
# Register your models here.

def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()
upper_case_name.short_description = 'Name'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 在文章列表里面显示的字段，有3种方法：
    # 1、直接填写模型里面的字段；
    # 2、定义函数，参数为该模型实例，返回定制的文本，把函数名或字符串函数名放到这个列表，如upper_case_name
    # 3、使用模型里面定义的实例方法，填写字符串方法名
    list_display = ['title', 'category_disc', 'cat_sub_disc', 'digest_disc', 'tags_disc',
                    'create_date','pub_date', 'is_original_disc', 'reference','votes']
    # 按发布日期显示阶层的搜索标签
    date_hierarchy = 'pub_date'
    # 分类和子分类会在同一行显示
    # fields = ('title', ('category', 'cat_sub'), 'content', 'tags','reference')
    # 不指定fields可以定义fieldsets
    fieldsets = (
        (None, {
            'fields':('title', ('category', 'cat_sub'), 'digest','content', 'pub_date')
        }),
        (u'附加选项', {
            # 'classes':( 'wide', ),
            'classes':( 'collapse', ), # collapse收起fields里面字段
            'fields': ('tags','reference'),
            # 'description': u"附加选项"
        })
    )
    # 对ManyToManyField起作用，可以把选中项目在备选框中左右、上下移动
    filter_horizontal = ['tags']
    # filter_vertical = ['tags']
    # 自定义字段编辑控件
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CategorySub)
class CategorySubAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(ReferenceFrom)
class ReferenceFromAdmin(admin.ModelAdmin):
    pass

