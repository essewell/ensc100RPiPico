from machine import Pin, ADC
import utime


relay = Pin(18, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
runLed = Pin(2, Pin.OUT)
onBoardLed = Pin(25, Pin.OUT)
rainsense = Pin(16, Pin.IN)

rtc = machine.RTC()
rtc.datetime((2022, 12, 6, 2, 0, 0, 0, 0))#Date/Time set for user
timestamp = rtc.datetime
endTime = 10; #ends 6AM
startTime = 20; #starts 3AM

waterlvl = ADC(Pin(26))

waterLed = Pin(0, Pin.OUT)
rainLed = Pin(1, Pin.OUT)
runLed = Pin(2, Pin.OUT)
onBoardLed = Pin(25, Pin.OUT)

def rainCheck():
    if (rainsense.value() == 1):
        rainLed.value(0)
        return True
    else:
        rainLed.value(1)
        return False
    
            
            
def waterCheck():
    readingWater = waterlvl.read_u16()
    if readingWater < 30000:
        waterLed.value(1)
        return False
    else:
        waterLed.value(0)
        return True
    
def run():
    while (rainCheck()):
        utime.sleep(10)
        runLed.value(1)
        relay.value(1)
        utime.sleep(10)
        relay.vaue(0)
    
if __name__ == '__main__':
    run()
    
    