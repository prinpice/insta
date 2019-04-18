from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', ] # 수정할 내용

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 동일할 경우 아래내용 안써줘도 됨
        # fields = UserCreationForm.Meta.fields
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname', 'image', ]
        
