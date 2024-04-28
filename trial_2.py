import numpy as np
import matplotlib.pyplot as plt
a=np.array([2,3,5])

print(a)
b=[1,2,3]
plt.plot(a,b)
plt.show()
c='text in string'
print(a,b,c)

a=a.tolist()
d=a+b