# -*- coding: utf-8 -*-
"""
CEC 411 Lab 1

@author: james
"""

import numpy as py
import matplotlib.pyplot as plt

uStep = py.heaviside
# 1   Given original discrete signal X[n]:
    #    X[n] = [1,1,2,2,3], n = 1,2,3,4,5
    # Plot 
        # X[n]
        # X1[n] = X[n-2]
        # X2[n] = X[-n]

# 2 Given original discrete signal X[n]:
    #   X[n] = [1,0,-1,3,2], n = -1,0,1,2,3
    # Plot
        # X1[n] = X[n+3]
        # X2[n] = X[-n-3]
        
# 3 Plot the following signals:
# (1) X[n]=sin(2*pi*n/7),𝑛𝑛=1,2,3…20
# (2) X[n]=cos(pi*n/3), 𝑛𝑛 =1,2,3…20
# (3) X[n]=cos(2*pi*n/3)+sin(2*pi*n/5), 𝑛𝑛 =1,2,3…50
        
# 4 Given discrete signal X[n]:
# X[n]=n∗(u[n]−u[n−8]), 𝑛𝑛=1,2,3…20
# Plot X[n]

### Problem 1
#Plot original signal X[n] which will be represented by y

y = py.array([1, 1, 2, 2, 3])
n = py.array([1, 2, 3, 4, 5])

x = plt
x.figure(0)
x.title('Discrete Plot X[n]')
x.ylabel('y')
x.xlabel('n')
x.stem(n,y, '--')
x.grid(True)    


#https://matplotlib.org/examples/pylab_examples/stem_plot.html    


#Plot X1[n]
n = n+2
x1 = plt
x1.figure(1)
x1.title('Discrete Plot X1[n]')
x1.ylabel('y')
x1.xlabel('n')
x1.stem(n,y, '--')
x1.grid(True)       

#Plot X2[n]
#Reset n
y = py.array([1, 1, 2, 2, 3])
n = py.array([1, 2, 3, 4, 5])

n = 0-n
x2 = plt
x2.figure(2)
x2.title('Discrete Plot X2[n]')
x2.ylabel('y')
x2.xlabel('n')
x2.stem(n,y, '--')
x2.grid(True)  

### Problem 2
#Plot X1[n]
y = py.array([1,0,-1,3,2])
n = py.array([-1,0,1,2,3])

n = n+3
x1 = plt
x1.figure(3)
x1.title('Discrete Plot X1[n]')
x1.ylabel('y')
x1.xlabel('n')
x1.stem(n,y, '--')
x1.grid(True)  

#Plot X2[n]
#reset n
y = py.array([1,0,-1,3,2])
n = py.array([-1,0,1,2,3])

n = 0-(n+3)
x2 = plt
x2.figure(4)
x2.title('Discrete Plot X2[n]')
x2.ylabel('y')
x2.xlabel('n')
x2.stem(n,y, '--')
x2.grid(True)  

#Problem 3
# (1) X[n]=sin(2*pi*n/7),𝑛𝑛=1,2,3…20
# (2) X[n]=cos(pi*n/3), 𝑛𝑛 =1,2,3…20
# (3) X[n]=cos(2*pi*n/3)+sin(2*pi*n/5), 𝑛𝑛 =1,2,3…50
#part 1
nN = py.array(range(1,20))
y = py.sin((2*(py.pi)*nN)/7)

x1 = plt
x1.figure(4)
x1.title('Discrete Plot X1[n]')
x1.ylabel('y')
x1.xlabel('nN')
x1.stem(nN,y, '--')
x1.grid(True)  

#Part 2
nN = py.array(range(1,20))
y = py.cos(((py.pi)*nN)/3)

x1 = plt
x1.figure(4)
x1.title('Discrete Plot X2[n]')
x1.ylabel('y')
x1.xlabel('nN')
x1.stem(nN,y, '--')
x1.grid(True)  

#Part 3
nN = py.array(range(1,50))
y = (py.cos((2*(py.pi)*nN)/3))+(py.sin((2*(py.pi)*nN)/5))

x1 = plt
x1.figure(4)
x1.title('Discrete Plot X2[n]')
x1.ylabel('y')
x1.xlabel('nN')
x1.stem(nN,y, '--')
x1.grid(True)  

# 4 Given discrete signal X[n]:
# X[n]=n∗(u[n]−u[n−8]), 𝑛𝑛=1,2,3…20
# Plot X[n]

nN = py.array(range(0,30))
y = py.sin((2*(py.pi)*nN)/7)

u = uStep(nN,1)
print(u)

u2 = uStep(nN-8,1)
print(u2)

x1 = plt
x1.figure(4)
x1.title('Discrete Plot U[n]')
x1.ylabel('y')
x1.xlabel('nN')
x1.stem(nN,u-u2, '--')
x1.grid(True) 
