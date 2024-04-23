import yfinance as yf

# Define the ticker symbol for Reliance Industries Limited
ticker_symbol = "RELIANCE.NS"

# Fetch data
reliance = yf.Ticker(ticker_symbol)

# Get the historical prices for this ticker
reliance_hist = reliance.history(period="1mo")  # 1 month of data

# Print the historical data
print(reliance_hist)

# Get current price using another method
current_price = reliance.info['regularMarketPreviousClose']

print(f"Current price of {ticker_symbol}: {current_price}")
