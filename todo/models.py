from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    list = models.ForeignKey('List', on_delete=models.CASCADE, related_name='items')

class List(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='lists')
    # is_template = models.BooleanField(default=False)

class User(models.Model):
    name = models.CharField(max_length=50)
