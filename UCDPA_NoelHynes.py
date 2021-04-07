import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Sp500_Time = pd.read_csv(r"c:\Users\user\OneDrive\Desktop\DA Finance\Assignement\UCDPA_NoelHynes2\all_stocks_5yr.csv")

Sp500_Detail = pd.read_csv(r"c:\Users\user\OneDrive\Desktop\DA Finance\Assignement\UCDPA_NoelHynes2\Symbol_Detail.csv", encoding = "ISO-8859-1")

print(Sp500_Time.head())
print(Sp500_Detail.head())

Sp500_Time_new = Sp500_Time.rename(columns={'Name': 'Symbol'})

print(Sp500_Time_new.head())

Sp500 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')
print(Sp500.head())

Sp500_last = Sp500.drop_duplicates(subset=['Symbol'], keep='last')
print(Sp500_last)

Sp500_last.plot(kind='scatter', x= 'close', y='Symbol')
plt.show()

#Sp500_last.plot(kind='bar', x='Country', y='Symbol')
#plt.show()
ax = Sp500_last['Country'].value_counts().plot.bar()
_ = ax.set_xlabel('Owner')
_ = ax.set_ylabel('Frequency')

plt.show()

Sp500_last.plot(kind='scatter', x= 'Founded', y='Symbol')
plt.show()



trx = Sp500_last['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
plt.show()

Sp500_sort=Sp500_last.sort_values(by=['close'])
Sp500_top10 = Sp500_sort.tail(10)

print(Sp500_top10['Symbol'])