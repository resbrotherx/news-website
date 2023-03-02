from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tags(models.Model):
	name = models.CharField(max_length=300)

	class Meta:
		verbose_name = 'tag'
		verbose_name_plural = 'tags'

	def __str__(self):
		return self.name

class New(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	image = models.ImageField(default=False)
	little_discription = models.TextField(default=False)
	discription = models.TextField()
	futured = models.BooleanField(default=False)
	one = models.BooleanField(default=False)
	popular = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	likes=models.ManyToManyField(User, related_name="love", blank=True)
	# dislikes=models.ManyToManyField(User, related_name="q_disliked", blank=True)
	tags = models.ManyToManyField(Tags)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news_detail', kwargs={
			'id': self.id
		})
	def get_absolute_url(self):
		return reverse('new:forum_details', args=[self.id])

	def num_likes(self):
		return self.likes.count()

	# def num_dislikes(self):
	# 	return self.dislikes.count()

class NewsComment(models.Model):
	question=models.ForeignKey(New, related_name="comments", on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	comment=models.TextField()
	date_updated = models.DateTimeField(auto_now=True)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} comment"


class Email(models.Model):
	emais = models.EmailField()


	def __str__(self):
		return self.emais
