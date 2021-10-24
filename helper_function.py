import yfinance as yf

def stock_history(stock_name):
    stock_ticker = yf.Ticker(stock_name)
    stock_info_dic = stock_ticker.info
    hist = stock_ticker.history(period='max')
    #return stock_info_dic
    return hist
