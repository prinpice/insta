from django.db import models
# from django.contrib.auth.models import User # django안에 저장되어 있는 곳을 찾아가서 보는 방법
from django.conf import settings
# conf에는 보이지 않는 많은 setting을 가지고 있다.

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True) # 업로드 된 파일이 들어오면 1. 특정위치에 넣고, 2. 주소값을 저장한다.
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # 이전코드(직접적)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 1:N
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    def __str__(self):
        return self.content
        
        
class Comment(models.Model):
    content = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content