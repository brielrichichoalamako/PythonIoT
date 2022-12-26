from pyfirmata import util, Arduino
import time

# tentukan port arduino
board = Arduino('COM3')

# iterasi pin arduino
it = util.Iterator(board)
it.start()

# baca nilai analog pada pin (float)
nilai_analog = board.get_pin('a:0:i')

# void loop
while True:

    # pastikan nilai analog terbaca
    if nilai_analog.read() is not None:
        # konversi nilai float ke ADC
        nilai_ADC = nilai_analog.read()*1024

        # konversi nilai ADC ke milivolt
        nilai_milivolt = (nilai_ADC * 5000)/1024

        # koversi ke temperatur, 10mV/C untuk LM35
        temperatur_celcius = nilai_milivolt / 10

        # print
        print(temperatur_celcius)

# delay
time.sleep(2)
