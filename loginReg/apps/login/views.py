from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
import bcrypt



def index(request):
	
	return render(request, 'login/index.html')

def registration(request):
	errors = User.objects.validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect(index) 

	hashed = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(5))

	User.objects.create(
		first_name = request.POST['first_name'],
		last_name = request.POST['last_name'],
		email = request.POST['email'],
		password = hashed,
		)

	return redirect(success)

def login(request):
	
	return redirect(success)

def success(request):

	return render(request, 'login/success.html')