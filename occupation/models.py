from django.db import models

# Create your models here.
class Occupation(models.Model):
    name = models.CharField(blank = False, null = False, max_length=200)
    picture_url = models.URLField(blank = False, null = False, default="https://leapmax.ai/wp-content/uploads/2024/06/Flexible-work-arrangements.webp")
    icon = models.CharField(blank = False, null = False, max_length = 100, default = "settings")

    def __str__(self):
        return self.name

class Speciality(models.Model):
    occupation = models.ForeignKey(to = Occupation, on_delete=models.CASCADE)
    name = models.CharField(blank = False, null = False, max_length=200)