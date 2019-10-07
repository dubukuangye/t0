# 1. transaction file: delete 5th, 9th, 10th, 14th column
cat SHL2_TRANSACTION_600615_201808.csv|csvcut -C 5,9,10,14 > ot.csv

# 2. add other filed using vim [hong]

# 3. reorder
csvcut -c 1-7,10-12,9,8,13 ot.csv > ot1.csv

# rename field

# 4. split according to tradingDay
/usr/local/bin/csvtk split ot1.csv -f tradingDay

# 5. mv file to right path
./mv_file.sh
