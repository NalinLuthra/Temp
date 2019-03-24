import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import time
import requests
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate('bmu-hackathon-firebase-adminsdk-ipov7-e3049ac49c.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bmu-hackathon.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
        'devices': 
            {
                'Laptop': {
                    'color': 'red',
                    'Status': 'OFF',
                    'power': 40,
                    #'length': 2
                },
                'Bulb': {
                    'color': 'green',
                    'Status': 'OFF',
                    'power': 100,
                    #'length': 3
                },
                'Hair-Dryer': {
                    'color': 'yellow',
                    'Status': 'OFF',
                    'power': 1000,
                    #'length': 1
                }
                # 'Unkown':{
                # 	'color' : 'Grey',
                # 	'status': 'OFF',
                # 	'power' : '0'
                # }
            }
        })

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)

cur = 0

while 1:
	try:
		current = ser.readline().strip()
		print(current)
		#current = float(current)
		a = ''
		for i in current:
			if i.isdigit():
				a = a + current
		#a = float(a)
		print(a)
		#current = [for i in current if i.isdigit()]
		#difference = current - cur
		difference = 100
		if(difference>0):
			if(difference>30 and difference<50):
				#Update Data Values
				ref = db.reference('devices')
				box_ref = ref.child('Laptop')
				box_ref.update({
				    'Status': 'ON'
				})
			if(difference>90 and difference<110):
				ref = db.reference('devices')
				box_ref = ref.child('Bulb')
				box_ref.update({
				    'Status': 'ON'
				})
			if(difference>90 and difference<100):
				ref = db.reference('devices')
				box_ref = ref.child('Hair-Dryer')
				box_ref.update({
				    'Status': 'ON'
				})
		if(difference<0):
			difference = difference*(-1)
			if(difference>30 and difference<50):
				#Update Data Values
				ref = db.reference('devices')
				box_ref = ref.child('Laptop')
				box_ref.update({
				    'Status': 'OFF'
				})
			if(difference>90 and difference<100):
				ref = db.reference('devices')
				box_ref = ref.child('Bulb')
				box_ref.update({
				    'Status': 'OFF'
				})
			if(difference>90 and difference<100):
				ref = db.reference('devices')
				box_ref = ref.child('Hair-Dryer')
				box_ref.update({
				    'Status': 'OFF'
				})
		cur = current
	except IOError:
		print('Error! Something went wrong.')
  #time.sleep(fixed_interval)


