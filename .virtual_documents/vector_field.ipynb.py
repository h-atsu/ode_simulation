import numpy as np 
import matplotlib.pyplot as plt 


def f(x,y):
    return np.array([2*x, 2*y])
def g(x,y):
    return np.array([-2*x + y, -2*y])


def viz_vector(f:callable):
    plt.figure(figsize = (8,8))

    lx,ly = 15., 15.
    dx = np.linspace(-lx,lx,10)
    dy = np.linspace(-ly,ly,10)
    X,Y = np.meshgrid(dx, dy)

    colors = [np.linalg.norm(f(i,j)) for i in dx for j in dy]

    fX, fY = f(X,Y)
    plt.quiver(X,Y,fX,fY, colors, cmap = 'Reds')
    plt.grid()


viz_vector(g)


vid
