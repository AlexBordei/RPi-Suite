import Adafruit_BMP.BMP085 as BMP085
import time


def setup():
    print('\n Barometer begins...')


def loop():
    while True:
        sensor = BMP085.BMP085()
        temp = sensor.read_temperature()  # Read temperature to veriable temp
        pressure = sensor.read_pressure()  # Read pressure to veriable pressure

        print('')
        print('      Temperature = {0:0.2f} C'.format(temp))  # Print temperature
        print('      Pressure = {0:0.2f} Pa'.format(pressure))  # Print pressure
        time.sleep(10)
        print('')


def destroy():
    pass


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
