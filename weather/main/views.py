from django.shortcuts import render 

import json 
# urllib.request to make a request to api 
import urllib.request 


def index(request):
	
	if request.method == 'POST': 
		city = request.POST['city'] 
		print(city)
		''' api key might be expired use your own api_key 
			place api_key in place of appid ="your_api_key_here " '''

		# source contain JSON data from API 

		source = urllib.request.urlopen(
		'http://api.openweathermap.org/data/2.5/weather?q='
		+ city + '&appid=a4abf770-0f39-11ee-8bb8-630c4f7ddbff').read()

		list_of_data = json.loads(source) 

		# data for variable list_of_data 
		data = { 
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + 'k', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		} 
		print(data)
		
	else: 
		data ={}
		
	return render(request, "main/index.html", data) 
