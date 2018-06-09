#!/usr/bin/env python
# -*- coding: utf-8 -*-
# codigo realizado por
# Jose David Ramos Rios
# 161002940
# scrits hace uso de una emulacion de trayectoria de la particula.
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def _update_plot(i,fig,scat):
    scat.set_offsets(([i,pow(i*0.2,2)],[50,50],[100,i]))
    print('Frames : %d' %i)

    return scat,
fig = plt.figure()

x= [0, 2, 3]
y= [3, 4, 5]

ax = fig.add_subplot(111)
ax.grid(True,linestyle = '-', color = '0.5')
ax.set_xlim([-50, 200])
ax.set_ylim([-50, 200])

scat = plt.scatter(x, y, c = x)
scat.set_alpha(0.8)

anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig , scat),
                               frames = 100, interval = 100)
plt.show()
