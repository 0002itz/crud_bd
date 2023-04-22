from django.contrib import admin
from .models import Proyect, Task, Question

#Register your models here.

admin.site.register(Proyect)
admin.site.register(Task)
admin.site.register(Question)