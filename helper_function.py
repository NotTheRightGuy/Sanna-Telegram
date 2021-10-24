import yfinance as yf

def info_stock(stock):
    ticker = yf.Ticker(stock)
    raw_dic = ticker.info
    with open('temp.txt','w') as file:
        for keys in raw_dic:
            var_str = "{} : {}\n".format(keys,raw_dic[keys])
            file.write(var_str)
        




