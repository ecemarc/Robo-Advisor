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


time_series = parsed_response["Time Series (5min)"]

dates = list(time_series.keys())

# taking the "0" from dates list "2020-06-05 14:50:00"   //is latest date first?? MAKE SURE
latest_5min = dates[0]

last_closing_price = time_series[latest_5min]["4. close"]


def usd_price(last_closing_price):
    return f"${last_closing_price:,.2f}"  # > $12,000.71

# breakpoint()


recent_highs = []  # creating a list of highs to find the highest

for date in dates:
    recent_high = time_series[date]["2. high"]
    recent_highs.append(float(recent_high))


recent_highest = max(recent_highs)  # creating a list and

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
print(f"RECENT HIGH: {usd_price(float(recent_highest))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
