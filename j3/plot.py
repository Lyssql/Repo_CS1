import numpy as np
import matplotlib.pyplot as plt

plt.plot([np.sin(1), 2, 3, 4])
plt.ylabel('random numbers')
plt.savefig("test.png")