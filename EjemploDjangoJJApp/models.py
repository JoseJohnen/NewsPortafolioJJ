from django.db import models

# Create your models here.
# class Member(models.Model):
    # fname = models.CharField(max_length=50)
    # lname = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200, unique=True) # This is for having an example of unique
    # passwd = models.CharField(max_length=50)
    # age = models.IntegerField()

    # def __str__(self):
    #    return self.fname + " " + self.lname

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date = models.DateField()


    def __str__(self):
       return "<b>" + self.title + "</b><br/>" + self.content + "<br/>" + self.date