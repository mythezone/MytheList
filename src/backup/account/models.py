from django.db import models
from utils.basemodel import BaseModel

# Create your models here.
class User(BaseModel):
    id = models.IntegerField(primary_key=True)
    username = models.CharField('用户名', max_length=30, null=True, blank=False, unique=True)
    password = models.CharField('密码', max_length=30, null=True, blank=False)
    email = models.EmailField('邮箱', max_length=30, null=True, blank=False, unique=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'  
        verbose_name_plural = '用户信息'
        
    def __str__(self) -> str:
        return self.username 