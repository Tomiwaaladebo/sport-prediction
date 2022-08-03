from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus', views.contactus, name='contactus'),
    path('experts/', views.profiles, name='profiles'),
    path('experts/<str:pk>/', views.profile, name='profile'),
    path('daily2odds/', views.dailyodds, name='daily2odds'),
    path('todaystips', views.allPredictions, name='allpredictions'),
    path('todaystips/<str:pk>', views.allPredictionsdays, name='allpredictionsdays'),
    path('topten', views.topten, name='topten'),
    path('topten/<str:pk>', views.toptendays, name='toptendays'),
    path('over', views.over, name='over'),
    path('over/<str:pk>', views.overdays, name='overdays'),
    path('tennis', views.tennis, name='tennis'),
    path('tennis/<str:pk>', views.tennisdays, name='tennisdays'),
    path('experts/prediction/<str:pk>/', views.experts, name='experts'),
    path('experts/prediction/<str:pk>', views.expertsdays, name='expertsdays'),
]
