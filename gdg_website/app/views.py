from django.shortcuts import render,get_object_or_404
from models import *
import datetime
from django.http import *

# Create your views here.
def home(request):
	now = datetime.datetime.now()
	event=Event.objects.all().filter(date_from__gte=now)[:4]	

	context={
	      "event":event,
	      
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
	comments = Comment.objects.all().filter(event_ID=id)
	context={
          "instance":instance,
          "comments":comments,
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



def subscribe(request):
	email=request.POST['email_ID']
	query=Subscriber(email_ID=email) 
	query.save()
	
	return HttpResponse("You have been subscribed")


def comment(request):
	id = request.POST['id']
	query = get_object_or_404(Event,id=id)
	now=datetime.datetime.now()
	name=request.POST['name']
	email=request.POST['email_ID']
	comment=request.POST['comment']
	query=Comment(event_ID=query,name=name,email_ID=email,date=now,comment=comment) 
	query.save()
	
	return HttpResponse("Success")


def reply(request):
	id = request.POST['id']
	query = get_object_or_404(Comment,id=id)
	now=datetime.datetime.now()
	name=request.POST['name']
	email=request.POST['email_ID']
	reply=request.POST['reply']
	query=Reply(comment_ID=query,name=name,email_ID=email,date=now,reply=reply) 
	query.save()

	return HttpResponse("Success")
	








