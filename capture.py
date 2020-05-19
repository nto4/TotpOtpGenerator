import pyautogui
from pyzbar.pyzbar import decode

from PIL import Image
import pyotp
import time

#Screen shot current windows and detect qr code  
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'.\qr.png')
x = decode(Image.open('qr.png'))

#Clean  decoded qr code and get secret key
x=str(x)
start = 't='
end = '&'
secret = (x[x.find(start)+len(start):x.rfind(end)])

#if you want to enter your secret key comment upper line and uncomment down line 
#secret = "YOUR KEY GOES HERE"
while True:
    totp = pyotp.TOTP(secret, interval= 30)
    x= int(time.time())
    x = 30 - (x %30)
    print("Current OTP:   "+ str(totp.now()) + "     Until time:  "+ str(x) ,end="\r")
    #print("Current OTP:   "+ str(totp.now()) + "     Until time: "+ str(x) )
    time.sleep(1)

"""
Default parameters;
6 digit otp
30 sec interval
ptotp default algorithm openssl_sha1 
"""
