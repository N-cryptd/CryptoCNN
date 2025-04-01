import pandas as pd
import talib

# Load sample data
df = pd.read_csv('CryptoCNN/data/BTCUSDT_1h_test.csv')
sample_df = df.head(300).copy()
sample_df['close'] = pd.to_numeric(sample_df['close'], errors='coerce', downcast='float') # Explicitly format 'close' to float

# Calculate indicators using TA-Lib
expected_rsi_values = talib.RSI(sample_df['close'], timeperiod=14)
expected_sma_values = talib.SMA(sample_df['close'], timeperiod=20)
macd, signal_line, hist_line = talib.MACD(sample_df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Print last values
print("\nExpected RSI Value (Last):", expected_rsi_values[-1])
print("\nExpected SMA Value (Last):", expected_sma_values[-1])
print("\nExpected MACD Value (Last):", macd[-1])
print("\nExpected Signal Value (Last):", signal_line[-1])
print("\nExpected Histogram Value (Last):", hist_line[-1])

# Print lengths of indicator arrays
print("\nRSI Length:", len(expected_rsi_values))
print("\nSMA Length:", len(expected_sma_values))
print("\nMACD Length:", len(macd))
print("\nSignal Length:", len(signal_line))
print("\nHistogram Length:", len(hist_line))

# Print data shape and data types
print("\nSample Data Shape:\n", sample_df.shape)
print("\nData Types:\n", sample_df.dtypes)