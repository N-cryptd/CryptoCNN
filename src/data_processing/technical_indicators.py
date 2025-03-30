import talib
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_rsi(df, period=14):
    """
    Calculate Relative Strength Index (RSI) using TA-Lib.

    Args:
        df (pd.DataFrame): DataFrame with 'close' column.
        period (int): RSI period.

    Returns:
        pd.Series: RSI values.
    """
    logging.info(f"Calculating RSI for period: {period}")
    rsi = talib.RSI(df['close'], timeperiod=period)
    logging.info("RSI calculation complete.")
    return rsi

def calculate_sma(df, period=20):
    """
    Calculate Simple Moving Average (SMA) using TA-Lib.

    Args:
        df (pd.DataFrame): DataFrame with 'close' column.
        period (int): SMA period.

    Returns:
        pd.Series: SMA values.
    """
    logging.info(f"Calculating SMA for period: {period}")
    sma = talib.SMA(df['close'], timeperiod=period)
    logging.info("SMA calculation complete.")
    return sma

def calculate_macd(df, fast_period=12, slow_period=26, signal_period=9):
    """
    Calculate Moving Average Convergence Divergence (MACD) using TA-Lib.

    Args:
        df (pd.DataFrame): DataFrame with 'close' column.
        fast_period (int): Fast EMA period.
        slow_period (int): Slow EMA period.
        signal_period (int): Signal SMA period.

    Returns:
        tuple: MACD, Signal line, and Histogram as pd.Series.
    """
    logging.info(f"Calculating MACD with fast_period: {fast_period}, slow_period: {slow_period}, signal_period: {signal_period}")
    macd, signal, hist = talib.MACD(df['close'], fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
    logging.info("MACD calculation complete.")
    return macd, signal, hist

if __name__ == '__main__':
    # Example usage (for testing)
    data = {
        'close': [10, 11, 12, 13, 12, 14, 15, 14, 16, 17, 18, 19, 20, 19, 21, 22, 23, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    }
    df = pd.DataFrame(data)

    rsi_values = calculate_rsi(df)
    print("RSI Values:\n", rsi_values)

    sma_values = calculate_sma(df)
    print("\nSMA Values:\n", sma_values)

    macd_line, signal_line, hist_line = calculate_macd(df)
    print("\nMACD Line:\n", macd_line)
    print("\nSignal Line:\n", signal_line)
    print("\nHistogram:\n", hist_line)