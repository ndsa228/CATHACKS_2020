import investpy
import matplotlib.pyplot as plt
import pandas as pd
import json

dates = []
closes= []

print('What stock would you like to review?')
stockName = input()
print('What country is the stock from?')
countryName = input()
print('Input a date you would like to review the stock from. (dd/mm/yyyy).')
startDate = input()
print('Input a date you would like to review the stock to. (dd/mm/yyyy).')
endDate = input() 

historicalData = investpy.get_stock_historical_data(stock=stockName,
                                                    country=countryName,
                                                    from_date=startDate,
                                                    to_date=endDate, as_json=True)
print(historicalData) #.tail(10) 
LastTenDays = json.loads(historicalData) #.head().to_json()

for i in range(0,10):
    dates.append(LastTenDays['historical'][i]['date'])
    closes.append(LastTenDays['historical'][i]['close'])
    

'''
for i in range(LastTenDays):
	dates = LastTenDays.values[i][0]
	closes = LastTenDays.values[i][1]
'''
plt.plot(dates, closes)
plt.show()
