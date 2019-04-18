from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    # 유저의 description을 하나만 가지도록 한다.
    # 하나만 사용할 수 있도록 관계맺고 싶을때
    # user = models.OneToOneField(가리키는 모델명, 옵션...)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    
# User모델을 건드리는 느낌(실제로 건드리지는 않음)
class User(AbstractUser): # 이름이 동일해도 루트가 다르기때문에 가능
    follows = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings") # 특정 객체(나)를 팔로우 하고있는 유저들
    