# !/usr/local/bin/python3
# 1. turnover = volume * price
# 2. BSFlag = (bidOrder>SellOrder) ? buy : sell
# 3. generate recorderTime

import pandas as pd
import numpy as np
import csv

'''
{
	'20190101': {
		'600613': true,  # yest it's ST
		'600615': false,  
	},
	'20190203': {
		'600623': true,  
		'600715': false,
	},
}
'''
ST_MAP = {}

df = pd.read_csv('x.csv', 
        dtype={'instrument':str, 'tradingday':str},
        header=None
        )
# add header row
df.columns = ['Symbol','TradingDate','TradingTime','PreClosePrice','OpenPrice','HighPrice','LowPrice','LastPrice','TradeStatus','SellLevelNo','SellPrice10','SellPrice09','SellPrice08','SellPrice07','SellPrice06','SellPrice05','SellPrice04','SellPrice03','SellPrice02','SellPrice01','BuyPrice01','BuyPrice02','BuyPrice03','BuyPrice04','BuyPrice05','BuyPrice06','BuyPrice07','BuyPrice08','BuyPrice09','BuyPrice10','BuyLevelNo','SellVolume10','SellVolume09','SellVolume08','SellVolume07','SellVolume06','SellVolume05','SellVolume04','SellVolume03','SellVolume02','SellVolume01','BuyVolume01','BuyVolume02','BuyVolume03','BuyVolume04','BuyVolume05','BuyVolume06','BuyVolume07','BuyVolume08','BuyVolume09','BuyVolume10','TotalNo','TotalVolume','TotalAmount','TotalBuyOrderVolume','WtAvgBuyPrice','BondWtAvgBuyPrice','TotalSellOrderVolume','WtAvgSellPrice','BondWtAvgSellPrice','IOPV','YTM','UNIX','Market','ClosePrice','TotalBuyOrderNo01','TotalBuyOrderNo02','TotalBuyOrderNo03','TotalBuyOrderNo04','TotalBuyOrderNo05','TotalBuyOrderNo06','TotalBuyOrderNo07','TotalBuyOrderNo08','TotalBuyOrderNo09','TotalBuyOrderNo10','TotalSellOrderNo01','TotalSellOrderNo02','TotalSellOrderNo03','TotalSellOrderNo04','TotalSellOrderNo05','TotalSellOrderNo06','TotalSellOrderNo07','TotalSellOrderNo08','TotalSellOrderNo09','TotalSellOrderNo10','ETFBuyNo','ETFBuyVolume','ETFBuyAmount','ETFSellNo','ETFSellVolume','ETFSellAmount','WithdrawBuyNo','WithdrawBuyVolume','WithdrawBuyAmount','WithdrawSellNo','WithdrawSellVolume','WithdrawSellAmount','TotalBuyNo','TotalSellNo','MaxBuyDuration','MaxSellDuration','BuyOrderNo','SellOrderNo','SecurityID']

def _read_st_list():
    with open('st.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            day = row['date']
            if day not in ST_MAP:
                ST_MAP[day] = {}
            for k in row:
                if k == 'date': continue
                ST_MAP[day][k] = row[k]
    
def _reorder(i, name):
    tmp=df[name]
    df.drop(labels=[name], axis=1,inplace = True)
    df.insert(i, name, tmp)

def run():
    field_dels=['BondWtAvgBuyPrice','TotalSellOrderVolume','BondWtAvgSellPrice','YTM','ETFBuyNo','ETFBuyVolume','ETFBuyAmount','ETFSellNo','ETFSellVolume','ETFSellAmount','WithdrawBuyNo','WithdrawBuyVolume','WithdrawBuyAmount','WithdrawSellNo','WithdrawSellVolume','WithdrawSellAmount','TotalBuyNo','TotalSellNo','MaxBuyDuration','MaxSellDuration','BuyOrderNo','SellOrderNo','TotalNo','WtAvgSellPrice','SellLevelNo','TotalBuyOrderVolume','WtAvgBuyPrice','BuyLevelNo','UNIX','Market','TotalBuyOrderNo01','TotalBuyOrderNo02','TotalBuyOrderNo03','TotalBuyOrderNo04','TotalBuyOrderNo05','TotalBuyOrderNo06','TotalBuyOrderNo07','TotalBuyOrderNo08','TotalBuyOrderNo09','TotalBuyOrderNo10','TotalSellOrderNo01','TotalSellOrderNo02','TotalSellOrderNo03','TotalSellOrderNo04','TotalSellOrderNo05','TotalSellOrderNo06','TotalSellOrderNo07','TotalSellOrderNo08','TotalSellOrderNo09','TotalSellOrderNo10','SecurityID','TradeStatus']
    
    for f in field_dels:
        df.drop([f],axis=1,inplace=True)
    
    # del day of TradingTime field
    df['Time']=df['TradingTime'].str.split(' ',expand=True)[1]
    df.drop(['TradingTime'],axis=1,inplace=True)
    df['RecordTime']=df['Time']
    df['RecordDate']=df['TradingDate']
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
    # error need provide 
    #day = df['TradingDate']
    #symbol = df['Symbol']
    #conditions = [
    #    (ST_MAP[day][symbol] == False),
    #    (ST_MAP[day][symbol] == True)]
    #choices = [1.1, 1.05]
    #choices_lower = [0.9, 0.95]
    #df['UpperLimitPrice'] = df['PreClosePrice']*np.select(conditions, choices, default='N')
    #df['LowerLimitPrice']=df['PreClosePrice']*np.select(conditions, choices_lower, default='N')
    df['UpperLimitPrice'] = 0
    df['LowerLimitPrice'] = 0
    
    # rename
    name_changes={'Symbol': 'InstrumentID', 'TradingDate': 'TradingDay', 
            'TotalVolume': 'Volume', 'TotalAmount': 'Turnover',
            'HighPrice': 'HighestPrice', 'LowPrice': 'LowestPrice',
            'BuyPrice01': 'BidPrice1', 'BuyVolume01': 'BidVolume1',
            'SellPrice01': 'AskPrice1', 'SellVolume01': 'AskVolume1',
            'BuyPrice02': 'BidPrice2', 'BuyVolume02': 'BidVolume2',
            'SellPrice02': 'AskPrice2', 'SellVolume02': 'AskVolume2',
            'BuyPrice03': 'BidPrice3', 'BuyVolume03': 'BidVolume3',
            'SellPrice03': 'AskPrice3', 'SellVolume03': 'AskVolume3',
            'BuyPrice04': 'BidPrice4', 'BuyVolume04': 'BidVolume4',
            'SellPrice04': 'AskPrice4', 'SellVolume04': 'AskVolume4',
            'BuyPrice05': 'BidPrice5', 'BuyVolume05': 'BidVolume5',
            'SellPrice05': 'AskPrice5', 'SellVolume05': 'AskVolume5',
            'BuyPrice06': 'BidPrice6', 'BuyVolume06': 'BidVolume6',
            'SellPrice06': 'AskPrice6', 'SellVolume06': 'AskVolume6',
            'BuyPrice07': 'BidPrice7', 'BuyVolume07': 'BidVolume7',
            'SellPrice07': 'AskPrice7', 'SellVolume07': 'AskVolume7',
            'BuyPrice08': 'BidPrice8', 'BuyVolume08': 'BidVolume8',
            'SellPrice08': 'AskPrice8', 'SellVolume08': 'AskVolume8',
            'BuyPrice09': 'BidPrice9', 'BuyVolume09': 'BidVolume9',
            'SellPrice09': 'AskPrice9', 'SellVolume09': 'AskVolume9',
            'BuyPrice10': 'BidPrice10', 'BuyVolume10': 'BidVolume10',
            'SellPrice10': 'AskPrice10', 'SellVolume10': 'AskVolume10',
    }
    df.rename(columns=name_changes, inplace=True)
    
    # reorder
    _reorder(2, 'Time')
    _reorder(3, 'Milliseconds')
    _reorder(4, 'LastPrice')
    _reorder(5, 'OpenPrice')
    _reorder(6, 'HighestPrice')
    _reorder(7, 'LowestPrice')
    _reorder(8, 'BidPrice1')
    _reorder(9, 'BidVolume1')
    _reorder(10, 'AskPrice1')
    _reorder(11, 'AskVolume1')
    
    _reorder(12, 'BidPrice2')
    _reorder(13, 'BidVolume2')
    _reorder(14, 'AskPrice2')
    _reorder(15, 'AskVolume2')
    _reorder(16, 'BidPrice3')
    _reorder(17, 'BidVolume3')
    _reorder(18, 'AskPrice3')
    _reorder(19, 'AskVolume3')
    _reorder(20, 'BidPrice4')
    _reorder(21, 'BidVolume4')
    _reorder(22, 'AskPrice4')
    _reorder(23, 'AskVolume4')
    _reorder(24, 'BidPrice5')
    _reorder(25, 'BidVolume5')
    _reorder(26, 'AskPrice5')
    _reorder(27, 'AskVolume5')
    _reorder(28, 'Volume')
    _reorder(29, 'Turnover')
    _reorder(30, 'OpenInterest')
    _reorder(31, 'PreOpenInterest')
    _reorder(32, 'PreSettlementPrice')
    _reorder(33, 'PreClosePrice')
    _reorder(34, 'UpperLimitPrice') #
    _reorder(35, 'LowerLimitPrice') # error: not provide
    _reorder(36, 'ClosePrice')
    _reorder(37, 'SettlementPrice')
    _reorder(38, 'PreDelta')
    _reorder(39, 'CurrDelta')
    _reorder(40, 'PreIOPV')
    _reorder(41, 'IOPV')
    _reorder(42, 'State')
    _reorder(43, 'RecordDate')
    _reorder(44, 'RecordTime')
    _reorder(45, 'RecordCounter')
    _reorder(46, 'BidPrice6')
    _reorder(47, 'BidVolume6')
    _reorder(48, 'AskPrice6')
    _reorder(49, 'AskVolume6')
    
    _reorder(50, 'BidPrice7')
    _reorder(51, 'BidVolume7')
    _reorder(52, 'AskPrice7')
    _reorder(53, 'AskVolume7')
    _reorder(54, 'BidPrice8')
    _reorder(55, 'BidVolume8')
    _reorder(56, 'AskPrice8')
    _reorder(57, 'AskVolume8')
    _reorder(58, 'BidPrice9')
    _reorder(59, 'BidVolume9')
    _reorder(60, 'AskPrice9')
    _reorder(61, 'AskVolume9')
    _reorder(62, 'BidPrice10')
    _reorder(63, 'BidVolume10')
    _reorder(64, 'AskPrice10')
    _reorder(65, 'AskVolume10')
    df.to_csv('out.csv', index=None)

def calcLimitPrice():
    _read_st_list()

    data = []
    with open('out.csv') as csvfile, open('sh.tick.out.csv', 'w') as outfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            inst = row['InstrumentID']
            day = row['TradingDay']
            if inst != 'InstrumentID': # first line, field name
                preClosePrice = float(row['PreClosePrice'])
                if ST_MAP[day][inst]=='True':
                    row['UpperLimitPrice'] = preClosePrice*(1+0.05);
                    row['LowerLimitPrice'] = preClosePrice*(1-0.05);
                else:
                    row['UpperLimitPrice'] = preClosePrice*(1+0.1);
                    row['LowerLimitPrice'] = preClosePrice*(1-0.1);

            row['UpperLimitPrice'] = float("{0:.2f}".format(row['UpperLimitPrice']))
            row['LowerLimitPrice'] = float("{0:.2f}".format(row['LowerLimitPrice']))
            data.append(row)

        # write to file
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # 1. read st list
    run()
    # generate upper and lower limit price
    calcLimitPrice()
