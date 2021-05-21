import pandas as pd
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np


start_date = '2021-01-01'
end_date = None

df_lab = pd.read_csv('surveillance_data/covid19/data_covid19_lab_by_time_latest.csv')
df_lab = df_lab.set_index(pd.to_datetime(df_lab['date']))
df_lab = df_lab[start_date:end_date]

fig_npos_rel = plt.figure()
ax = (df_lab['n_pos']/(df_lab['n_neg'] + df_lab['n_pos'])).plot(drawstyle="steps-post",)
ax.set_ylabel(r'$\frac{\textbf{Positive}}{\textbf{Positive} + \textbf{Negative}}$')
fig_npos_rel.axes.append(ax)

fig_tot = plt.figure()
ax2 = (df_lab['n_pos']+df_lab['n_neg']).plot(drawstyle="steps-post",)
ax2.set_ylabel(r'\textbf{Total}')
fig_tot.axes.append(ax2)

fig_npos = plt.figure()
ax3 = df_lab['n_pos'].plot(drawstyle="steps-post",)
ax3.set_ylabel(r'\textbf{Positive}')
fig_npos.axes.append(ax3)

df_hospital = pd.read_csv('surveillance_data/covid19/data_covid19_hospital_by_time_latest.csv')
df_hospital = df_hospital.set_index(pd.to_datetime(df_hospital['date']))
df_hospital = df_hospital[df_hospital['location_code'] == 'norge']
df_hospital = df_hospital[start_date:end_date]
fig_hospital = plt.figure()
ax4 = df_hospital['n_icu'].plot(label='Intensiven', drawstyle="steps-post",)
ax5 = df_hospital['n_hospital_main_cause'].plot(label='Hovedårsak', drawstyle="steps-post",)
ax4.set_ylabel(r'$\frac{\textbf{Innlagt}}{\textbf{Dag}}$')
ax5.set_title('COVID-19 Innlagte')
fig_hospital.axes.append(ax4)
fig_hospital.axes.append(ax5)
plt.legend()

plt.show()

