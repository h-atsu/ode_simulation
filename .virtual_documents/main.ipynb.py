import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 


num_dim = 10
A = np.random.random((num_dim,num_dim))
r = np.abs(np.random.random(num_dim))
K = np.ones(num_dim)

for i in range(num_dim):
    A[i][i] = 1


def lotka_volterra(x, t, A, r, K):
    return r*x*(1 - A@x / K)        


dt = 0.01
T = 500.0
t = np.arange(0,T,dt)


args = (A,r,K)


x0 = abs(np.random.random(num_dim))


orbit = odeint(lotka_volterra, x0, t, args)


fig = plt.figure()
for i in range(num_dim):               
    plt.plot(t,orbit[:,i])
