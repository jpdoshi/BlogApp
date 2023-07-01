from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name="index"),
	path('blogs/', views.blogs, name="blogs"),
	path('blog/<int:id>/', views.blog, name="blog"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('create/', views.create, name="create"),
	path('post', views.post, name="post"),
	path('login-auth/', views.login_auth, name="login-auth"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)