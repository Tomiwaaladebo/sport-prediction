from email.policy import default
from django.shortcuts import render
from pred.models import Prediction
from .forms import ContactusForm
from datetime import date, timedelta


Experts = [
    {
    'id': '1',
    'name': 'Harrison',
    'bio': 'graduate of Unilag, Studied',
    'ig': '@harrion',
    'twitter': '@harrison',
    'image': "{% static 'images/profiles/profile.png' %}"
},
{
    'id': '2',
    'name': 'Olaolu',
    'bio': 'A soccer enthisiast, who has been into soccer prediction for 10years with incredible success rate',
    'ig': '@olaolu',
    'twitter': '@olaolu',
    'image': "{% static 'images/profiles/profile.png' %}"   
}]


Today = date.today()
Yesterday = Today + timedelta(-1)
Tomorrow = Today + timedelta(1)

def home(request):
    odds = 1
    bundle = Prediction.objects.filter(bundleRef='Bundle One').filter(date = Today)
    for tip in bundle:
       odds*=tip.odds
    context = {
        'bundle' : bundle,
        'odds' : round(odds,2)
    }
    return render(request, 'pred/bundle.html', context)


def dailyodds(request):
    dailyTwoodds = Prediction.objects.filter(dailyRef='Two Odds').filter(date = Today) #filtering by the different options in the database(drop down)
    dailyTwoodds2 = Prediction.objects.filter(dailyRef='Two Odds one').filter(date = Today)
    dailyTwoodds3 = Prediction.objects.filter(dailyRef='Two Odds two').filter(date = Today)
    odds = 1
    for tip in dailyTwoodds:
       odds*=tip.odds

    odds2 = 1
    for tip in dailyTwoodds2:
       odds2*=tip.odds

    odds3 = 1
    for tip in dailyTwoodds3:
       odds3*=tip.odds

    context = {
        'predict' : dailyTwoodds,
        'predict2' : dailyTwoodds2,
        'predict3' : dailyTwoodds3,
        'Today' : Today,
        'odds' : round(odds,2),
        'odds2' :round(odds2,2),
        'odds3' :round(odds3,2),
        }
    return render(request, 'pred/daily2odds.html', context)

def allPredictions(request):
    predictions = Prediction.objects.all().filter(date = Today)
    context={
        'predictions': predictions,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow,
        }
    return render(request, 'pred/todaystips.html', context)


def allPredictionsdays(request, pk):
    predictions1 = Prediction.objects.all()
    predict = None
    for i in predictions1:
        if i['date'] == pk:
            predict = i
    context = {
        'predict' : predict,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow
        }
    return render(request, 'pred/todaystipsdays.html', context)


def topten(request):
    top10 = Prediction.objects.filter(toptenRef='Top Ten').filter(date = Today)
    context={
        'predictions': top10,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow,
        }
    return render(request, 'pred/topten.html', context)

def toptendays(request, pk):
    top10 = Prediction.objects.filter(toptenRef='Top Ten')
    predict = None
    for i in top10:
        if i['date'] == pk:
            predict = i
    context = {
        'predict' : predict,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow
        }
    return render(request, 'pred/toptendays.html', context)


def over(request):
    over = Prediction.objects.filter(overOneRef='Over One').filter(date = Today)
    context = {
        'predictions' : over,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow,
    }
    return render(request, 'pred/over.html', context)

def overdays(request, pk):
    over = Prediction.objects.filter(overOneRef='Over One')
    predict = None
    for i in over:
        if i['date'] == pk:
            predict = i
    context = {
        'predict' : predict,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow
        }
    return render(request, 'pred/overdays.html', context)


def tennis(request):
    tennis = Prediction.objects.filter(tennisRef='Tennis').filter(date = Today)
    context = {
        'predictions' : tennis,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow,
    }
    return render(request, 'pred/tennis.html', context)

def tennisdays(request, pk):
    tennis = Prediction.objects.filter(tennisRef='Tennis')
    predict = None
    for i in tennis:
        if i['date'] == pk:
            predict = i
    context = {
        'predict' : predict,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow
        }
    return render(request, 'pred/tennisdays.html', context)


def contactus(request):
    form = ContactusForm()
    context = {
        'form': form
    }
    return render(request, 'pred/contactus.html', context)


def profiles(request):
    context={'experts': Experts}
    return render(request, 'pred/profiles.html', context)


def profile(request, pk):
    person = None
    for i in Experts:
        if i['id'] == pk:
            person = i
    return render(request, 'pred/single-profile.html', {'person':person})

def experts(request, pk):
    expert = Prediction.objects.filter(date = Today)
    Olexperttips = None
    global Experts
    for i in Experts:
        if i['name'] == pk:
            expert.filter(expertsRef='name')
            Olexperttips = i

    context = {
        'predictions' : Olexperttips,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow,
    }
    return render(request, 'pred/expert-predict.html', context)

    Experts = [
    {
    'id': '1',
    'name': 'Harrison',
    'bio': 'graduate of Unilag, Studied',
    'ig': '@harrion',
    'twitter': '@harrison',
    'image': "{% static 'images/profiles/profile.png' %}"
},
{
    'id': '2',
    'name': 'Olaolu',
    'bio': 'A soccer enthisiast, who has been into soccer prediction for 10years with incredible success rate',
    'ig': '@olaolu',
    'twitter': '@olaolu',
    'image': "{% static 'images/profiles/profile.png' %}"   
}]

def expertsdays(request, pk):
    expert = Prediction.objects.filter(expertsRef='Olaolu')
    expert2 = Prediction.objects.filter(expertsRef='Harrison')
    
    predict = None
    for i in expert:
        if i['date'] == pk:
            predict = i

    predict = None
    for i in expert2:
        if i['date'] == pk:
            predict = i
    
    context = {
        'predict' : predict,
        'Today' : Today,
        'Yesterday' : Yesterday,
        'Tomorrow' : Tomorrow
        }
    return render(request, 'pred/tennisdays.html', context)



 