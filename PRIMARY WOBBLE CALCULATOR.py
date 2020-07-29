#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
from astropy import units as u
from astropy import constants as const
from astropy.units import imperial
imperial.enable()


# In[61]:


my_data = pd.read_csv('./HamiltonianStateOut_172800.0_40.0_40.0_4_2_output_example.csv')
my_data
posi_x = my_data['posi-x'].values
posi_y = my_data['posi-y'].values
posi_z = my_data['posi-z'].values


# In[62]:


Vp = 248474846.2*u.m**3
Vs = 2309564.878*u.m**3
Ms = 5.01175578e09*u.kg
Mp = 5.39190416e11*u.kg


# In[63]:


class Dart(object):

    def __init__(self, posi_x=None, posi_y=None, posi_z=None, primary_mass=None, secondary_mass=None):
        self.posi_x = posi_x
        self.posi_y = posi_y
        self.posi_z = posi_z
        self.primary_mass = primary_mass
        self.secondary_mass = secondary_mass
    def distance(self):
        result = np.sqrt(self.posi_x**2 + self.posi_y**2 + self.posi_z**2)
        return result * u.m
    def one(self):
        result = (self.secondary_mass*self.distance())/(self.primary_mass*(1+self.secondary_mass/self.primary_mass))
        return result * u.m
    def bary_x(self):
        result = -(self.secondary_mass*self.posi_x)/(self.primary_mass*(1+self.secondary_mass/self.primary_mass))
        return result * u.m
    def bary_y(self):
        result = -(self.secondary_mass*self.posi_y)/(self.primary_mass*(1+self.secondary_mass/self.primary_mass))
        return result * u.m
    def bary_z(self):
        result = -(self.secondary_mass*self.posi_z)/(self.primary_mass*(1+self.secondary_mass/self.primary_mass))
        return result * u.m
    def two(self):
        result = np.sqrt(self.bary_x()**2 + self.bary_y()**2 + self.bary_z()**2)
        return result * u.m
    


# In[64]:


sample_model = Dart(posi_x = posi_x, posi_y = posi_y, posi_z = posi_z, primary_mass = Mp, secondary_mass = Ms)
bary_x = sample_model.bary_x()
bary_y = sample_model.bary_y()
bary_z = sample_model.bary_z()
sample_model.two()
sample_model.one()


# In[68]:


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

fig.set_size_inches(15,15)

fig.tight_layout()
ax.set_zlim3d(-0.01,0.01)

ax.plot(bary_x, bary_y, bary_z, c = "Maroon")
ax.scatter(bary_x, bary_y, bary_z, c = "Navy", s = 15);
ax.set_xlabel('x(m)')
ax.set_ylabel('y(m)')
ax.set_zlabel('z(m)')
ax.view_init(azim = 45, elev = 15)


# In[ ]:




