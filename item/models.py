from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Events(models.Model):
    # 
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Galleries'
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self): 
        return self.title
    


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'Comment by {self.author.username} on {self.post.title}'



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    


class Stats(models.Model):
    trees_planted = models.CharField(max_length=255, blank=True, null=True)
    high_schools = models.CharField(max_length=255, blank=True, null=True)
    primary_schools = models.CharField(max_length=255, blank=True, null=True)



class Issues(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class NewsUpdates(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateField(null=True)
    description = models.TextField()
    pics = models.ImageField(upload_to='news_images/', blank=True, null=True)



class Feedback(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pics = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    


    

