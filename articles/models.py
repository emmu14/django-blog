from django.db import models
from django.contrib.auth.models import User


class article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(upload_to='images/',null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'