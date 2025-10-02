from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(blank = False, null = False, max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(to = State, on_delete=models.SET_NULL, null = True)
    name = models.CharField(blank = False, null = False, max_length=200)
    picture_url = models.URLField(blank = False, null = False, default = 'https://google.com')

    def __str__(self):
        return self.name
