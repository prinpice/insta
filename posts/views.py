from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post
from django.views.decorators.http import require_POST

# Create your views here.
def create(request):
    if request.method == "POST":
        # 작성된 post(글)를 DB에 적용
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        
    else: # GET
        # post를 작성하는 form을 보여줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    
    return render(request, 'posts/list.html', {'posts': posts})
    
# @require_POST # Post로 보냈을 때만 허용해줌
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:list')
    
    
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'posts/update.html', {'form':form})
    
    