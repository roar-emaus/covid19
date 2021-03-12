import pandas as pd
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('surveillance_data/covid19/data_covid19_lab_by_time_latest.csv')
df = df.set_index(pd.to_datetime(df['date']))
#df = df['2021-02-01':'2021-03-10']

fig_npos_rel = plt.figure()
ax = (df['n_pos']/(df['n_neg'] + df['n_pos'])).plot()
ax.set_ylabel(r'$\frac{\textbf{Positive}}{\textbf{Positive} + \textbf{Negative}}$')
fig_npos_rel.axes.append(ax)

fig_tot = plt.figure()
ax2 = (df['n_pos']+df['n_neg']).plot()
ax2.set_ylabel(r'\textbf{Total}')
fig_tot.axes.append(ax2)

fig_npos = plt.figure()
ax3 = df['n_pos'].plot()
ax3.set_ylabel(r'\textbf{Positive}')
fig_npos.axes.append(ax3)

plt.show()

