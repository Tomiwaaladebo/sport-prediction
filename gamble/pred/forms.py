from ast import Mod
from django.forms import ModelForm
from .models import Contactus
# Create your models here.

class ContactusForm(ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
