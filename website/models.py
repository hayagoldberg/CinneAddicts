from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie (models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    director = models.CharField(max_length=20)
    main_actors = models.CharField(max_length=100)
    release_year = models.IntegerField(default=0)
    flyer = models.ImageField(blank=True, default='default.jpg')
    image = models.ImageField(blank=True, default='default.jpg')


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.movie.title}"
