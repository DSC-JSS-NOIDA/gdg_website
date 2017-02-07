from django.shortcuts import render,get_object_or_404
from models import *
import datetime

# Create your views here.
def home(request):
	event=Event.objects.all()
	project=Project.objects.all()
	context={
	      "event":event,
	      "project":project,
	}

	return render(request,"home.html",context)


def event(request):
	
	now = datetime.datetime.now()

	ongoing = Event.objects.all().filter(date_from__lte=now, date_to__gte=now)
	upcoming = Event.objects.all().filter(date_from__gte=now)
	past = Event.objects.all().filter(date_to__lte=now)


	context={
          
           "queryset1":ongoing,
		   "queryset2":upcoming,
		   "queryset3":past,
          
    }


	return render(request,"event.html",context)

def event_detail(request,id=None):

	instance = get_object_or_404(Event,id=id)
	context={
          "instance":instance,
    }

	return render(request,"event_detail.html",context)





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


def project(request):
	queryset=Project.objects.all()
	context={
	      "queryset":queryset,
	}

	return render(request,"project.html",context)

