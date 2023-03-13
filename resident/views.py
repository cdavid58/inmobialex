from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Resident, Social
from operations.operations import Reservations

def Access(request):
	return render(request,'login/access.html')

def Login(request):
	if request.is_ajax():
		data = request.GET
		result = False
		try:
			user = Resident.objects.get(email = data['email'], psswd = data['psswd'])
		except Resident.DoesNotExist as e:
			if "Resident matching query does not exist." in str(e):
				result = "Usuario o contraseña incorrecta"
			user = None
		if user is not None:
			request.session['pk_user'] = user.pk
			request.session['email_user'] = user.email
			request.session['phone'] = user.phone
			result = True
		return HttpResponse(result)


def Register(request):
	if request.is_ajax():
		result = False
		try:
			Resident(
				email = request.GET['email'],
				psswd = request.GET['psswd']
			).save()
			result = True
		except Exception as e:
			print(e)
			if "resident_resident.email" in str(e):
				result = "El email ya esta registrado"
		return HttpResponse(result)
		

def Profile(request):
	resident = Resident.objects.get(pk = request.session['pk_user'])
	if request.method == 'POST':
		data = request.POST
		print(data)
		try:
			resident.photo = request.FILES['photo_profile']
		except Exception as e:
			pass
		resident.name = data['name']
		resident.name_user = data['name_user']
		resident.phone = data['phone']
		resident.gender = data['sexo']
		resident.nationality = data['nationality']
		resident.address = data['address']
		resident.date_brithday = data['date_brithday']
		resident.save()	
	try:
		social = Social.objects.get(resident = resident)
	except Social.DoesNotExist:
		social = {}
	r = Reservations().GetReservations(request.session['email_user'])
	print(r)
	return render(request,'login/profile.html',{'resident':resident,'social':social,'reservation':r})


def LogOut(request):
	for i,j in list(request.session.items()):
		del request.session[i]
	return redirect('Home')