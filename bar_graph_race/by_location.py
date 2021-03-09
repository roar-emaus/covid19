import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

sur_path = Path('../surveillance_data/covid19')
dates = []
oslo = []
aalesund = []
paths = sorted(list(sur_path.glob('data_covid19_msis_by_location_20*.csv')))
for path in paths:
    df = pd.read_csv(path)
    df = df[df['location_code'].isin(['municip0301', 'municip1507'])]
    d_v = str(path).split('location_')[-1].split('.csv')[0]
    o_v = float(df[df['location_name']=='Oslo']['pr100000'])
    a_v = float(df[df['location_name']=='Ålesund']['pr100000'])
    dates.append(d_v)
    oslo.append(o_v)
    aalesund.append(a_v)
    
    fig, ax = plt.subplots()
    ax.set_title(d_v)
    ax.bar(x='Oslo', height=o_v)
    ax.bar(x='Ålesund', height=a_v)
    plt.savefig(f'{d_v}.png')
    plt.close(fig)
    
