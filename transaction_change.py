# !/usr/local/bin/python3
# 1. turnover = volume * price
# 2. BSFlag = (bidOrder>SellOrder) ? buy : sell
# 3. generate recorderTime

import pandas as pd
import numpy as np
df = pd.read_csv('x.csv', dtype={'instrument':str, 'tradingday':str})

conditions = [
    (df['askOrder'] == 0) | (df['bidOrder'] == 0),
    (df['askOrder'] > df['bidOrder']),
    (df['askOrder'] < df['bidOrder'])]
choices = ['', 'S', 'B']
df['bsFlag'] = np.select(conditions, choices, default='N')
df['orderKind']=''
df['functionCode']=''
df['recorderTime']=df['updateTime']
df.to_csv('z.csv', index=None)

