from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Codedata(models.Model):
    Code = models.CharField(max_length=3, null=True)
    Issure = models.CharField(max_length=3 , null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Code

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline