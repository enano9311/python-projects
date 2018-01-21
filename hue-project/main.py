import requests
import time
import random

base_url = "http://192.168.1.20/api/2hjqCuaz38r0sLWEb6QkZp95SVmsGarSFYiPCumU"

r = requests.get(base_url+"/lights/1")

print("got hue light info with GET!")
print r.status_code
print r.headers
print r.content

print("Pushing state using PUT!")

#hue_payload = '{"on" : true, "sat" : 100, "bri" : 254, "hue" : 15000}'
#r2 = requests.put(base_url + "/lights/1/state",data = hue_payload)
#print r2.content

def modify_light(base_url, status, color):
	hue_payload = '{"on" : ' + status + ', "sat" : 100, "bri" : 254, "hue" : ' + color + '}'
	r2 = requests.put(base_url + "/lights/1/state",data = hue_payload)

while True:
	time.sleep(random.uniform(.05,.2))
	state = random.choice(['false','true'])
	state = 'true'
	hu = str(random.randint(500,30000))
	modify_light(base_url,state,hu)
	print("light on? "+ state)
	print("color? " + hu)

