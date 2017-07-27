#!/usr/bin/env python
#edit: wenyang
#
#coding:utf-8
import os
import json
import sys
import ConfigParser
from dbconn import update_portstatus,update_portbase


def main():
    
    #define a list for store msg
    a=[]
    
    #read db config file
    cf = ConfigParser.ConfigParser()
    cf.read("db.conf")
    secs = cf.sections()
    if 'db' in secs:
        db_ip = cf.get("db", "ip")
        db_user = cf.get("db", "user")
        db_pass = cf.get("db", "pass")

    else:
        sys.exit()

#read today's switch port status  information       
    filedate = sys.argv[1]
    filename = filedate+"-portcheck.log"
    info=open(filename,'r').readlines()

#determine if the new port-status changed,if changed update db.    
    for line in info:
        try:
            hostname= line.split()[0]
            itemname= line.split()[1]
            portstatus= line.split()[2]

        except:
            continue
        else:
            res = update_portstatus(hostname,itemname,portstatus,db_ip,db_user,db_pass)
        if res:           # if res == 1 means port-status has changed
        if portstatus == '1': #if port status from down change to up, need modify port-status's baseline 
            portchange = 'sync_base'
            update_portbase(hostname,itemname,portstatus,db_ip,db_user,db_pass)
        elif portstatus == '2': #if port-status from up change to down, baseline no need to modify automatic by default,should be ack by NOC and modify it .
            portchange = 'no_change'
            msg = '{"hostname":'+hostname+',"itemname":'+itemname+',"portstatus":'+portstatus+',"portchange":'+portchange+'}'
            a.append(msg)
        #print "update it !"
    for i in range(len(a)):
        print a[i]




if __name__ == "__main__":
    main()
