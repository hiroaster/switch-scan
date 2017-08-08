#!/usr/bin/env python
#edit: wenyang
#
#coding:utf-8
import os
import json
import sys
import ConfigParser
from dbconn import get_status,update_alert
from alertsend import smsSend,mailSend


def main():

    #define a list for store msg
    a=[]

    #read db config file
    cf = ConfigParser.ConfigParser()
    cf.read("db.conf")
    secs = cf.sections()
    if 'db' in secs:
        db_ip = cf.get("db", "db_ip")
        db_user = cf.get("db", "db_user")
        db_pass = cf.get("db", "db_pass")

    else:
        sys.exit()

#determine if the new port-status changed,if changed update db.
    filedate = sys.argv[1]
    filename = "swlist.txt"
    info=open(filename,'r').readlines()
    for line in info:
        try:
            hostname= line.split()[2]

        except:
            continue
        else:
            res = get_status(hostname,db_ip,db_user,db_pass)
        if res:           
            for i in range(len(res)):
                host = res[i][0]  
                item = res[i][1] 
                stats =  res[i][2]    
                desc = res[i][3]
                if stats == '1':
                    if 'server' not in desc  and  'ignore' not in desc:
                        alert = '0'
                    else:
                        alert = '1'
                        
                else:
                    alert = '1'
                
                rest = update_alert(host,item,alert,db_ip,db_user,db_pass)
                if rest:
                    msg = '{"hostname":'+host+',"itemname":'+item+',"portstatus":'+stats+',"alertoff":'+alert+'}'
                    a.append(msg)
    
    mail_subject = "[Alert-autopilot]FS-IDC port_alert change log--"+filedate
    mailSend(mail_subject,str(a))
                    
                





if __name__ == "__main__":
    main()
