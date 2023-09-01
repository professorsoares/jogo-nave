import matplotlib.pyplot as plt
import numpy as np

a = 4
b = 2

t = np.linspace(-np.pi, np.pi, 100)
x = a * np.cos(t)
y = b * 2.5 * np.sin(t)

plt.plot(x, y)
plt.show()
