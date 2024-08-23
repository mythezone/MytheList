from django.db import models
from utils.basemodel import BaseModel
from account.models import User

# Create your models here.
class Article(BaseModel):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField('标题', max_length=100, null=True, blank=False)
    content = models.TextField('内容', null=True, blank=False)
    publish_date = models.DateTimeField('发布时间', auto_now_add=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'article'
        verbose_name = '文章'   
        verbose_name_plural = '文章'
        ordering = ['-publish_date']
        
    def __str__(self) -> str:
        return self.title
        
        