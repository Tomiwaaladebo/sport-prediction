from django.db import models
from datetime import datetime
# Create your models here.


bundleRef = {
    ('Bundle One', 'Bundle One'),
    ('Bundle Two', 'Bundle Two'),
    ('Bundle Three', 'Bundle Three'),
    ('Bundle Four', 'Bundle Four'),
}

dailyRef = {
    ('Two Odds', 'Two Odds'),
    ('Two Odds one', 'Two Odds one'),
    ('Two Odds two', 'Two Odds two')
}

Tipsref = {
    ('Tip', 'Tip')
}

Toptenref = {
    ('Top Ten', 'Top Ten')
}

OverOneref = {
    ('Over One', 'Over One')
}

tennisref = {
    ('Tennis', 'Tennis')
}

expertref = {
    ('Olaolu', 'Olaolu'),
    ('Harrison', 'Harrison'),
}

 

class Prediction(models.Model):
    date = models.DateField()
    time = models.TimeField(null=False, blank=False)
    league = models.CharField(max_length=100)
    teamA = models.CharField(max_length=100)
    teamB = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    outcome = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    odds = models.FloatField(max_length=4)
    dailyRef = models.CharField(max_length=20, null=True, blank=True, choices=dailyRef)
    bundleRef = models.CharField(max_length=20, null=True, blank=True, choices=bundleRef)
    tipsRef = models.CharField(max_length=20, null=True, blank=True, choices=Tipsref)
    overOneRef = models.CharField(max_length=20, null=True, blank=True, choices=OverOneref)
    toptenRef = models.CharField(max_length=20, null=True, blank=True, choices=Toptenref)
    tennisRef = models.CharField(max_length=20, null=True, blank=True, choices=tennisref)
    expertsRef = models.CharField(max_length=50, null=True, blank=True,  choices=expertref)

    def __getitem__(self, date):
        return (date)

    def __getitem__(self, expertsRef):
        return (expertsRef)
 


class Contactus(models.Model):
    fullName = models.CharField(max_length=100)
    sendersEmail = models.EmailField()
    subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=3000)
    