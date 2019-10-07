# 1. tick_change.py
python3 tick_change.py

# 2. reorder
csvcut -c 1-3,57,8,5-7,31,41,20,30,32,42,19,29,33,43,18,28,34,44,17,27,35,45,16,26,9-10,58-60,4,51-52,53,61,63,62,64,54,65,56,55,66,36,46,15,25,37,47,14,24,38,48,13,23,39,49,12,22,40,50,11,21 z.csv > a.csv

# 3. time field: del .

# 4. split according to tradingDay
/usr/local/bin/csvtk split a.csv -f TradingDay

# 5. mv file to right path
./mv_tick_file.sh
