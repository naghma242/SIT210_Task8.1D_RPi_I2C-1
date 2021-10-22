import smbus
import time

BH1750_sensor = 0x23

turnoff = 0x00  # represent 0 if power is off
turnon   = 0x01 # represent 1 if power is on
Reset     = 0x07 # resetting the whole setup

recieved_address = 0x23

bus = smbus.SMBus(1)

def Light():
  address = bus.read_i2c_block_data(BH1750_sensor,recieved_address)
  value = Light_intensity(address)
  return value

def Light_intensity(address): 
  result=(address[1] + (256 * address[0])) / 1.2
  return (result)

def message():
  while True:
    intensity=Light()
    print(Light())
    if(intensity>= 1300):
        print("Too Bright")
    elif(intensity> 500 and intensity<900):
        print("Bright")
    elif(intensity > 100 and intensity< 400):
        print("Medium")
    elif(intensity<100 and intensity>20):
        print("Dark")
    elif(intensity<20):
        print("Too Dark")
 
    time.sleep(0.25)

message()
