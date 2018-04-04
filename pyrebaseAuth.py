import pyrebase

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
interpretedID  = identifier.split('%n')
print("What I interpreted: ")
print ("Email: " + interpretedID[0])
print ("Password: " + interpretedID[1])
print("\n")

user = auth.sign_in_with_email_and_password(interpretedID[0], interpretedID[1])

db = firebase.database()

#dataget = db.child("public").child("test").get(user['idToken']).val()
#print(dataget)

userInfo = auth.get_account_info(user['idToken'])
UID = userInfo['users'][0]['localId']

trackingNumbers = db.child("users").child(UID).child("trackingNumbers").get(user['idToken']).val()

while(1):
    track = input("Enter Tracking Number")
    if(track == "stop"):
        break
    if track in trackingNumbers.values():
        print("Tracking number exists")
    else:
        print("tracking number does not exist")

print("exiting")
