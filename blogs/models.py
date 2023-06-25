from django.db import models

class User(models.Model):
	id    = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=16)

	def get_user_by_id(_id):
		user = User.objects.get(id=_id)
		return user

	def __str__(self):
		return f"{self.fname} {self.lname}"

class Blog(models.Model):
	id    = models.AutoField(primary_key=True)
	user  = models.ForeignKey(User, on_delete=models.CASCADE)
	cover = models.ImageField(upload_to="uploads/")
	title = models.CharField(max_length=50)
	body  = models.TextField()

	def get_blog_by_id(_id):
		blog = Blog.objects.get(id=_id)
		return blog

	def get_all_blogs():
		return Blog.objects.all()

	def __str__(self):
		return f"{self.title} - {self.user}"
