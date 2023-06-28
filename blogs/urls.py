from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('blogs/', views.blogs, name="blogs"),
	path('blog/<int:id>/', views.blog, name="blog"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('create/', views.create, name="create"),
	path('login-auth/', views.login_auth, name="login-auth"),
]