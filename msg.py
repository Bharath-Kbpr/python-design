import requests
import json

def send_sms(number,message):
    url ='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':'Uwj9BRgtOQfNVxXCec0apMym2T31n8AJhGkdZIF7Ks5LSib6l4Ej1Hh3gwDbrUcBioTuAXMOqd5WRNxS',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number
    }

    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)


send_sms("_your number__","message")

