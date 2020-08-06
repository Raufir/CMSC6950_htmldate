import csv
import pandas as pd
import numpy as np
from htmldate import find_date
import matplotlib.pyplot as plt

#reading the data input file
data = pd.read_csv("top500Domains.csv")
data =data.head(20)

#appending 'https://' at the begining of URL's
url_list = 'https://' + data['Root Domain']

#calling find_date() for each URL with progress
def wrapper_find_date(url):
    print(url)
    p = find_date(url)
    print('Found date for url', p)
    return p

#Getting publication date and putting into a new column
data['Publish Date'] = url_list.apply(wrapper_find_date)

#sanitizing the dataframe by removing rows with 'None' value
data = data.mask(data.eq('None')).dropna()
data = data.sort_values(by = 'Publish Date')

#creating two more different columns for month and year
data['Year'] = pd.DatetimeIndex(data['Publish Date']).year
data['Month'] = pd.DatetimeIndex(data['Publish Date']).month

#creating new reference for Year and Month for future data manipulation
year = data['Year']
month = data['Month']

#building the first plot
plt.rcParams['figure.figsize'] = [20, 10]
fig,ax =  plt.subplots()
ax.hist(year,100,histtype='bar',color="#45855f",density=False)
ax.set_xlabel("Year")
ax.set_ylabel("Frequency")
ax.xaxis.set_ticks(np.arange(1998, 2021, 1))
fig.suptitle("Year wise publication/upgradation frequency of top 500 websites", fontsize=14, fontweight='bold')
fig.savefig('Plot1.png')

#building the second plot
plt.rcParams['figure.figsize'] = [20, 10]
fig,ax =  plt.subplots()
ax.hist(month,100,histtype='bar',color="#45855f",density=False)
ax.set_xlabel("Months")
ax.set_ylabel("Frequency")
ax.xaxis.set_ticks(np.arange(1, 13, 1))
fig.suptitle("Month wise publication/upgradation frequency of top 500 websites", fontsize=14, fontweight='bold')
fig.savefig('Plot2.png')

print("Plot file is ready!")