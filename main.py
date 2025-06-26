import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

class planet():
    def __init__(self, x, y, z, mass, radius):
        self.x = x
        self.y = y 
        self.z = z
        self.mass = mass
        self.radius = radius

earth = planet(0, 0, 0, 5.972e24, 6371e3)
mars = planet(10, 5, 12, 6.417e23, 3389.5e3)
jupiter = planet(20, 15, 10, 1.898e27, 69911e3)
venus = planet(5, 10, 5, 4.867e24, 6051.8e3)


xpoint = [earth.x, mars.x, jupiter.x, venus.x]
ypoint = [earth.y, mars.y, jupiter.y, venus.y]
zpoint = [earth.z, mars.z, jupiter.z, venus.z]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 
ax.set_xlabel('X Coordinate (m)')
ax.set_ylabel('Y Coordinate (m)')
ax.set_zlabel('Z Coordinate (m)')
ax.set_title('3D Planetary Positions')

ax.text(earth.x, earth.y, earth.z, 'Earth', color='black') 
ax.text(mars.x, mars.y, mars.z, 'Mars', color='red')
ax.text(jupiter.x, jupiter.y, jupiter.z, 'Jupiter', color='orange')
ax.text(venus.x, venus.y, venus.z, 'Venus', color='yellow')
ax.scatter(xpoint, ypoint, zpoint, c='b', marker='o')
plt.show()