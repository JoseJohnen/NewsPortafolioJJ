from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
       return "<b>" + self.title + "</b><br/>" + self.content + "<br/>" + self.date