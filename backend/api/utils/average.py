from calendar import week
import datetime

import requests 
import json
from django.conf import settings


def average_weather(lon, lat):

    h = datetime.datetime.now()
    hus = h - datetime.timedelta(days=5)

    week_ago = int(datetime.datetime.timestamp(hus))
    url = f'{settings.URL_API}onecall/timemachine?lat={lat}&lon={lon}&dt={week_ago}&appid={settings.API_KEY}'
    temp=[]
    r = requests.get(url)
    result=json.loads(r.text.encode('utf-8'))
    for avg in result['hourly']:
        temp.append(avg["temp"])
    average = sum(temp)/len(temp)
    return average
