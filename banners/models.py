from django.db import models
from cities.models import City
from account.models import Profile
# Create your models here.
class Advertisement(models.Model):
    city = models.ForeignKey(to = City, on_delete=models.CASCADE)
    author = models.ForeignKey(to = Profile, on_delete=models.CASCADE)
    headline = models.CharField(max_length = 100, blank = False, null = False)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.headline

class Events(models.Model):
    date = models.DateField()
    orgainizer = models.ForeignKey(to = Profile, on_delete=models.CASCADE)
    headline = models.CharField(max_length = 100, blank = False, null = False)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.headline