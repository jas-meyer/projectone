from django.shortcuts import render, HttpResponse, redirect
import re
from models import User
from django.contrib import messages
def index(request):
	context = {
	"users" : User.objects.all()

	}
	print context

	return render(request, 'users/index.html', {"users" : User.objects.all()})
def new(request):
	return render(request, "users/new.html")
def show(request, id):
	 return render(request, 'users/show.html', {"user" : User.objects.get(id = id)})
def edit(request, id):
	return render(request, 'users/edit.html', {"user" : User.objects.get(id = id)})
def update(request,id):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/users/edit/'+id)
	else: 
		user = Blog.objects.get(id = id)
		user.first_name = request.POST['firstname']
		user.last_name = request.POST['lastname']
		user.email = request.POST['email']
		blog.save()
		return redirect('/users/edit/'+id)
def destroy(request, id):
	b = User.objects.get(id = id)
	b.delete()
	return redirect('/users')

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/users/new')
	firstname = str(request.POST['firstname'])
	lastname = str(request.POST['lastname'])
	email = str(request.POST['email'])
	User.objects.create(first_name = firstname, last_name = lastname, email = email) 
	return redirect('/users')
