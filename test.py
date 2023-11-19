import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

f = 2.0
sec = 1

t = np.arange(0,sec,1/1000)
y = np.sin(2 * np.pi * f * t)

samp_1_t = t[::50]
samp_1_y = y[::50]

samp_2_t = t[::200]
samp_2_y = y[::200]

samp_3_t = t[::300]
samp_3_y = y[::300]

plt.plot(t,y,"g-",label="analog")
plt.plot(samp_1_t,samp_1_y,"r-",label="20Hz")
plt.plot(samp_2_t,samp_2_y,"b-",label="5Hz")
plt.plot(samp_3_t,samp_3_y,"k-",label="3Hz")


plt.legend(loc=7)
plt.savefig("sampling.jpg")
plt.show()