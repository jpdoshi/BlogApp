from django.shortcuts import render, HttpResponse, redirect
from .models import Blog, User

# Create your views here.


def index(request):
    if request.COOKIES.get('user') and request.COOKIES.get('user') != "":
        user = User.get_user_by_id(request.COOKIES['user'])
        context = {
            'user': User.get_user_by_id(request.COOKIES['user']),
            'blogs': Blog.get_blogs_by_user(user),
        }
        return render(request, "dashboard.html", context)
    else:
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
    return render(request, "login.html")


def login_auth(request):
    username = request.GET["username"]
    password = request.GET["password"]

    try:
        user = User.get_user_by_username(username)
    except:
        return HttpResponse("Incorrect Username")

    if user.password == password:
        response = redirect('index')
        response.set_cookie('user', user.id)

    else:
        response = HttpResponse("Incorrect Password")

    return response


def logout(request):
    response = redirect("index")

    response.set_cookie('user', "")
    return response


def create(request):
    return render(request, "create.html")


def post(request):
    try:
        title = request.POST['title']
        user = User.get_user_by_id(request.COOKIES.get('user'))
        cover = request.POST['cover']
        body = request.POST['body']

        blog = Blog(title=title, cover=cover, user=user, body=body)
        blog.save()
        
        return redirect('index')
    except:
        return HttpResponse("Error creating blog, try login again")
