from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', ] # 수정할 내용
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname', ]