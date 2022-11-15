from django.db import models

class Gun(models.Model):
    Gun_name = models.CharField(max_length=200)
    is_legal = models.BooleanField('Is legal?')
    amount = models.IntegerField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    manufacturer = models.ForeignKey(Gun, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text