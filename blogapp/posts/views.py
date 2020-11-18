from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world このページは投稿のインデックスです")

# Create your views here.
