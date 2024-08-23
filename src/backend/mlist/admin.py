from django.contrib import admin
from .models import Tag, Category, Comment, MList, Image, Album
from ckeditor.widgets import CKEditorWidget
from django import forms

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class CommentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = '__all__'

class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['id', 'user', 'content', 'valid', 'reply', 'create_at', 'update_at']
    search_fields = ['content', 'user__username']
    list_filter = ['valid', 'reply', 'create_at', 'update_at']

class MListAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MList
        fields = '__all__'

class MListAdmin(admin.ModelAdmin):
    form = MListAdminForm
    list_display = ['id', 'title', 'subtitle', 'price', 'top', 'create_at', 'update_at']
    search_fields = ['title', 'subtitle']
    list_filter = ['top', 'create_at', 'update_at']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'url', 'thumb_url', 'user', 'size', 'album']
    search_fields = ['url', 'thumb_url', 'user__username']
    list_filter = ['size', 'album']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'user']
    search_fields = ['name', 'user__username']

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MList, MListAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)