# Code made for automatic plant watering system project
# Excess comments for explanation to readers

# libraries
from machine import ADC, Pin
import utime

# variable definitions and defaults
relay = Pin(13,Pin.OUT)
moisture_sensor = ADC(27)
relay.value(0)
thresh = 30000

# infinite loop
while True:
    # variable to read moisture as a 16-bit value
    reading = moisture_sensor.read_u16()
    # variable to read voltage from 3.3V
    voltage = 3.3*reading/65535
    # prints voltage and soil sensor value
    print("Voltage:",voltage)
    print("Moisture:", reading)
    # if soil sensor reading is higher than threshold
    if reading > thresh:
        # print to screen that water is detected and that the pump remains off
        print ("Water detected. Pump off.")
        # keep pump turned off
        relay.value(0)
    # if soil sensor reading is less than threshold  
    if reading < thresh:
        # activate pump
        relay.value(1)
        # print to screen that pump is turned on after no water is detected
        print ("No water. Turning on pump!")
    # separate loop values
    print ("----")
    # while loop in 1 second intervals
    utime.sleep(1)

