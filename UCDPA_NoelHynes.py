import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

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
print(Sp500.info())

#could add a dropna() here but want full range of values for next chart

#second copy of left join merge of the tables to edit later in the file
Sp500_10 = Sp500_Time_new.merge(Sp500_Detail, on='Symbol', how='left')

#filter on the last day of tradigng for each stock and print resulting table
Sp500_last = Sp500.drop_duplicates(subset=['Symbol'], keep='last')
print(Sp500_last)

#Set an index to the filtered table
Sp500_last_2 =Sp500_last.reset_index()
print(Sp500_last_2)

#print table info for more insight
print(Sp500_last_2.info())

#next we will produce scatter chart of the closing prices for the 505 stocks, adding labels and a title and using the index for the x axis
plt.scatter(Sp500_last_2.index, Sp500_last_2['close'])
plt.title("Closing Values for each SP500 Stock")
plt.xlabel("Stock Index")
plt.ylabel("Closing Stock Value")
plt.show()

Sp500_last_2 = Sp500_last_2.dropna()
print(Sp500_last_2.info())

#now we will produce a bar chart with the country of origin for these large companies
ax = Sp500_last_2['Country'].value_counts().plot.bar()
_ = ax.set_title('Countries where S&P500 Stock were Founded')
_ = ax.set_xlabel('Country where Stock Founded')
_ = ax.set_ylabel('# of Stocks Founded')
plt.show()

#scatter chart on year founded
Sp500_last_2.plot(kind='scatter', x= 'Founded', y='Symbol')
#set_xticks(Sp500_last['Country'][::10])
plt.title("Year S&P500 Stock were Founded")
plt.xlabel("Year")
plt.ylabel("Stock Index")
plt.show()

#count the stocks by sector to show the mix of industries which feature on the market index. using different colours to represent each industry
trx = Sp500_last['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
plt.title("Industry Sector of S&P500 Stocks")
plt.xlabel("Industry Sector")
plt.ylabel("# of Stocks")
plt.show()

#sort the closing values to find the stocks with the largest share prices, the top 10
Sp500_sort=Sp500_last.sort_values(by=['close'])
Sp500_top10 = Sp500_sort.tail(10)


#create a list of the top 10 stocks
Top10 =[]
Top10 = Sp500_top10['Symbol'].tolist()
print(Top10)

#filter the entire dataset down to the stocks in the top 10
Sp500_T10 = Sp500_10[Sp500_10['Symbol'].isin(Top10)]
print(Sp500_T10)

Sp500_T10["date"] = pd.to_datetime(Sp500_T10["date"])

Sp500_T10_last = Sp500_T10.drop_duplicates(subset=['Symbol'], keep='last')
Sp500_T10_last_2 =Sp500_T10_last.sort_values(by=['Founded'])

#scatter plot of when the top 10 stocks were founded
Sp500_T10_last_2.plot(kind='scatter', x= 'Founded', y='Symbol')
plt.title("Year Top 10 S&P500 Stocks were Founded")
plt.xlabel("Year")
plt.ylabel("Stock Index")
plt.show()

#plot stocks prices over time
Sp500_T10["date"] = pd.to_datetime(Sp500_T10["date"])
Sp500_T10.pivot(index="date", columns="Symbol", values="close").plot()
plt.title("Top 10 S&P500 Stocks Prices")
plt.xlabel("Year")
plt.ylabel("Stock Price")
plt.show()

#plot count by country of where top 10 were founded
arx = Sp500_T10_last_2['Country'].value_counts().plot.bar()
_ = ax.set_title('Countries where Top 10 S&P500 Stock were Founded')
_ = ax.set_xlabel('Country where Stock Founded')
_ = ax.set_ylabel('# of Stocks Founded')
plt.show()

#plot industries of top 10 stocks
trex = Sp500_T10_last_2['GICS Sector'].value_counts().plot.bar(color=['grey', 'c','red' ,'peru', 'lightpink', 'yellow', 'orange','blue', 'purple', 'green', 'lavender'])
plt.title("Industry Sector of Top10 S&P500 Stocks")
plt.xlabel("Industry Sector")
plt.ylabel("# of Stocks")
plt.show()


###

Sp500_GOOG = Sp500[Sp500['Symbol']=="GOOG"]
print(Sp500_GOOG)

Sp500_GOOG = Sp500_GOOG.reset_index()
print(Sp500_GOOG)


Year = np.array(Sp500_GOOG['index'])
GOOG_Close = np.array(Sp500_GOOG['close'])

plt.scatter(Year, GOOG_Close)
plt.show()

from scipy import stats                  #import scipy package from  stats libary

slope, intercept, r_value, p_value, std_err = stats.linregress(Year, GOOG_Close)

print(r_value ** 2)  #calculating our R**2 value

import matplotlib.pyplot as plt         #import libraries needed

def predict(x):
    return slope * x + intercept

fitLine = predict(Year)                 #predict a fitline to show predictions using linear regression on timstep and Stock price

plt.scatter(Year, GOOG_Close)               #scatter our data
plt.plot(Year, fitLine, c='r')         #plot our fitline, in colour red
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.show()