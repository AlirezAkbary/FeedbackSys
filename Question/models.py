from django.db import models
# Create your models here.



class Question(models.Model):
    Question_Types = (
        ('M', 'MultipleChoice'),
        ('L', 'LongAnswer')
    )
    title = models.TextField(null=False, blank=False) ##Body of Question
    subject = models.TextField(null=False, blank=False, default="No Default") ## Question appeared in menu
    q_type = models.CharField(max_length=1, choices=Question_Types, default='M')



class MultipleChoiceQuestion(Question):
    pass

class LongAnswerQuestion(Question):
    pass


class Choice(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, related_name="choices", on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    count = models.IntegerField(null=False, blank=False, default=0)


class Answer(models.Model):
    question = models.ForeignKey(LongAnswerQuestion, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False, default="Your Answer")
    ###position maybe
