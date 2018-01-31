
# coding: utf-8

# In[44]:

from numpy import array
import numpy as np
from random import random
from math import sin, sqrt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from IPython.display import HTML


# In[45]:

iter_max = 1000
pop_size = 100
dimensions = 2
c1 = 1 #Usuallly taken to be 2, Changed value for better visualization
c2 = 1
error_threshold = 0.00001

class particle:
    pass


# In[46]:

def f6(param):
    
    para = param * 10
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) *         (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) *             (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 = 0.5 - (num/denom)
    error_f6 =   1 - f6
    
    return f6, error_f6

def quad(param):
    
    para = param[0:2]
    quadr = -1*((param[0] - 15) * (param[0] - 15) + (param[1] - 15) * (param[1] - 15))
    error = (param[0] - 15) * (param[0] - 15) + (param[1] - 15) * (param[1] - 15)
    return quadr, error

particles = []

for i in range(pop_size):
    p = particle()
    p.params = array([random() for i in range(dimensions)]) #For f6
    #p.params = array([20 * random() for j in range(dimensions)]) #For our quadratic function
    p.fitness = 0
    p.v = 0.0
    particles.append(p)
    
gbest = particles[0]
err = 999999999

history = np.zeros((iter_max + 1, pop_size, dimensions))
arr = array([p.params for p in particles])
history[0, :,:] = arr

i=0

while i < iter_max:
    no_particle = 0
    err = 0
    for p in particles:
        fitness, err_t = f6(p.params) #For F6
        #fitness, err_t = quad(p.params) #For quadratic function
        err = err + err_t
        
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.params
            
        if fitness > gbest.fitness:
            gbest = p
            
        v = p.v + c1 * random() * (p.best - p.params)                 + c2 * random() * (gbest.params - p.params)
            
        p.params = p.params + v
        
        history[i, no_particle,:] = p.params
        no_particle +=1
        
    
    i +=1
        
        
    
    
    
    
    if err < error_threshold:
        break
    if i % (iter_max/10) == 0:
        print '.'
        
print '\nParticle Swarm Optimisation\n'
print 'PARAMETERS\n','-'*9
print 'Population size : ', pop_size
print 'Dimensions      : ', dimensions
print 'Error Criterion : ', error_threshold
print 'c1              : ', c1
print 'c2              : ', c2
print 'function        :   f6'

print 'RESULTS\n', '-'*7
print 'gbest fitness   : ', gbest.fitness
print 'gbest params    : ', gbest.params
print 'iterations      : ', i+1
    
    
    
        
        


# In[51]:

fig = plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)
graph, = plt.plot([],[], 'o')


def animate(i):
    
    graph.set_data(list(history[i, :, 0]), list(history[i, :, 1]))
    return graph

ani = FuncAnimation(fig, animate, frames=10, interval=1000)
HTML(ani.to_html5_video())


# In[ ]:



