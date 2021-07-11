from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request, 'pswd_app/home.html')

def about(request):
	return render(request, 'pswd_app/about.html')	

def password(request):

	the_password='testing'

	characters=list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		characters.extend(list('@#$%^&*!'))
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))		

	length=int(request.GET.get('length',2))

	the_password=''
	for x in range(length):
		the_password+=random.choice(characters)

	return render(request, 'pswd_app/password.html' ,{'password':the_password})
