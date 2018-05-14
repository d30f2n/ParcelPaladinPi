from threading import Thread
from time import sleep
import pyrebase

trackingNumbers = 0

def loginAndUpdate():
    global trackingNumbers
    config = {
    "apiKey": "AIzaSyCdu3P-I2ifCb-aTqEuzyn4g313nvkrUHA",
    "authDomain": "parcelpal-sjsu.firebaseapp.com",
    "databaseURL": "https://parcelpal-sjsu.firebaseio.com/",
    "storageBucket": "http://parcelpal-sjsu.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)

    auth = firebase.auth()

    identifier = input("Scan your identifier\n")
    print("what you scanned: " + identifier + "\n")
    interpretedID  = identifier.split(',')
    print("What I interpreted: ")
    print ("Email: " + interpretedID[0])
    print ("Password: " + interpretedID[1])
    print("\n")

    user = auth.sign_in_with_email_and_password(interpretedID[0], interpretedID[1])
    
    userInfo = auth.get_account_info(user['idToken'])
    UID = userInfo['users'][0]['localId']
    startscan = Thread(target = scanAndCheck)
    startscan.start()
    while(1):
        trackingNumbers = db.child("users").child(UID).child("trackingNumbers").get(user['idToken']).val()
        sleep(5)

def scanAndCheck():
    global trackingNumbers
    db = firebase.database()
    while(1):
        track = input("Enter Tracking Number")
        if(track == "stop"):
            break
        trackingNumbers = db.child("users").child(UID).child("trackingNumbers").get(user['idToken']).val()
        if track in trackingNumbers.values():
            print("Tracking number exists")
            sleep(3)
            
        else:
            print("tracking number does not exist")
            sleep(3)
        

if __name__ == "__main__":
    thread = Thread(target = loginAndUpdate)
    thread.start()
    thread.join()
    print ("thread finished...exiting")
