#!/bin/bash
URLS=./urls
OUT=/home/waqeel/Documents/proceedings

# Venue handler mapping
declare -A HANDLERS=(
	["sigcomm"]="./acm.py"
	["imc"]="./acm.py"
	["hotnets"]="./acm.py"
	["nsdi"]="./usenix.py"
	["osdi"]="./usenix.py"
	["usenixsec"]="./usenix.py"
)

VENUE=$1
YEAR=$2
LIST=$OUT/$VENUE/$YEAR/list

mkdir -p $OUT/$VENUE/$YEAR
PAGE=`awk -v v=$VENUE-$YEAR '$1 == v {print $2}' $URLS`
STYLE=`awk -v v=$VENUE-$YEAR '$1 == v {print $3}' $URLS`

# Get all papers and dump (name link) to $LIST
${HANDLERS[$VENUE]} $PAGE $STYLE > $LIST

while read -r line
do
	# wget each item in $LIST
	DEST=$OUT/$VENUE/$YEAR/`echo $line | cut -d" " -f1`
	LINK=`echo $line | cut -d" " -f2`
	wget $LINK -O $DEST.pdf
done < $LIST
