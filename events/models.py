from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tags(models.Model):
	name = models.CharField(max_length=300)

	class Meta:
		verbose_name = 'name'
		verbose_name_plural = 'names'

	def __str__(self):
		return self.name

class Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	discription = models.TextField()
	futured = models.BooleanField(default=False)
	likes=models.ManyToManyField(User, related_name="q_loved", blank=True)
	# dislikes=models.ManyToManyField(User, related_name="q_disliked", blank=True)
	tags = models.ManyToManyField(Tags)
	date_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('webify:forum_details', args=[self.id])

	def num_likes(self):
		return self.likes.count()

	# def num_dislikes(self):
	# 	return self.dislikes.count()

class EvenComment(models.Model):
    question=models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment"
