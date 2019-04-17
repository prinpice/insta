from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    # 유저의 description을 하나만 가지도록 한다.
    # 하나만 사용할 수 있도록 관계맺고 싶을때
    # user = models.OneToOneField(가리키는 모델명, 옵션...)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)