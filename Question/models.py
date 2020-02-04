from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.TextField(null=False, blank=False)


class MultipleChoiceQuestion(Question):
    pass


class Choice(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, related_name="choices", on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    ###position maybe
