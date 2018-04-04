#Python script to send tracking numbers to firebase

from firebase import firebase
firebase = firebase.FirebaseApplication('https://parcelpal-sjsu.firebaseio.com/')

info = firebase.get('/users/001/tracking',None)
numoftrack = len(info)

print("Tracking numbers in database:")
for key,val in info.items():
   print (key,val)
print("Total tracking numbers:", numoftrack)
print("-------------------------------\n")

print ("Tracking start")
track = 0

while(1):
    track = input("Enter tracking number")
    if(track == "7121100001"):
        break
    numoftrack += 1
    trackno = 'track'+f'{numoftrack:02}'
    print(track, "will be entered as", trackno)
    firebase.patch('/users/001/tracking/', {trackno: track})


info = firebase.get('/users/001/tracking',None)

print("\nTracking numbers in database:")
for key,val in info.items():
   print (key,val)
print("")
print("exiting")
    
    
