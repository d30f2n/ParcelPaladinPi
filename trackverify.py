#Script to verify if tracking number is valid

#import firebase library and ParcelPaladin database
from firebase import firebase
firebase = firebase.FirebaseApplication('https://parcelpal-sjsu.firebaseio.com/')

#import user1 tracking data
info = firebase.get('/users/001/tracking',None)

#this is for debugging
numoftrack = len(info)
print("Tracking numbers in database:")
for key,val in info.items():
   print (key,val)
print("Total tracking numbers:", numoftrack)
print("-------------------------------\n")

#main program
print ("Tracking start")
track = 0

while(1):
    track = input("Enter tracking number")
    if(track == "7121100001"):
        break
    if track in info.values():
        print("Tracking number exists")
    else:
        print("Tracking number does not exist")

print("exiting")
