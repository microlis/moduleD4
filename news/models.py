from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Author(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rating_author = models.IntegerField(default = 0)
	
	def update_rating(self):
		value_post = Author.objects.filter(Post__rating_post) # Каждой статьи автора
		value_post = value_post*3
		value_auth = Author.objects.filter(Comment__rating_comment) #всех комментариев автора
		value_comment = Author.objects.filter(Post__rating_post, Comment__rating_comment) #всех комментариев к статьям автора
		value = value_post + value_auth + value_comment
		
		self.rating_author = value
		self.save()
		
		
	
class Category(models.Model):
	categ = models.CharField(max_length=255, unique = True)
	
class Post(models.Model):
	time_in_post = models.DateTimeField(auto_now_add = True)
	
	news = 'NEW'
	article = 'ARICLE'
	POSITIONS = [(article, 'Статья'),(news, 'Новость')]
	
	type_post = models.CharField(max_length = 20, choices = POSITIONS, default = news)
	
	
	
	head_post = models.CharField(max_length = 255) #заголовок
	text_post = models.TextField(default = "Пусто")
	rating_post = models.IntegerField(default = 0)
	
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	category = models.ManyToManyField(Category, through = 'PostCategory')
	
	def preview(self):
		prew = self.text_post[:124]
		prew = prew+'...'
		return prew
	
	def like(self):
		self.rating_post +=1
		self.save()
		
	
	def dislike(self):
		self.rating_post -=1
		if (self.rating_post <0):
			self.rating_post = 0
		self.save()
		
	def get_absolute_url(self):
		return f'/posts/{self.id}'
	
class PostCategory(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)   
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	
	text_comment = models.TextField(default = "")
	time_in_comment = models.DateTimeField(auto_now_add = True)
	rating_comment = models.IntegerField(default = 0)
	
	def like(self):
		self.rating_comment +=1
		self.save()
		
	
	def dislike(self):
		self.rating_comment -=1
		if (self.rating_comment <0):
			self.rating_comment = 0
		self.save()
