from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def index(request):
	return render(request, "home.html")

def blogs(request):
	context = {
		'blogs': Blog.get_latest_blogs(),
	}
	return render(request, "blogs.html", context)

def blog(request, id):
	context = {
		'blog': Blog.get_blog_by_id(id),
	}
	return render(request, "blog.html", context)

def login(request):
	return HttpResponse("Login Page")

def create(request):
	return HttpResponse("Create Blog")