
for f in $(ls ./GTA_SEL2_TAQ_201907/*.csv)
do
    day=$(echo $f|cut -d'.' -f2|cut -d'_' -f6)
    if [ -f "./RealData/SSE/SHA/20190731/tick/${day}.csv" ]
    then
        echo "[info]: skip $day"
    else
        echo "[info]: ./sh_tick_convert.sh $f"
        ./sh_tick_convert.sh $f
    fi
done
echo "[info]: finish"
