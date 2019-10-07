# convert tick data for SH
# 1. sh_tick_change.py
python3 sh_tick_change.py

# 2. split according to tradingDay
/usr/local/bin/csvtk split sh.tick.out.csv -f TradingDay

# 5. mv file to right path
./mv_tick_file.sh
