from django.shortcuts import render,get_object_or_404
from models import *

# Create your views here.
def home(request):


	return render(request,"home.html")


def team(request):
	Past = Team.objects.all().filter(status="Past")
	Current = Team.objects.all().filter(status="Current")
	Mentor = Team.objects.all().filter(status="Mentor")

	context={
           "Past":Past,
           "Current":Current,
           "Mentor":Mentor,

	}

	return render(request,"team.html",context)

