import numpy as np 
import time
import random

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()
print("Vectorized version:", c, "Time:", toc - tic)

c = 0
tic = time.time()
for i in range(len(a)):
    c += a[i] * b[i]    
toc = time.time()
print("Loop version:", c, "Time:", toc - tic)
