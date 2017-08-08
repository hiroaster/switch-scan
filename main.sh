#!/bin/sh

DATE=`date +%Y%m%d`


cat swlist.txt | while read switchinfo
do

switchip=`echo $switchinfo | awk '{print $1}'`
community=`echo $switchinfo | awk '{print $2}'`

sysname=`snmpwalk -v 2c -c $community $switchip 1.3.6.1.2.1.1.5.0 | sed 's/"//g' | sed 's/.*STRING://g'`

snmpwalk -v 2c -c $community  $switchip 1.3.6.1.2.1.2.2.1.2 | grep "GE" > gig.txt


cat gig.txt | while read line

do

oid=`echo $line | sed 's/.*ifDescr.//g' | sed 's/ =.*//g' `
ifname=`echo $line | sed 's/"//g' | sed 's/.*STRING://g'`
status=`snmpwalk -v 2c -c $community $switchip 1.3.6.1.2.1.2.2.1.8.$oid | sed 's/.*INTEGER://g'| sed 's/.*(//g' | sed 's/)//g'`

echo $sysname $ifname $status >> $DATE-portcheck.log


done
done

if [  -f  "$DATE-portcheck.log" ]; then
echo "file create !"
echo "---begin sync db---"
python portscan.py $DATE
echo "--end sync db---"

mv -f $DATE-portcheck.log checklog/
fi
# scan port alert off status
python alert-off.py $DATE
