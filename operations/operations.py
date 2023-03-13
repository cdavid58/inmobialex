import json, requests
from datetime import datetime

class Opertations:

	def GetListPropertys(self):
		try:
			url = "http://localhost:9090/api/GetLastProperty/"
			payload = json.dumps({})
			headers = {'Content-Type': 'application/json'}
			response = requests.request("POST", url, headers=headers, data=payload)
			return json.loads(response.text)
		except Exception as e:
			return {}
		

	def GetSpace(self):
		try:
			url = "http://localhost:9090/api/GetSpace/"
			payload={}
			headers = {}
			response = requests.request("POST", url, headers=headers, data=payload)
			return json.loads(response.text)
		except Exception as e:
			return {}

	def GetDeatilProperty(self,pk):
		url = "http://localhost:9090/api/Details_Property/"
		payload = json.dumps({"pk": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)



class Reservations:
	def CreateReservation(self,data):
		d1 = data['date'].split('-')
		url = "http://localhost:9090/api/Create_Reservation/"
		payload = json.dumps({
		  "date_enter": self.Fecha(str(d1[0]).strip()),
		  "date_exit": self.Fecha(str(d1[1]).strip()),
		  "user_email": data['client'],
		  "propertys": data['property'],
		  "pk_user": data['pk_user'],
		  "boys": 0,
		  "adult": data['persons'],
		  "price": data['price'],
		  "hour_input": data['hour'],
		  "note": data['note'],
		  'days':data['days'],
		  'clean':data['feed_clean']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)

		return json.loads(response.text)['result']

	def Fecha(self,strDate):
		objDate = datetime.strptime(strDate, '%m/%d/%Y')
		return str(objDate).split(' ')[0]

	def GetReservations(self,email):
		url = "http://localhost:9090/api/GetReservations/"
		payload = json.dumps({"email": email})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)
