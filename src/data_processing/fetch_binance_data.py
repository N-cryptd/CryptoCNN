import requests
import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_klines(symbol, interval, start_time=None, end_time=None, limit=500):
    """
    Fetches candlestick data from Binance API and saves it to a CSV file.

    Args:
        symbol (str): Trading pair symbol (e.g., "BTCUSDT").
        interval (str): Candlestick interval (e.g., "1m", "1h", "1d").
        start_time (int, optional): Start timestamp in milliseconds. Defaults to None.
        end_time (int, optional): End timestamp in milliseconds. Defaults to None.
        limit (int, optional): Number of data points to retrieve. Defaults to 500, max 1000.

    Returns:
        pandas.DataFrame: DataFrame containing the fetched kline data, or None if an error occurs.
    """
    base_url = "https://api.binance.com"
    endpoint = "/api/v3/klines"
    url = base_url + endpoint

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    if start_time:
        params["startTime"] = start_time
    if end_time:
        params["endTime"] = end_time

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                           'close_time', 'quote_asset_volume', 'number_of_trades',
                                           'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        numeric_cols = ['open', 'high', 'low', 'close', 'volume', 'quote_asset_volume',
                        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col])

        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", f"{symbol}_{interval}.csv")
        df[['timestamp', 'open', 'high', 'low', 'close', 'volume']].to_csv(file_path, index=False)

        logging.info(f"Successfully fetched and saved {symbol} {interval} data to {file_path}")
        return df

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error fetching {symbol} {interval} data: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error fetching {symbol} {interval} data: {req_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while fetching {symbol} {interval} data: {e}")

    return None

if __name__ == '__main__':
    # Example usage: fetch 1-hour klines for BTCUSDT
    symbol = "BTCUSDT"
    interval = "1h"
    df_btc_1h = fetch_klines(symbol, interval)
    if df_btc_1h is not None:
        print(f"DataFrame for {symbol} {interval} fetched successfully.")
    else:
        print(f"Failed to fetch DataFrame for {symbol} {interval}.")