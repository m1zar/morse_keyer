#
# Python morse generator, reversing the decoding to encoding!
# James Wilkinson 2020
#
# Do imports...
import pyautogui as pa
import time

# Setup encoder variable..
#  012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
x="__TEMNAIOGKDWRUS_!QZYCXBJP_L_FVH09_8___7_(___/=61____+_&2___3_45_______:____,_____)__;________-__'___@____.__\"_____?____________"

def keyer(p):
    pa.keyDown('.')
#    pa.mouseDown()
    time.sleep(p)
    pa.keyUp('.')
#    pa.mouseUp()
    return

# Main detect and decode loop.
while True:
    text = input("TEXT->").upper()
    time.sleep(5)
    print("SENT->",end="")
# Loop through text..
    for i in text:
        print(i,end="")
        if i==" ":
                time.sleep(.28)
        else:
            morse=format(x.find(i),'b')[1:]
            for z in morse:
                    if z=="1":
                        keyer(0)
                    else:
                        keyer(.22)
# Next LETTER gap...
        time.sleep(.19)
    print("")
