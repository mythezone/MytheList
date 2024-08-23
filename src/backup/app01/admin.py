from django.contrib import admin
from app01.models import Article


def get_author(obj):
    return obj.user.username
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id',get_author, 'title', 'content', 'create_at', 'update_at']
    # list_display_links = ['id','title','content']
    list_filter = ['title','content']
    
    list_editable = ['title','content']
    

    search_fields = ['title','content']
    
    readonly_fields = ['create_at', 'update_at']
    

get_author.short_description = '作者'
    
admin.site.register(Article, ArticleAdmin)