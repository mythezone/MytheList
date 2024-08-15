from django.contrib import admin
from account.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    
    list_filter = ['username','email']
    
    search_fields = ['username','email']
    
admin.site.register(User, UserAdmin)
