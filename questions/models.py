from django.db import models
from django.contrib.auth.models import User
from spenglr.education.models import Module


# Question and resource models store information for testing/studying purposes
class Resource(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # How to handle ISBN references and URIs? May need own handler e.g. URIField
    link = models.URLField(verify_exists=True)

class Question(models.Model):
    def __unicode__(self):
        return self.content
    def answers_shuffled(self):
        return self.answer_set.order_by('?')
    content = models.TextField()
    resource = models.ManyToManyField(Resource, blank=True) # Multiple resource records for this Question, resources assigned to >1 question
    modules = models.ManyToManyField(Module, blank=True)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField()


    






