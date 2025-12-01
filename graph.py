import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x, y, z = np.meshgrid(np.arange(-4, 4, 1),
                      np.arange(-4, 4, 1),
                      np.arange(0, 4, 1))

ax.quiver(x, y, z, -y-x, x-y, -z, length=0.6, normalize=True)
ax.set_title("The Vector Feild F = [-y-x,x-y,-z]")
ax.axes.get_xaxis().set_ticks([])
ax.axes.get_yaxis().set_ticks([])
ax.axes.get_zaxis().set_ticks([])

def animate(i):
    ax.view_init(elev=30, azim=(i*0.1))
    return ax,

ani = FuncAnimation(fig, animate,frames=3600, interval=20, blit=False)
print(ani.to_html5_video())
