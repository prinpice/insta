from django.urls import path
from . import views


app_name = "posts"


urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list") # list : 내장함수지만 동일 이름 써도 상관없음
]