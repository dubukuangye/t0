# convert tick data for SH
# usage example: ./sh_tick_convert.sh SHL2_TAQ_603569_201907.csv
# 1. sh_tick_change.py
cp $1 x.csv
python3 sh_tick_change.py

# 2. split according to tradingDay
/usr/local/bin/csvtk split sh.tick.out.csv -f TradingDay

# 5. mv file to right path
code=$(sed -n '2p' sh.tick.out.csv |cut -d',' -f1)
./mv_tick_file.sh ${code} "SSE/SHA/"
