# !/bin/sh

CODE="002008"
CURR_DIR=$(pwd)
DEST_DIR="${CURR_DIR}/RealData/L2Records/Transactions/"

DAY_LIST="list.day"

day_count_str=$(wc -l ${DAY_LIST} |awk '{print $1}')
day_count=$(expr $day_count_str)
i=0
while [ $i -lt $day_count ]
do
	read day
	echo "[info]: proccesing day[${day}]"
	mkdir -p ${DEST_DIR}/${day}
	mv ./002008.trans-${day}.csv ${DEST_DIR}/${day}/${CODE}.csv
	i=$(expr $i + 1)
done < ${DAY_LIST}
echo "[info]: finish"
