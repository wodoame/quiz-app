from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser): 
    pass 


class Question(models.Model): 
    question_formats = (
        ('objectives', 'objectives'),
        ('essay', 'essay')
    )
    year = models.CharField(max_length=4)
    subject = models.CharField(max_length=25)
    question_format = models.CharField(choices=question_formats, max_length=128)
    instruction = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=25)
    number = models.PositiveIntegerField(null=True, blank=True)
    content = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.year + ' ' + self.subject + ' ' + self.question_format
    
class Objective(Question): 
    answers = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    option_a = models.CharField(max_length=128)
    option_b = models.CharField(max_length=128)
    option_c = models.CharField(max_length=128)
    option_d = models.CharField(max_length=128)
    answer = models.CharField(choices=answers, max_length=1)
    
    def getOptions(self): 
        return [self.option_a, self.option_b, self.option_c, self.option_d]
    
    def getDict(self): 
        return {
                'year': self.year,
                'subject':self.subject,
                'topic':self.topic,
                'number':self.number,
                'content':self.content,
                'format':self.question_format, 
                'options': self.getOptions(), 
                'answer': self.answer
                }