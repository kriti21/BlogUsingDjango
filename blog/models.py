from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

#class Category(models.Model):
#    name = models.CharField(max_length = 500)

#    def __str__(self):
#        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 500)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length = 250)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + '--' + ((str)(self.published_date)) + '--' + self.author + '--' #also print Category

    def publish(self):
        self.published_date = timezone.now()
        self.save()
