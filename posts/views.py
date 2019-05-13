from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def create(request):
    if request.method == "POST":
        # 작성된 post(글)를 DB에 적용
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:list')
        
    else: # GET
        # post를 작성하는 form을 보여줌
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})
        
@login_required
def list(request):
    # # 모든 Post를 보여줌
    # posts = Post.objects.all()
    
    
    # # 1. 내가 팔로우 한 사람들의 Post만 보여줌
    # posts = Post.objects.filter(user_id__in=request.user.followings.all())
    
    # # 2. (1) + 내가 작성한 Post도 보여줌
    # my_posts = request.user.post_set.all() # related_name을 하지 않아서 post_set 사용
    # posts.extends(my_posts) # Query 2개 작동
    # # list(posts) += list(my_posts) # list를 사용하여 query하나만 사용가능 but 여기서 함수이름과 동일하여 작동하지 않음
    
    # print(posts.query) # posts에 들어간 Query 보기
    
    posts = Post.objects.filter(Q(user_id__in=request.user.followings.all()) | Q(user_id=request.user))
    
    # Comment를 작성하는 form을 보여줌
    
    comment_form = CommentModelForm()
    
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form' : comment_form})
    
# @require_POST # Post로 보냈을 때만 허용해줌
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')
    
    
def update(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'posts/update.html', {'form':form})
    
@login_required # login을 했을때 사용가능하도록 지정
def like(request, post_id):
    # like를 추가할 post를 가져옴
    post = get_object_or_404(Post, id=post_id)
    # post = Post.objects.get(id=post_id)
    
    # 2. 만약 유저가 해당 post를 이미 like 했다면,
    #       like를 제거하고,
    #   아니면,
    #       like를 추가한다.
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')
    

# 먼저 불리는 것을 위에 작성함
@login_required # 로그인 안한 경우 로그인 창으로 넘어감
@require_POST
def comment_create(request, post_id):
    # Comment를 만드는 로직
    # !! post = get_object_or_404(Post, pk=post_id) # 이런 방식으로 저장도 가능하지만 가능한 (직접적인 방식은) 사용하지 않는다
    form = CommentModelForm(request.POST) # 요청방식(GET/POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        # !! comment.post = post 
        comment.save()
    return redirect('posts:list')
    
@login_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user != request.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')