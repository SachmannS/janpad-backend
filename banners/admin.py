from django.contrib import admin
from .models import Events, Advertisement
# Register your models here.

admin.site.register([Events, Advertisement])