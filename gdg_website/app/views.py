from django.shortcuts import render,get_object_or_404
from models import *

# Create your views here.
def home(request):


	return render(request,'home.html')


def team(request,id=None):

	instance = get_object_or_404(Team,id=id)
	context={
          "instance":instance,
    }

	return render(request,"team.html",context)