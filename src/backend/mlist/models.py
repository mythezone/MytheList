from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from ckeditor.fields import RichTextField

User = get_user_model()

class CustomS3Boto3Storage(S3Boto3Storage):
    location = 'media'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mlist = models.ManyToManyField('MList', related_name='tags')
    
    def __str__(self):
        return self.name
        

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mlist = models.ForeignKey('MList', related_name='categories', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    pid = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    content = models.TextField()
    # poster = models.ImageField(storage=CustomS3Boto3Storage(), upload_to='comments/', null=True, blank=True)
    poster = models.ImageField(upload_to='uploader/mlist/', null=True, blank=True)
    valid = models.BooleanField(default=True)
    reply = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True, blank=True)
    like = models.ManyToManyField(User, related_name='liked_comments')
    
    def __str__(self):
        return str(self.id)

class MList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pid = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    # poster = models.ImageField(storage=CustomS3Boto3Storage(), upload_to='mlist/', null=True, blank=True)
    poster = models.ImageField(upload_to='uploader/mlist/', null=True, blank=True)
    desc = RichTextField()
    comment = models.OneToOneField(Comment, null=True, blank=True, related_name='mlist', on_delete=models.SET_NULL)
    like = models.ManyToManyField(User, related_name='liked_mlists')
    owner = models.ForeignKey(User, null=True, blank=True, related_name='owned_mlists', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    complete = models.ManyToManyField(User, related_name='completed_mlists')
    top = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='mlists', on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    thumb_url = models.URLField()
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    album = models.ForeignKey('Album', related_name='images', on_delete=models.CASCADE)

class Album(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name