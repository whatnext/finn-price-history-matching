import yfinance as yf

msft = yf.Ticker("MSFT")

tickers = yf.Tickers()

print(f"tickers: {tickers}");

# get all stock info
print (f"info {msft.info}");

#hist = msft.history(period="10y")

hist = msft.history(
	start = "1980-01-01",
	end = "1990-01-01"
);

print (f"history: {hist}");
print("hist is a " + str(type(hist)))