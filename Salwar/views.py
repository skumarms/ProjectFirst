from django.shortcuts import render
from . models import Salwar

def salwar(request):
	jobs = Salwar.objects
	return render(request, 'salwar/salwar.html', {'jobs':jobs})
