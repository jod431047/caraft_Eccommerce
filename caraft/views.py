from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.



class  CaraftList(generic.ListView):
    model  = Caraft
    


class CaraftDetail(generic.DetailView):
    model  = Caraft