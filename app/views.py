from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import *
from .decorators import *
from random import *

# Create your views here.
@login_required(login_url = 'login')
def home(request):

	rand_user = Musician.objects.order_by('?')[:1]
	#don't forget to create a random model
	
	musician = Musician.objects.all()
	
	count = 0

	for i in range (len(musician)):
		if i == None:
			count +=1
	if count !=0:
		return redirect('profile')
	else:
	
		context = {'rand_user':rand_user, 'musician': musician}

		return render(request, 'app/home.html', context)

@unauthenticated_user
def loginUser(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)

		if user is not None:
			
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Ошибка ввода')


			
	return render(request, 'app/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def registration(request):

	form = CreateUserForm()

	if request.method == 'POST':
		
		form = CreateUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			
			group = Group.objects.get(name = 'Musician')
			user.groups.add(group)
			Musician.objects.create(
				user = user,
				email = user.email

			)
			
			messages.success(request, "Пользователь успешно создан")
			return redirect ('login')
	
	context = {'form': form}

	return render(request, 'app/registration.html', context)

@login_required(login_url = 'login')
def profile(request):

	musician = request.user.musician

	if request.method == 'POST':
		form = MusicianForm(request.POST, request.FILES, instance= musician)
		if form.is_valid():
			form.save()
			#form.cleaned_data()
	else:
		form = MusicianForm(instance= musician)
		
	context = {'form': form}

	return render(request, 'app/profile.html', context)