from django.shortcuts import render
# import json to load json data to python dictionary
import json
import os
# urllib.request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
        api_key = os.environ.get('API_KEY')

        # source contain JSON data from API

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        source = urllib.request.urlopen(url).read()
        # converting JSON data to a dictionary
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
    else:
        data = {}
    return render(request, "weather_apps/index.html", data)