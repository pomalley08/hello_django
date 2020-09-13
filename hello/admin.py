from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.LogMessage)

print('http://127.0.0.1:8000/admin')