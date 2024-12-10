from datetime import timezone

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    date_posted = models.DateTimeField(verbose_name="Gönderilme Tarihi")
    def __str__(self):
        return self.title