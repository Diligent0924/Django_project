from urllib import request
from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length= 30)
    content = models.TextField()

class PersonalModel(models.Model):
    variety_1 = (
              ('Backjoon', 'Backjoon'),
              ('SWEA', 'SWEA'),
              ('Programmers', 'Programmers'),
    )
    
    username = models.CharField(max_length=30)
    variety = models.CharField(max_length=30, choices=variety_1)
    