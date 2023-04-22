from django.db import models

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task (models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyect = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '--' + self.proyect.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)