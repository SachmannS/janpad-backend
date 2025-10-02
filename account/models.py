from django.db import models
from django.contrib.auth.models import User
from cities.models import City
from occupation.models import Occupation, Speciality

# Create your models here.
def profile_upload_path(instance, filename):
    return f"profile_pictures/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.ForeignKey(to = User, blank = False, null = False, on_delete=models.CASCADE)
    city = models.ForeignKey(to = City, blank = False, null = False, on_delete=models.CASCADE)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)

class ProfileOccupation(models.Model):
    profile = models.ForeignKey(to = Profile, blank = False, null = False, on_delete=models.CASCADE)
    occupation = models.ForeignKey(to = Occupation, blank = False, null = False, on_delete=models.CASCADE)
    speciality = models.ForeignKey(to = Speciality, blank = True, null = True, on_delete=models.CASCADE)

class Review(models.Model):
    profile = models.ForeignKey(to = Profile, blank = False, null = False, on_delete=models.CASCADE)
    review_by = models.ForeignKey(to = User, blank = False, null = False, on_delete=models.CASCADE)
    rating = models.IntegerField(blank = False, null = False)
    review = models.TextField(blank = True, null = True)
    created = models.DateField(auto_now_add=True)

class Preference(models.Model):
    preference = models.IntegerField()
    profile = models.ForeignKey(to = Profile, blank = False, null = False, on_delete=models.CASCADE)
    review = models.ForeignKey(to = Review, blank = False, null = False, on_delete=models.CASCADE)

class SocialMedia(models.Model):
    user = models.ForeignKey(to = User, blank = False, null = False, on_delete=models.CASCADE)
    instagram = models.CharField(max_length = 500, blank = True)
    x = models.CharField(max_length = 500, blank = True)
    phone_number = models.CharField(max_length=20, blank = False)
    facebook = models.CharField(max_length = 500, blank = True)
    threads = models.CharField(max_length = 500, blank = True)
    linkedIn = models.CharField(max_length = 500, blank = True)