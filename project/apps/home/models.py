from django.db import models

# Create your models here.
class Recipe(models.Model):
 title = models.CharField(max_length=100)
 content = models.TextField()
 def __str__(self) -> str:
  return self.title
 
class Chef(models.Model):
 name = models.CharField(max_length=100)
 age = models.IntegerField()
 
 def __str__(self) -> str:
  return self.name