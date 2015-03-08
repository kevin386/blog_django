from django.contrib import admin
from models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'create_date','pub_date','excerpt','votes']

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

