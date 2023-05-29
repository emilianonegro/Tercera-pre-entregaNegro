from django.db import models

# Create your models here.
class Post(models.Model):
 title = models.CharField(max_length=100)
 content = models.TextField()
 def __str__(self) -> str:
  return self.title
 
class Author(models.Model):
 name = models.CharField(max_length=100)
 age = models.IntegerField()
 
 def __str__(self) -> str:
  return self.name