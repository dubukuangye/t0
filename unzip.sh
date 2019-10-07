
CODE_LIST="bottom200of500.txt"

code_count_str=$(wc -l ${CODE_LIST} |awk '{print $1}')
code_count=$(expr $code_count_str)
i=0
while [ $i -lt $code_count ]
do
	read code
	echo "[info]: proccesing code[${code}]\n"
    unzip GTA_SEL2_TAQ_201907.zip GTA_SEL2_TAQ_201907/SHL2_TAQ_${code}_201907.csv
	i=$(expr $i + 1)
done < ${CODE_LIST}
echo "[info]: finish"
