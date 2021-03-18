# implements discrete fourier transform

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

sin = np.sin
cos = np.cos
pi = np.pi

def my_fft(x):
	# x is a numpy 1d array
	n = len(x)
	m = np.ones((n,n))
	for i in range(n):
		for k in range(n):
			m[i,k] = np.exp(-complex(0,2*np.pi*i*k/n))
	return np.dot(m,x)

if __name__ == "__main__":
	print("testing vectors")
	v1 = [np.exp(-t**2/30) for t in range(-100,100)]
	v2 = [sin(t*10) for t in range(600)]
	v3 = [cos(t*10) for t in range(600)]
	
	for v in [v1,v2,v3]:
		plt.subplots(figsize=(12,8))
		plt.subplot(1,3,1)
		plt.title("normal")
		plt.plot(v)
		plt.subplot(1,3,2)
		plt.title("fft")
		plt.plot(my_fft(v))
		plt.subplot(1,3,3)
		plt.title("scipy fft")
		plt.plot(fft(v))
		plt.show()



