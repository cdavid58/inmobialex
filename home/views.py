from operations.operations import Opertations
from django.http import HttpResponse
from django.shortcuts import render
from operations.operations import Reservations
from resident.models import Resident
import json

def Home(request):
	op = Opertations()
	with open('data/colombia.json', encoding="utf8") as file:
		data = json.load(file)
	return render(request,'index.html',{'city':data,'op':op.GetListPropertys(),'cat':op.GetSpace()})


def GetCountry(request):
	if request.is_ajax():
		with open('data/'+str(request.GET['country']).lower()+'.json', encoding="utf8") as file:
			data = json.load(file)
		return HttpResponse(json.dumps(data))

def Details_Property(request,pk):
	op = Opertations().GetDeatilProperty(pk)
	try:
		resident = Resident.objects.get(email = request.session['email_user'])
	except Exception as e:
		resident = None
	return render(request,'property/details.html',{'op':op,'photos':op['multimedia'],'inf_1':op['information'][0],'inf_2':op['information_extra'][0], 'resident':resident})

def Contact(request):
	return render(request,'contact.html')

def Create_Reservation(request):
	if request.is_ajax():
		print(request.GET['hour'])
		r = Reservations().CreateReservation(request.GET)
		return HttpResponse(r)