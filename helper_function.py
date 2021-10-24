import yfinance as yf

def stock_history(stock_name):
    stock_ticker = yf.Ticker(stock_name)
    hist = stock_ticker.history(period='max')
    return hist

def stock_info(stock_name):
    stock_ticker = yf.ticker(stock_name)
    stock_info_dic = stock_ticker.info
    return stock_info_dic
