import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


#style.use('fivethirtyeight')
csv_file = 'electricity-consumption-of-wind-power-in-various-provinces-and-regions.csv'
df = pd.read_csv(csv_file, sep=';')
df.rename(columns={'Year-on-year increase%':'yearly_increase%'}, inplace=True)
df.drop([3], inplace=True)


def increase_in_use():
    df['Electricity'] *= df['yearly_increase%']


df.sort_values(by='Electricity', ascending=True, inplace=True)

fig, axes = plt.subplots(1, 2)

ax1 = df.plot.bar(ax=axes[0], x='Province', y='Electricity', figsize=(11,4),
                  subplots=True)
ax2 = df.plot.bar(ax=axes[1], x='Province', y='yearly_increase%',figsize=(11,4),
                  color=[np.where(df['yearly_increase%'] < 0, 'r', 'g')])
axes[1].set_title('Average Year-on-Year Percentage Increase in Usage of Wind Energy (2012-2016)',fontsize=11)

print(df.describe())
print(df.head(33))
plt.tight_layout()
plt.show()



