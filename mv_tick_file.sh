# !/bin/sh

CODE=$1
CURR_DIR=$(pwd)
#DEST_DIR="${CURR_DIR}/RealData/SZE/SZA/"
DEST_DIR="${CURR_DIR}/RealData/$2"

for f in $(ls sh.tick.out-*.csv)
do
    day=$(echo $f|cut -d'-' -f2|cut -d'.' -f1)
	echo "[info]: proccesing day[${day}]"
	mkdir -p ${DEST_DIR}/${day}/tick
	#mv ./sh.tick.out-${day}.csv ${DEST_DIR}/${day}/tick/${CODE}.csv
	mv ./$f ${DEST_DIR}/${day}/tick/${CODE}.csv
done
echo "[info]: finish"
