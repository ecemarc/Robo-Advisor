# app/robo_advisor.py

import requests
import json

#
# INFO INPUTS
#
#
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(request_url)
print(type(response))  # class
print(response.status_code)  # we got 200
print(response.text)  # string-need to import json module


# parse use the json module called jason.loads to change response.text to dictionary
parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

last_closing_price = parsed_response["Time Series (5min)"]["2020-06-05 14:50:00"]["4. close"]


def usd_price(last_closing_price):
    return f"${last_closing_price:,.2f}"  # > $12,000.71

# breakpoint()


#
#
#


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {usd_price(float(last_closing_price))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
