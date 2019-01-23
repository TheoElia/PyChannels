from django.test import TestCase

# Create your tests here.

import urllib.request as req
import json

resp = req.urlopen("http://tellighapi.pythonanywhere.com/smsapi/Sms/?username=Theophy&api_key=faa66b4640ed7482fc21007016db22174fe6d26dd0a0af33d7761af49a5c")
data = resp.read()
data = data.decode("utf8")
jsondata = json.loads(data)
json_to_store = json.dumps(jsondata)
file = open("tellismsapi.json","w+")
file.write(json_to_store)
file.close()
f = open("tellismsapi.json","r+")
data = f.read()

jsondata = json.loads(data)
def send_msg(msg,recipient):
    print(msg, "has been sent to", recipient)

objects = jsondata['objects']
count = 0
for i in objects:
    object = objects[count]
    msg = object['body']
    recipients = object['recipients']
    print("Sending SMS to ",len(recipients)," number of people\n")
    for each_recipient in recipients:
        print("*" * 100,)
        send_msg(msg,each_recipient)
        print("*"*100,"\n")
    count+=1


