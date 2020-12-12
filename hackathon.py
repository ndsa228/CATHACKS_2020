#imports
import investpy

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
                                        to_date=endDate)


print(historicalData.tail(10))

