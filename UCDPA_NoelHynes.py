import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Source of all_stocks file
#https://www.kaggle.com/camnugent/sandp500?select=all_stocks_5yr.csv

#Source of Symbol Details
#https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

#Read in both csv files from computer, note symbol_Detail file is encoded using "ISO-8859-1" so this was added to code
#first file provides the opening, closing prices for each of the SP500 stocks, including high and low price for the day and trading volume
Sp500_Time = pd.read_csv(r"c:\Users\user\OneDrive\Desktop\DA Finance\Assignement\UCDPA_NoelHynes2\all_stocks_5yr.csv")
#second file provides added detail for each of the SP500 stocks, such as Inductry sector, year company was founded and country they are based
Sp500_Detail = pd.read_csv(r"c:\Users\user\OneDrive\Desktop\DA Finance\Assignement\UCDPA_NoelHynes2\Symbol_Detail.csv", encoding = "ISO-8859-1")

#print first 5 lines of both datasets
print(Sp500_Time.head())
print(Sp500_Detail.head())

#rename columnname "Name" to "Symbol", to align with corresponding column in other table
Sp500_Time_new = Sp500_Time.rename(columns={'Name': 'Symbol'})

#print first 5 lines of updated table
print(Sp500_Time_new.head())

#left join merge for the 2 tables, on the mutual column "Symbol"


Sp500_10 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')
Sp500 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')
print(Sp500.head())

Sp500_last = Sp500.drop_duplicates(subset=['Symbol'], keep='last')
print(Sp500_last)

Sp500_last.plot(kind='scatter', x= 'close', y='Symbol')
#plt.show()



ax = Sp500_last['Country'].value_counts().plot.bar()
_ = ax.set_xlabel('Owner')
_ = ax.set_ylabel('Frequency')

#plt.show()

Sp500_last.plot(kind='scatter', x= 'Founded', y='Symbol')
#plt.show()



trx = Sp500_last['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
#plt.show()

Sp500_sort=Sp500_last.sort_values(by=['close'])
Sp500_top10 = Sp500_sort.tail(10)

Top10 =[]
Top10 = Sp500_top10['Symbol'].tolist()
print(Top10)


Sp500_T10 = Sp500_10[Sp500_10['Symbol'].isin(Top10)]
print(Sp500_T10)

Sp500_T10["date"] = pd.to_datetime(Sp500_T10["date"])
Sp500_T10.pivot(index="date", columns="Symbol", values="close").plot()

Sp500_T10_last = Sp500_T10.drop_duplicates(subset=['Symbol'], keep='last')

a2x = Sp500_T10_last['Founded'].value_counts().plot.bar()
_ = a2x.set_xlabel('Owner')
_ = a2x.set_ylabel('Frequency')

plt.show()