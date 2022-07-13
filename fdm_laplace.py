import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Lx = 1
Ly = 1

nx = 100
ny = 100

dx = Lx/(nx)
dy = Ly/(ny)

x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)

def solve_laplace(U, dx, dy, tolerance):
    error = 2 * tolerance
    iters = 0
    while (error > tolerance):
        U_prev = U.copy()
        #U[1: -1, 1: -1] = ((dy**2*(U_prev[2:,1:-1] + U_prev[0:-2,1:-1]) + dx**2*(U_prev[1:-1,2:]+U_prev[1:-1,0:-2]))/(2*(dx**2 + dy**2)))
        U[1: -1, 1: -1] = (U_prev[2:,1:-1] + U_prev[0:-2,1:-1] + U_prev[1:-1,2:]+U_prev[1:-1,0:-2])/4
        # since dx = dy 
        error = np.sum(U-U_prev, axis = None)
        iters += 1
    print(f'Iterations: {iters}')
    return U
        
U = np.zeros((nx, ny), dtype = np.float32)

U[:,0] = 0
U[:,-1] = 0
U[0,:] = 0
U[-1,:] = np.sin(6 * x)

tolerance = 1e-8

U = solve_laplace(U, dx, dy, tolerance)


fig = plt.figure(figsize=(15,15))
ax = fig.gca(projection='3d')

X,Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, U, cmap = 'plasma', linewidth = 0.5, antialiased = False)
ax.set_title('Numerical Solution', fontsize = 20)
ax.set_xlim(0, Lx)
ax.set_ylim(0, Ly)
ax.set_xlabel('x', fontsize = 20)
ax.set_ylabel('y', fontsize = 20)
ax.set_zlabel('Velocity', fontsize = 15)
