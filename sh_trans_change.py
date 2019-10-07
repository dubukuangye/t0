# !/usr/local/bin/python3
# 1. turnover = volume * price
# 2. BSFlag = (bidOrder>SellOrder) ? buy : sell
# 3. generate recorderTime

import pandas as pd
import numpy as np

# add column name
column_names = ['instrument','tradingDay','TradingTime','index','TradeChannel','price','volume','turnover','UNIX','Market','bidOrder','askOrder','bsFlag','SecurityID']
df = pd.read_csv('x.csv', names=column_names, dtype={'instrument':str, 'tradingday':str})

field_dels=['TradeChannel', 'UNIX', 'Market', 'SecurityID']

for f in field_dels:
    df.drop([f],axis=1,inplace=True)

# del day of TradingTime field
df['updateTime']=df['TradingTime'].str.split(' ',expand=True)[1]
df.drop(['TradingTime'],axis=1,inplace=True)

df['orderKind']=''
df['functionCode']=''
df['recorderTime']=df['updateTime']

#def _reorder(i, name):
#    tmp=df[name]
#    df.drop(labels=[name], axis=1,inplace = True)
#    df.insert(i, name, tmp)
#
## reorder
#_reorder(2, 'Time')
#_reorder(3, 'Milliseconds')
#_reorder(4, 'LastPrice')
#_reorder(5, 'OpenPrice')
#_reorder(6, 'HighestPrice')
#_reorder(7, 'LowestPrice')
#_reorder(8, 'BidPrice1')
#_reorder(9, 'BidVolume1')
#_reorder(10, 'AskPrice1')
#_reorder(11, 'AskVolume1')
#
#_reorder(12, 'BidPrice2')
#_reorder(13, 'BidVolume2')
#_reorder(14, 'AskPrice2')
#_reorder(15, 'AskVolume2')
#_reorder(16, 'BidPrice3')
#_reorder(17, 'BidVolume3')
#_reorder(18, 'AskPrice3')
#_reorder(19, 'AskVolume3')
#_reorder(20, 'BidPrice4')
#_reorder(21, 'BidVolume4')
#_reorder(22, 'AskPrice4')
#_reorder(23, 'AskVolume4')
#_reorder(24, 'BidPrice5')
#_reorder(25, 'BidVolume5')
#_reorder(26, 'AskPrice5')
#_reorder(27, 'AskVolume5')
#_reorder(28, 'Volume')
#_reorder(29, 'Turnover')
#_reorder(30, 'OpenInterest')
#_reorder(31, 'PreOpenInterest')
#_reorder(32, 'PreSettlementPrice')
#_reorder(33, 'PreClosePrice')
#_reorder(34, 'UpperLimitPrice') #
#_reorder(35, 'LowerLimitPrice') # error: not provide
#_reorder(36, 'ClosePrice')
#_reorder(37, 'SettlementPrice')
#_reorder(38, 'PreDelta')
#_reorder(39, 'CurrDelta')
#_reorder(40, 'PreIOPV')
#_reorder(41, 'IOPV')
#_reorder(42, 'State')
#_reorder(43, 'RecordDate')
#_reorder(44, 'RecordTime')
#_reorder(45, 'RecordCounter')
#_reorder(46, 'BidPrice6')
#_reorder(47, 'BidVolume6')
#_reorder(48, 'AskPrice6')
#_reorder(49, 'AskVolume6')
#
#_reorder(50, 'BidPrice7')
#_reorder(51, 'BidVolume7')
#_reorder(52, 'AskPrice7')
#_reorder(53, 'AskVolume7')
#_reorder(54, 'BidPrice8')
#_reorder(55, 'BidVolume8')
#_reorder(56, 'AskPrice8')
#_reorder(57, 'AskVolume8')
#_reorder(58, 'BidPrice9')
#_reorder(59, 'BidVolume9')
#_reorder(60, 'AskPrice9')
#_reorder(61, 'AskVolume9')
#_reorder(62, 'BidPrice10')
#_reorder(63, 'BidVolume10')
#_reorder(64, 'AskPrice10')
#_reorder(65, 'AskVolume10')
df.to_csv('z.csv', index=None)

