import pyrebase
from time import sleep
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

import Adafruit_CharLCD as LCD
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 26

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight, 0, 1)


GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial = GPIO.LOW)

config = {
    "apiKey": "AIzaSyCdu3P-I2ifCb-aTqEuzyn4g313nvkrUHA",
    "authDomain": "parcelpal-sjsu.firebaseapp.com",
    "databaseURL": "https://parcelpal-sjsu.firebaseio.com/",
    "storageBucket": "http://parcelpal-sjsu.appspot.com",
    }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

lcd.message('Scan your\nidentifier')
identifier = input("Scan your identifier\n")
lcd.clear()
print("what you scanned: " + identifier + "\n")
interpretedID  = identifier.split(',')
print("What I interpreted: ")
print ("Email: " + interpretedID[0])
print ("Password: " + interpretedID[1])
print("\n")

user = auth.sign_in_with_email_and_password(interpretedID[0], interpretedID[1])

db = firebase.database()

userInfo = auth.get_account_info(user['idToken'])
UID = userInfo['users'][0]['localId']

trackingNumbers = db.child("users").child(UID).child("trackingNumbers").get(user['idToken']).val()

lcd.message('Welcome\n'+interpretedID[0])
sleep(3)
lcd.clear()

while(1):
    lcd.message('Ready to scan...')
    track = input("Enter Tracking Number")
    lcd.clear()
    if(track == "stop"):
        break
    trackingNumbers = db.child("users").child(UID).child("trackingNumbers").get(user['idToken']).val()
    if track in trackingNumbers.values():
        lcd.message('Tracking #\n found!')
        print("Tracking number exists")
        GPIO.output(21, 1)
        sleep(5)
        GPIO.output(21, 0)
        lcd.clear()
        
    else:
        lcd.message('Tracking\nnot found!')
        print("tracking number does not exist")
        GPIO.output(20, 1)
        sleep(5)
        GPIO.output(20, 0)
        lcd.clear()

GPIO.cleanup()
lcd.message('program\nexited')
print("exiting")
