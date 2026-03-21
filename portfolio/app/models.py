from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    tech=models.CharField(max_length=200)
    github_link=models.TextField(default=None)
    live_link=models.TextField(default=None)
    
    def __str__(self):
        return self.title
    
class Backend(models.Model):
    name=models.CharField(max_length=200)
    progress=models.IntegerField()
    def __str__(self):
        return self.name

class Frontend(models.Model):
    name=models.CharField(max_length=200)
    progress=models.IntegerField()
    def __str__(self):
        return self.name
    
class Tools(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
    