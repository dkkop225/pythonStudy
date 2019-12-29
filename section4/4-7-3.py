import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018,2,1)
end = datetime.datetime(2018,2,15)

gs = web.DataReader('KRX: 035720','google',start,end)
