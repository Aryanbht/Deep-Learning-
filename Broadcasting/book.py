import numpy as np

a = np.array([[56,0.0,4.4,68],[1.2,104,52,8.0],[1.8,135,99,0.9]])

print(a)

cal = a.sum(axis=0)
print(cal)

percentage = 100*a/cal.reshape(1,4)
print(percentage)