import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
        '../surveillance_data/covid19/data_covid19_msis_by_time_sex_age_latest.csv'
        )
df = df[['sex', 'age', 'date', 'n']]
df = df.set_index('date')

for i in set(df.index):
    fig, ax = plt.subplots()
    ax.set_title(i)
    ax.set_ylim((0,1))

    sub_df = df.loc[i]
    male = sub_df[sub_df['sex'] == 'male']
    female = sub_df[sub_df['sex'] == 'female']

    fem_n = male['n'].values
    mal_n = female['n'].values 
    all_n = fem_n + mal_n
    fem_age = female['age'].values
    
    all_norm_n = np.linalg.norm(all_n)
    #mal_norm_n = np.linalg.norm(mal_n)
    #fem_norm_n = np.linalg.norm(fem_n)
    
    ax.bar(x=fem_age, height=all_n/all_norm_n)
    #ax.bar(x=fem_age, height=fem_n/fem_norm_n, label='female')
    #ax.bar(x=fem_age, height=mal_n/mal_norm_n, label='male')
    print(f'{i}.png')
    plt.savefig(f'{i}.png')
    #plt.legend()
    #plt.show()
    plt.close(fig)

