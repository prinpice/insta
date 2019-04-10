from django import forms
from .models import Post

# Post라는 모델을 조작할 수 있는 PostModelForm(또는 PostForm) 정의
class PostModelForm(forms.ModelForm):
    # 1. 어떤 input 필드를 가지는지
    content = forms.CharField(label="content", widget=forms.Textarea(attrs={
        'placeholder' : '오늘은 무엇을 하셨나요?'
    })) # content : column 명, "content" : label 명
    
    # 2. 해당 input 필드의 속성을 추가 & 어떤 모델을 조작할지
    class Meta:
        model = Post
        fields = ['content'] # 사용자가 직접 입력하는 필드만 폼에 추가
        # "__all__" : 가지고 있는 모든 column이 다 나옴