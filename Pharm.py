import firebase_admin
import pyqrcode
import pandas as pd
from firebase_admin import credentials
from firebase_admin import db


def search(Pat_id):	
	p_id = []
	for i in dat:
		p_id.append(str(i))
#	print(p_id)
	flag = 0
	for i in p_id:
		if i == Pat_id:
			flag = 1 
	if flag == 1:
		return True
	else:
		return False	
	

def getResults(Pat_id):
	x=dat[Pat_id]
	for key,value in x.items():
		print(key,value)
		
#	print(dat[Pat_id])

cred = credentials.Certificate('smartpharmacy.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartpharmacy-dbdd2.firebaseio.com',
    'databaseAuthVariableOverride': None
})

ref = db.reference('Patients')
dat = ref.get()
Pat_id = raw_input("Enter Patients Id\n")
search_results = search(Pat_id)
if search_results == True:
	getResults(Pat_id)
	dr_pres = raw_input("Enter Prescription\n")
	my_ref = db.reference('Doctors').child('Doc1').child('Patients')
	my_ref.set({Pat_id : "prescription :" + dr_pres})
	
else :
	print("No Data Found in Database")
	dr_pres = raw_input("Enter Prescription\n")
	my_ref = db.reference('Doctors').child('Doc1').child('Patients')
	my_ref.set({Pat_id : "prescription :" + dr_pres})
	
YoN = raw_input("Press 'Y' to get QR\n")
if YoN == "Y" or YoN =="y" :
	img = pyqrcode.create("1,"+Pat_id +"," + dr_pres)
	print(img.terminal(quiet_zone=1))
	
	

