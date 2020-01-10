import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegWriter


fig, ax = plt.subplots()
A = range(-5,5)
xdata, ydata = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []

ln1, ln2, ln3, ln4 = ax.plot([], [], 'r-', 
                         [], [], 'b-', 
                         [], [], 'y-', 
                         [], [], 'c-', 
                         animated=False) #animated is associated with blit
                         
def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-6, 6)    
    return ln1,ln2,ln3,ln4

def update(i): #i is an int from 0 to frames-1, and keep looping
    ax.set_xlim(i/250, 10+i/250)
    global A
    iter = int(i/50)
    if i==0:
        xdata.clear()
        ydata.clear()
        xdata2.clear()
        ydata2.clear()
        iter = 0
    xdata.append(i/50)
    ydata.append(A[iter])
    xdata2.append(i/50)
    ydata2.append(np.cos(i/100))
    xdata3.append(i/50)
    ydata3.append(np.cos(i/100-np.pi))
    ln1.set_data(xdata, ydata)
    ln2.set_data(xdata2, ydata2)
    ln3.set_data(xdata3, ydata3)
    x = np.linspace(0, 10, 1000)
    y = np.sin(np.pi*(x + i/100))
    ln4.set_data(x, y)
    iter += 1
    return ln1, ln2, ln3, ln4

def main():
    ani = FuncAnimation(fig, update, frames = 500, interval = 20,
                    init_func=init, blit=False)
    writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save('animation.mp4',writer=writer) 
    plt.show()
        
if __name__ == '__main__':
    main()