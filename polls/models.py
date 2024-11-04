from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Models essentially is the database layout with additional metadata

"""
Create two models: Question and Choice
Question has two fields: question and a publication date
Choice has two fields: text of the choice and a vote tally
Each choice is associated with a question
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")
    #...
    def __str__(self):
        return self.question_text
   
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #...
    def __str__(self):
        return self.choice_text

#each model is represented by a class that subclasses django.db.models.Model
# Each model has a number of class variables, each of which represents a database field in the model.
# 