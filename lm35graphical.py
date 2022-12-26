from pyfirmata import util, Arduino
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import datetime as dt
import time

board = Arduino('COM3')
it = util.Iterator(board)
it.start()

nilai_analog = board.get_pin('a:0:i')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
temperature_y = []
waktu_x = []


def animate(i, xs, ys):

    tem_celcius = 0
    if nilai_analog.read() is not None:
        adcValue = nilai_analog.read()*1024
        milivolt = (adcValue * 5000) / 1024
        tem_celcius = milivolt / 10

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(tem_celcius)

    # limit x dan y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # draw x dan y lists
    ax.clear()
    ax.plot(xs, ys)

    # format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('LM35 - Arduino via Python')
    plt.ylabel('Temperature (deg C)')


ani = anim.FuncAnimation(fig, animate, fargs=(waktu_x, temperature_y))
plt.show()
time.sleep(2)
