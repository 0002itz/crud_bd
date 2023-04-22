from django.contrib import admin
from .models import Project, Task, Question

#Register your models here.
admin.site.register(Question)
admin.site.register(Project)
admin.site.register(Task)
