from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("hello world このページは投稿のインデックスです")
    # {'テンプレ内での変数名':渡す変数名}

    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request,post_id):
    return render(request, 'posts/post_detail.html',{'post_id':post_id})
# Create your views here.
