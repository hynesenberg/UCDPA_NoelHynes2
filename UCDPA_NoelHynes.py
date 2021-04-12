import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from pylab import *


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

#update old stock name PCLN to it's new stock symbol, BKNG
Sp500_Time_new['Symbol'].replace(to_replace=['PCLN'],value='BKNG',inplace=True)

#left join merge for the 2 tables, on the mutual column "Symbol"
Sp500 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')
print(Sp500.head())

#second copy of left join merge of the tables to edit later in the file
Sp500_10 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')

#filter on the last day of tradigng for each stock and print resulting table
Sp500_last = Sp500.drop_duplicates(subset=['Symbol'], keep='last')
print(Sp500_last)

#Set an index to the filtered table
Sp500_last_2 =Sp500_last.reset_index()
print(Sp500_last_2)

print(Sp500_last_2.info())
#

plt.scatter(Sp500_last_2.index, Sp500_last_2['close'])
plt.title("Closing Values for each SP500 Stock")
plt.xlabel("Stock Index")
plt.ylabel("Closing Stock Value")
plt.show()

#hkgk
#Sp500_last_2 =Sp500_last_2.sort_values(by=['Founded'])
ax = Sp500_last_2['Country'].value_counts().plot.bar()

#plt.figure(figsize=(8,6))
_ = ax.set_title('Countries where S&P500 Stock were Founded')
_ = ax.set_xlabel('Country where Stock Founded')
_ = ax.set_ylabel('# of Stocks Founded')
plt.show()

#n hjlhk
Sp500_last_3 =Sp500_last_2.sort_values(by=['Founded'])
#reset index
Sp500_last.plot(kind='scatter', x= 'Founded', y='Symbol')
#set_xticks(Sp500_last['Country'][::10])
plt.title("Year S&P500 Stock were Founded")
plt.xlabel("Year")
plt.ylabel("Stock Index")
plt.show()

trx = Sp500_last['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
plt.title("Industry Sector of S&P500 Stocks")
plt.xlabel("Industry Sector")
plt.ylabel("# of Stocks")
plt.show()

Sp500_sort=Sp500_last.sort_values(by=['close'])
Sp500_top10 = Sp500_sort.tail(10)

Top10 =[]
Top10 = Sp500_top10['Symbol'].tolist()
print(Top10)


Sp500_T10 = Sp500_10[Sp500_10['Symbol'].isin(Top10)]
print(Sp500_T10)

Sp500_T10["date"] = pd.to_datetime(Sp500_T10["date"])

Sp500_T10_last = Sp500_T10.drop_duplicates(subset=['Symbol'], keep='last')
Sp500_T10_last_2 =Sp500_T10_last.sort_values(by=['Founded'])

#a2x = Sp500_T10_last_2['Founded'].value_counts().plot.bar()
Sp500_T10_last_2.plot(kind='scatter', x= 'Founded', y='Symbol')
plt.title("Year Top 10 S&P500 Stocks were Founded")
plt.xlabel("Year")
plt.ylabel("Stock Index")
plt.show()

Sp500_T10["date"] = pd.to_datetime(Sp500_T10["date"])
Sp500_T10.pivot(index="date", columns="Symbol", values="close").plot()
plt.title("Top 10 S&P500 Stocks Prices")
plt.xlabel("Year")
plt.ylabel("Stock Price")
plt.show()

arx = Sp500_T10_last_2['Country'].value_counts().plot.bar()
_ = ax.set_title('Countries where Top 10 S&P500 Stock were Founded')
_ = ax.set_xlabel('Country where Stock Founded')
_ = ax.set_ylabel('# of Stocks Founded')
plt.show()

trex = Sp500_T10_last_2['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
plt.title("Industry Sector of Top10 S&P500 Stocks")
plt.xlabel("Industry Sector")
plt.ylabel("# of Stocks")
plt.show()


###########
Botswana = np.array(df['Botswana'])        #filter out the Botswana data from the dataset


plt.scatter(Year,World, c='b', marker='x', label='World')
plt.scatter(Year, Botswana, c='g', marker='s', label='Botswana')    #As well as scattering the World urban Pop % over time, let's also plot the Botswana urban % over the last 60 years. we will plot with green boxes
plt.plot(Year, fitLine, c='r')                       #Display World Fitline in Red
plt.title('Linear Regression')           #Adding a title, and axis labels for tidyness
plt.xlabel('Year')
plt.ylabel('Urban Population %')

plt.legend(loc='upper left')            #Add a legend for clarity
plt.show()