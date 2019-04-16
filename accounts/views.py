from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash

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
    
def signup(request):
    if request.method == "POST":
        # POST : 유저 등록
        form = UserCreationForm(request.POST) # request.POST는 dictionary로 되어있다.
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # request.POST 사용해도 됨
            return redirect('posts:list')
    else:
        # GET : 유저 정보 입력
        form = UserCreationForm()
        
    return render(request, 'accounts/signup.html', { 'form' : form })
    
def people(request, username):
    # 사용자에 대한 정보
    people = get_object_or_404(get_user_model(), username=username)
    # 1. settings.AUTH_USER_MODEL(django.conf) => settings.py에 AUTH_USER_MODEL= 작성해줘야 함
    # 2. get_user_model() # 가장 많이 사용함
    # 3. User (django.contrib.auth.models) # 사용 안함
    return render(request, 'accounts/people.html', {'people' : people})
    
# 회원 정보 변경(편집 & 반영)
def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('people', user.username) # people의 url에는 username을 보내어 줘야 하기 때문에 추가한다.
    else:
        user_change_form = CustomUserChangeForm(instance=request.user) # 현재 로그인 된 유저 # instance라는 키워드 인자에 넣어주기 
        context = {
            'user_change_form' : user_change_form,
        }
        return render(request, 'accounts/update.html', context)
        
# 회원 탈퇴(안만드는 것이 좋음, 만드는 경우에는 꼭꼭 숨겨놔야 함)
def delete(request):
    if request.method == "POST":
        # 현재 접속해 있는 유저를 지운다.
        request.user.delete()  
        return redirect('posts:list')
    
    return render(request, 'accounts/delete.html')
    
# 비밀번호변경
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username)
    else:
        # 첫 번째 객체를 request로 받고 있어서 key없이 작성
        password_change_form = PasswordChangeForm(request.user)
        context = {
            'password_change_form' : password_change_form,
            
        }
        return render(request, 'accounts/password.html', context)