from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=128)
    text_2 = models.CharField(max_length=2048, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="creation date")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="modification date")

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
