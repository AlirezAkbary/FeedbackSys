from django.db import models

# Create your models here.



class Question(models.Model):
    Question_Types = (
        ('M', 'MultipleChoice'),
        ('L', 'LongAnswer'),
        ('D', 'Default')
    )
    title = models.TextField(null=False, blank=False)
    q_type = models.CharField(max_length=1, choices=Question_Types, default='M')



class MultipleChoiceQuestion(Question):
    pass

class LongAnswerQuestion(Question):
    pass


class Choice(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, related_name="choices", on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    ###position maybe
