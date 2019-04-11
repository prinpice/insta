from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True) # 업로드 된 파일이 들어오면 1. 특정위치에 넣고, 2. 주소값을 저장한다.
    
    def __str__(self):
        return self.content
        