#!/bin/bash
MYNAME="Uysse"
echo "Hello $MYNAME" 
Year=2024
mkdir -p "$YEAR"




for MONTH in {01..12}
do
    mkdir -p "$YEAR/MONTH"

    DAYS_IN_MONTH=$(cal $MONTH $YEAR | awk 'NF {DAYS = $NF}; END {print DAYS}')

    for DAY in $(seq -w 01 $DAYS_IN_MONTH)
    do
        DAY_NAME=$(date -d "$YEAR-$MONTH" +%A)

        echo "$YEAR/$MONTH/$DAY is a $DAY_NAME" > "$YEAR/$MONTH/$DAY.txt"
    done
done
