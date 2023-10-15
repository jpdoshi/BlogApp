from django.db import models


class User(models.Model):
	id    = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	email = models.EmailField()
	about = models.TextField()
	password = models.CharField(max_length=16)
	liked_blogs = models.CharField(max_length=100)

	def get_user_by_id(_id):
		user = User.objects.get(id=_id)
		return user

	def get_liked_blogs(_liked_blogs):
		if _liked_blogs != "":
			if _liked_blogs[0] == ',':
				_liked_blogs = _liked_blogs[1:]
			lb = _liked_blogs.split(',')
			blogs = Blog.objects.filter(id__in=lb).order_by('title')
			return blogs
		else:
			return None

	def get_user_by_username(_username):
		user = User.objects.get(username=_username)
		return user

	def __str__(self):
		return f"{self.fname} {self.lname}"


class Blog(models.Model):
	id    = models.AutoField(primary_key=True)
	user  = models.ForeignKey(User, on_delete=models.CASCADE)
	cover = models.ImageField(upload_to="uploads/")
	title = models.CharField(max_length=50)
	pub_date = models.DateField(auto_now=True)
	body  = models.TextField()
	likes = models.IntegerField(default=0)

	def get_blog_by_id(_id):
		blog = Blog.objects.get(id=_id)
		return blog

	def get_blogs_by_user(_user):
		blogs = Blog.objects.filter(user=_user)
		return blogs

	def get_latest_blogs():
		return Blog.objects.order_by('-pub_date')[:12]

	def __str__(self):
		return f"{self.title} - {self.user}"
