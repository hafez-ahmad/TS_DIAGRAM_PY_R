# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:50:52 2020

@author: hafez
"""


import numpy as np
import pandas as pd
import gsw

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

data=pd.read_csv('tsdata2008_2020.csv')

ts=data[['temperatureSurface', 'salinitySurface']]

df=ts.sort_values('temperatureSurface',ascending=True)

mint=np.min(df['temperatureSurface'])
maxt=np.max(df['temperatureSurface'])

mins=np.min(df['salinitySurface'])
maxs=np.max(df['salinitySurface'])

tempL=np.linspace(mint-1,maxt+1,156)

salL=np.linspace(mins-1,maxs+1,156)

Tg, Sg = np.meshgrid(tempL,salL)
sigma_theta = gsw.sigma0(Sg, Tg)
cnt = np.linspace(sigma_theta.min(), sigma_theta.max(),156)

fig,ax=plt.subplots(figsize=(10,10))
#fig.suptitle('programmer:Hafez Ahmad', fontsize=14, fontweight='bold')
cs = ax.contour(Sg, Tg, sigma_theta, colors='grey', zorder=1)
cl=plt.clabel(cs,fontsize=10,inline=False,fmt='%.1f')

sc=plt.scatter(df['salinitySurface'],df['temperatureSurface'],c=cnt,s=10)

cb=plt.colorbar(sc)

ax.set_xlabel('Salinity ($‰$)')

ax.set_ylabel('Temperature[$^\circ$C]')
ax.set_title('General T-S (Temperature and salinity) Diagram',fontsize=14, fontweight='bold')
ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
ax.yaxis.set_major_locator(MaxNLocator(nbins=8))
ax.tick_params(direction='out')
cb.ax.tick_params(direction='out')
cb.set_label('Density[kg m$^{-3}$]')
plt.tight_layout()
plt.savefig('ts_diagram.png',format='png',dpi=900,transparent=False)
plt.show()

















