# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:02:29 2024

@author: james
"""
import matplotlib.pyplot as plt
import yfinance as yf

def getData(key):
    # Get data for Live Nation between 2019 and 2024
    company = yf.Ticker(key)
    hist = company.history(start="2019-06-01", end="2024-01-01")
    
    # Remove general market trend using S&P 500
    sp500 = yf.Ticker("^GSPC")
    sp500_hist = sp500.history(start="2019-06-01", end="2024-01-01")
    
    # Normalize stock prices (company stock price divided by index price)
    hist['Normalised'] = hist['Close'] / sp500_hist['Close']
    hist['N'] = hist['Normalised'] / hist['Normalised'].iloc[0]
    
    # Remove noise using a simple moving average
    hist['SMA'] = hist['N'].rolling(window=20).mean()
    
    return(hist)

LYV_hist = getData('LYV')
EB_hist = getData('EB')
MSGS_hist = getData('MSGS')
SIRI_hist = getData('SIRI')

# Plot the data
plt.figure(figsize=(10, 6))  # Optional: Set figure size
plt.plot(LYV_hist.index, LYV_hist['SMA'], label="Live Nation")
plt.plot(EB_hist.index, EB_hist['SMA'], label="Eventbrite")
plt.plot(MSGS_hist.index, MSGS_hist['SMA'], label="Madison Square Garden")
plt.plot(SIRI_hist.index, SIRI_hist['SMA'], label="SiriusXM")

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Live Music Stock Prices")

plt.grid(True)
plt.legend()

plt.show()
