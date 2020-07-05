from django.db import models

# Create your models here.

class Novels(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    resume = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images')

class Chapters(models.Model):
    title = models.CharField(max_length=50)
    belong = models.CharField(max_length=10)
    chapter_url = models.CharField(max_length=100)
    chapter_num = models.CharField(max_length=5)

class TestModeln(models.Model):
    bookname = models.CharField(max_length=10)
    img = models.ImageField(upload_to='images')