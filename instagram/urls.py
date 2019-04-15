"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from . import settings # django스럽지 않은 코딩
from django.conf import settings # 다른 요약된 클래스의 객체 등을 통해 접근한다. # 관리할 때 직접적으로 접근할 경우 파일변경이 생길 수 도 있음(=> 하나씩 다 수정해야함) # 데이터 은닉 관점
# django.conf : 모든 환경설정 접근가능 # 파일에 직접들어가지 않고 접근하는 함수, 객체, 방법을 만들어 파일을 직접 조작하지 못하게 한다.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'posts/', include('posts.urls')),
    path( 'accounts/', include('accounts.urls')),
]
# urls.py는 whitelisting으로 직집 추가하지 않으면 동작하지 않음
# urlpatterns += staic(통과시키고자 하는 url, 실제 저장 장소)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # keyword를 적어주어 어디로 찾아가는지 알려준다.