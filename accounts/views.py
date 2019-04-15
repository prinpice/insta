from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    
    
    
    if request.method == 'POST':
        # POST : 실제 로그인(세션에 유저 정보 추가)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next= 정의 되어 있으면, 해당하는 url로 리다이렉트
            # 정의되어 있지 않다면, posts:list로 리다이렉트
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        # GET : 로그인 정보 입력
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})
        
        
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    