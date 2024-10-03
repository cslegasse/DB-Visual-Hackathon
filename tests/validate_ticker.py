import yfinance as yf

def validate_ticker(ticker: str) -> bool:
    try:
        ticker_obj = yf.Ticker(ticker)
        # Try to access some basic info to verify the ticker
        _ = ticker_obj.info['symbol']
        return True
    except:
        return False