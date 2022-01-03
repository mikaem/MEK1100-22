import numpy as np
import matplotlib.pyplot as plt

# transpose nedenfor tilpasser datasett som var lagret for bruk i Matlab
# slik at de kan brukes i Python

p = np.transpose(np.loadtxt('trykkfelt.dat'))
u = np.transpose(np.loadtxt('vindfelt_u.dat'))
v = np.transpose(np.loadtxt('vindfelt_v.dat'))

print(p.shape)
print(u.shape)
print(v.shape)

Nx, Ny = p.shape

isobarer = np.arange(980, 1025, 5)
x = np.linspace(0, (Nx-1)*55, Nx)
y = np.linspace(0, (Ny-1)*55, Ny)
xx, yy = np.meshgrid(x, y, indexing='ij')
plt.figure(figsize=(5, 5))
CS = plt.contour(xx, yy, p, isobarer)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')

plt.figure(figsize=(5, 5))
plt.quiver(xx, yy, u, v)

l = np.sqrt(u**2 + v**2)
l_max = l.max()
print('max vindhastighet ', l_max)

dx = x[1]-x[0]
dy = y[1]-y[0]
dudx = np.gradient(u, dx, axis=0)
dvdy = np.gradient(v, dy, axis=1)
div = dudx + dvdy
plt.figure(figsize=(5, 5))
isobarer = np.array([-9, -4, -3, -2, -1, 0, 1, 2])
CS = plt.contour(xx, yy, div, 10)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')

dudy = np.gradient(u, dy, axis=1)
dvdx = np.gradient(v, dx, axis=0)
curlz = dvdx - dudy
plt.figure(figsize=(5, 5))
CS = plt.contour(xx, yy, curlz)
plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f', colors='k')
#plt.show()

# Plot mesh
plt.figure(figsize=(5, 5))
for i in range(y.shape[0]):
    plt.plot((x[0], x[-1]), (y[i], y[i]), 'k')
for i in range(x.shape[0]):
    plt.plot((x[i], x[i]), (y[0], y[-1]), 'k')