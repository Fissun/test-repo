import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(leds, GPIO.OUT)

def decToBinList(decNumber):
    binNumber = bin(decNumber)
    mystr = str(binNumber)
    mystrcut = mystr[2::]
    mylist = list(map(int, mystrcut))
    myzerolist = [0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    for i in range(len(mylist)):
        myzerolist[8 - len(mylist) + i] = mylist[i]

    return myzerolist

    # for i in range(7): 
    #     GPIO.output(leds[i], myzerolist[i])
    #     time.sleep(3)

def lightNumber (number):   
    n = decToBinList(number)

    i = 0 
    for i in range(7): 
        GPIO.output(leds[i], n[i])

    time.sleep(3)

def PutOutNumber (number):   
    n = decToBinList(number)

    i = 0 
    for i in range(7): 
        GPIO.output(leds[i], n[i])

    time.sleep(3)
    
def RunningPattern (number, direct)
    
    k = 1
    
    wile k = 1:
        n = decToBinList(number)
        
        i = 0 
        for i in range(7): 
            GPIO.output(leds[i], n[i])
    
        time.sleep(3)
        
        for i in range(7): 
            GPIO.output(leds[i], 0)
        
        time.sleep(3)
    
        n = np.roll(n, direct)
    
    
RunningPattern(7, 1)

GPIO.cleanup()



