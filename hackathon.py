import investpy
import matplotlib.pyplot as plt
import pandas
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

historicalData = investpy.get_stock_historical_data(stock=stockName,country=countryName,from_date=startDate,to_date=endDate)
#historicalData = investpy.get_stock_historical_data('TSLA','United States','10/09/2016','10/10/2016', as_json=True)


LastTenDays = json.loads(historicalData)

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