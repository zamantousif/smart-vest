import RPi.GPIO as GPIO
import time
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

COOLING_REQD = True
HEAT_REQD = False

# configure the temperature sensor
temp_sensor = Adafruit_DHT.DHT22
temp_pin = 4 # it is pin 'GCK' in io.BCM format

# configure the pins for the fans
fan1 = 18
fan2 = 23
fan3 = 24
fan4 = 25

GPIO.setup(fan1, GPIO.OUT)
GPIO.setup(fan2, GPIO.OUT)
GPIO.setup(fan3, GPIO.OUT)
GPIO.setup(fan4, GPIO.OUT)

# configure the pins for the heating pads
heatpad1 = 17
heatpad2 = 27
heatpad3 = 22

GPIO.setup(heatpad1, GPIO.OUT)
GPIO.setup(heatpad2, GPIO.OUT)
GPIO.setup(heatpad3, GPIO.OUT)

# test the led at pin 10
#for i in range(10):
	#print("Led turning on.")
	#GPIO.output(ledpin, GPIO.HIGH)
	#time.sleep(0.5)
	#print("Led turning off.")
	#GPIO.output(ledpin, GPIO.LOW)
	#time.sleep(0.5)

# function to read the temperature sensor and switch to COOLING/HEATING
def check_temp(temp):

	if temp > 24:
		COOLING = True
		HEATING = False
		#GPIO.output(led_pin, io.HIGH)
	if temp < 24:
		COOLING = False
		HEATING = True
		#GPIO.output(led_pin, io.LOW)
	
	TEMP_STATUS = [COOLING, HEATING]
	
	return TEMP_STATUS


# function to turn ON the fans
def turn_on_fans():
	GPIO.output(fan1, GPIO.HIGH)
	print("Fan1 turning on.")
	#time.sleep(0.5)
	GPIO.output(fan2, GPIO.HIGH)
	print("Fan2 turning on.")
	#time.sleep(0.5)
	GPIO.output(fan3, GPIO.HIGH)
	print("Fan3 turning on.")
	#time.sleep(0.5)
	GPIO.output(fan4, GPIO.HIGH)
	print("Fan4 turning on.")
	#time.sleep(0.5)

# function to turn OFF the fans
def turn_off_fans():
	GPIO.output(fan1, GPIO.LOW)
	print("Fan1 turning off.")
	#time.sleep(0.5)
	GPIO.output(fan2, GPIO.LOW)
	print("Fan2 turning off.")
	#time.sleep(0.5)
	GPIO.output(fan3, GPIO.LOW)
	print("Fan3 turning off.")
	#time.sleep(0.5)
	GPIO.output(fan4, GPIO.LOW)
	print("Fan4 turning off.")
	#time.sleep(0.5)

# function to turn ON the heating pads
def turn_on_heatpads():
	GPIO.output(heatpad1, GPIO.HIGH)
	print("Heatpad1 turning on.")
	#time.sleep(0.5)
	GPIO.output(heatpad2, GPIO.HIGH)
	print("Heatpad2 turning on.")
	#time.sleep(0.5)
	GPIO.output(heatpad3, GPIO.HIGH)
	print("Heatpad3 turning on.")
	#time.sleep(0.5)

# function to turn OFF the heating pads
def turn_off_heatpads():
	GPIO.output(heatpad1, GPIO.LOW)
	print("Heatpad1 turning off.")
	#time.sleep(0.5)
	GPIO.output(heatpad2, GPIO.LOW)
	print("Heatpad2 turning off.")
	#time.sleep(0.5)
	GPIO.output(heatpad3, GPIO.LOW)
	print("Heatpad3 turning off.")
	#time.sleep(0.5)
		
# the MAIN function for the program
def main():
	
	# the following stuff needs to be looped forever
	

	# monitor the temperature sensor to decide if COOLING/HEATING 
	# would be required
	t = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
	print "Temperature right now is", t[1]
	# t[0] is humidity and t[1] is temp in celcius
	time.sleep(2) # if you do print(t) it will print a tuple 
	                                   # of (humidity, temp)
	# check temperature for COOLING/HEATING status
	[COOLING_REQD, HEAT_REQD] = check_temp(t[1])
	
	# check if cooling is required and turn on/off the fans
	if COOLING_REQD == True:
		turn_on_fans()
	else:
		turn_off_fans()
	
	# check if heating is required and turn on/off the heatpads
	if HEAT_REQD == True:
		turn_on_heatpads()
	else:
		turn_off_heatpads()
		
	# monitor the heart rate sensor
	
	# monitor the accelerometer/gyrometer/magnetometer
	

if __name__ == "__main__":

	while True:
		main()
