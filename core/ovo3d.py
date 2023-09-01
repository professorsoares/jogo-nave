import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

a = 4
b = 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-0.5 * np.pi, 0.5 * np.pi, 100)  # Ajuste de intervalo para parecer mais com um ovo
u, v = np.meshgrid(u, v)
x = a * np.cos(u) * np.cos(v)
y = b * np.sin(u) * np.cos(v)
z = 1.5 * (a * b) * np.sin(v)  # Ajuste da equação z para um ovo mais natural

ax.plot_surface(x, y, z, color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Desenho 3D de um ovo')
plt.show()
