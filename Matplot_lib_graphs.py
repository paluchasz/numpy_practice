import numpy as np
import matplotlib.pyplot as plt


#plotting a sine function from x=0 to x=3*pi, plotting x every 0.1 (which gives smooth enough curve)
x = np.arange(0, 3 * np.pi, 0.1)

axes = plt.gca()
#axes.set_xlim([0, 3 * np.pi])
axes.set_ylim([-3, 3])

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.plot(x,y_tan)
plt.title('Sine, Cosine and Tan')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(['Sine','Cosine', 'Tan'])
plt.show()
