from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('blogs/', views.blogs, name="blogs"),
	path('blog/<int:id>/', views.blog, name="blog"),
	path('login/', views.login, name="login"),
	path('create/', views.create, name="create"),
]