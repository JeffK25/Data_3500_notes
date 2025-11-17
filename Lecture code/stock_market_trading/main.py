
import requests
import json

#keys
key1 = "Time Series (Daily)"
key2 = "4. close"

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

request = requests.get(url)
request_dictionary = json.loads(request.text)

file = open("/workspaces/Data_3500_notes/Lecture code/stock_market_trading/AAPL.csv", "w")


#save the date and the close price in a csv file
#how to we isolate the close price and the date?

for date in request_dictionary[key1].keys():
    file.write(date + ", " + request_dictionary[key1][date][key2] + "\n")



# lines = []

# lines = lines[::-1]
# file.writelines(lines)
# file.close()

