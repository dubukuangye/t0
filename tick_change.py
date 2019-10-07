# !/usr/local/bin/python3
# 1. turnover = volume * price
# 2. BSFlag = (bidOrder>SellOrder) ? buy : sell
# 3. generate recorderTime

import pandas as pd
import numpy as np
df = pd.read_csv('x.csv', dtype={'instrument':str, 'tradingday':str})


df.drop(['TotalNo'],axis=1,inplace=True)
df.drop(['TradeNo'],axis=1,inplace=True)
df.drop(['TradeVolume'],axis=1,inplace=True)
df.drop(['TradeAmount'],axis=1,inplace=True)
df.drop(['PERatio1'],axis=1,inplace=True)
df.drop(['PERatio2'],axis=1,inplace=True)
df.drop(['TotalAskOrderVolume'],axis=1,inplace=True)
df.drop(['WtAvgAskPrice'],axis=1,inplace=True)
df.drop(['AskLevelNo'],axis=1,inplace=True)
df.drop(['TotalBidOrderVolume'],axis=1,inplace=True)
df.drop(['WtAvgBidPrice'],axis=1,inplace=True)
df.drop(['BidLevelNo'],axis=1,inplace=True)
df.drop(['UNIX'],axis=1,inplace=True)
df.drop(['Market'],axis=1,inplace=True)
#df.drop(['PriceUpLimit'],axis=1,inplace=True)
#df.drop(['PriceDownLimit'],axis=1,inplace=True)
df.drop(['PriceUpdown1'],axis=1,inplace=True)
df.drop(['PriceUpdown2'],axis=1,inplace=True)
df.drop(['SecurityPhaseTag'],axis=1,inplace=True)
df.drop(['NAV'],axis=1,inplace=True)
df.drop(['PremiumRate'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo01'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo02'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo03'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo04'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo05'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo06'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo07'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo08'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo09'],axis=1,inplace=True)
df.drop(['TotalBidOrderNo10'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo01'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo02'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo03'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo04'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo05'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo06'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo07'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo08'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo09'],axis=1,inplace=True)
df.drop(['TotalAskOrderNo10'],axis=1,inplace=True)
df.drop(['SymbolSource'],axis=1,inplace=True)
df.drop(['SecurityID'],axis=1,inplace=True)

df['Time']=df['Time'].str.split(' ',expand=True)[1]
df['RecordTime']=df['Time']
df['RecordDate']=df['TradingDay']
df['Milliseconds']=0
df['OpenInterest']=0
df['PreOpenInterest']=0
df['PreSettlementPrice']=0
df['SettlementPrice']=0
df['CurrDelta']=0
df['PreDelta']=0
df['PreIOPV']=0
df['State']=0
df['RecordCounter']=0

df.to_csv('z.csv', index=None)

