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

class Osoba(models.Model):
    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Osoby"

    class Dates(models.IntegerChoices):
        JANUARY = 1
        FEBRUARY = 2
        MARCH = 3
        APRIL = 4
        MAY = 5
        JUNE = 6
        JULY = 7
        AUGUST = 8
        SEPTEMBER = 9
        OCTOBER = 10
        NOVEMBER = 11
        DECEMBER = 12

    imie = models.CharField(max_length=64, blank=False)
    nazwisko = models.CharField(max_length=64, blank=False)
    miesiac_urodzenia = models.IntegerField(choices=Dates.choices, default=Dates.JANUARY)
    data_dodania = models.DateTimeField(auto_now_add=True)
    druzyna = models.ForeignKey(
        'Druzyna',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Druzyna(models.Model):
    class Meta:
        verbose_name_plural = "Druzyny"
    nazwa = models.TextField(max_length=64, blank=False)
    kraj = models.TextField(max_length=2, blank=False)

    def __str__(self):
        return self.nazwa + ' (' + self.kraj + ')'