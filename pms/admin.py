from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Project)
admin.site.register(Module)
admin.site.register(ModuleRating)
admin.site.register(Comment)