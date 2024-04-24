import yfinance as yf

# Define the ticker symbol
ticker_symbol = "RELIANCE.NS"

# Fetch data
reliance = yf.Ticker(ticker_symbol)

# Get historical closing prices for the past year
reliance_hist = reliance.history(period="1y")

import matplotlib.pyplot as plt

# Plotting the closing prices
plt.figure(figsize=(10, 5))
plt.plot(reliance_hist.index, reliance_hist['Close'], label='Closing Price')
plt.title('Closing Stock Prices of Reliance Industries Over the Past Year')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.legend()
plt.grid(True)
plt.show()
