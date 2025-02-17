import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
print("hello")
def animate1(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')
    for i, l in enumerate(pullData):
            pass
    print i + 1
    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-1000:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
while True:
    ani = animation.FuncAnimation(fig, animate1, interval=1000)
    plt.show()
    time.sleep(10)