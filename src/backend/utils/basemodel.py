from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', editable=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间', editable=True)
    # ...
    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)