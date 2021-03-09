
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../surveillance_data/covid19/data_covid19_msis_by_time_location_2021-03-08.csv')
oslo = df[df['location_code'] == 'county03']
mr = df[df['location_code'] == 'county15']

for date in sorted(set(df['date'])):
    fig, ax = plt.subplots()
    ax.set_title(date)
    ax.set_xlim((0.01, 30))
    ax.set_xscale('log')
    ax.barh(y='Møre & Romsdal', width=float(mr[mr['date']==date]['pr100000']))
    ax.barh(y='Oslo', width=float(oslo[oslo['date'] == date]['pr100000']))
    #plt.show()
    print(date)
    #plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.savefig(f'{date}.png')
    plt.close(fig)
