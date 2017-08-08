#!/usr/bin/env python
#edit: wenyang
#
# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/python
import MySQLdb
import time
import sys
ISOTIMEFORMAT='%Y-%m-%d'
today = time.strftime(ISOTIMEFORMAT,time.localtime())





def update_portstatus(hostname,itemname,portstatus,db_ip,db_user,db_pass):


    db = MySQLdb.connect(db_ip,db_user,db_pass,"enigma")
    cursor = db.cursor()

    sql = "update alert_rule set Portstatus='"+portstatus+"' where Hostname='"+hostname+"' and Itemname='"+itemname+"'"

  #  sql=sql_base+sql_body
    try:

        results = cursor.execute(sql)
        #cursor.execute(sql)
    #results = cursor.fetchall()
        if results:
            return results
        else:
            return False
    except:
        print "Error: unable to fecth data"
    db.close()

def update_portbase(hostname,itemname,baseportstatus,db_ip,db_user,db_pass):

    db = MySQLdb.connect(db_ip,db_user,db_pass,"enigma")
    cursor = db.cursor()

    sql = "update alert_rule set Baseportstatus='"+baseportstatus+"' where Hostname='"+hostname+"' and Itemname='"+itemname+"'"

  #  sql=sql_base+sql_body
    try:

        results = cursor.execute(sql)
        #cursor.execute(sql)
    #results = cursor.fetchall()
        if results:
            return results
        else:
            return False
    except:
        print "Error: unable to fecth data"
    db.close()

def update_portstatus(hostname,itemname,portstatus,db_ip,db_user,db_pass):


    db = MySQLdb.connect(db_ip,db_user,db_pass,"enigma")
    cursor = db.cursor()

    sql = "update alert_rule set Portstatus='"+portstatus+"' where Hostname='"+hostname+"' and Itemname='"+itemname+"'"

  #  sql=sql_base+sql_body
    try:

        results = cursor.execute(sql)
        #cursor.execute(sql)
    #results = cursor.fetchall()
        if results:
            return results
        else:
            return False
    except:
        print "Error: unable to fecth data"
    db.close()


def get_status(hostname,db_ip,db_user,db_pass):


    db = MySQLdb.connect(db_ip,db_user,db_pass,"enigma")
    cursor = db.cursor()

    sql = "select Hostname,Itemname,Portstatus,Portdesc from  alert_rule  where Hostname='"+hostname+"'"

  #  sql=sql_base+sql_body
    try:

        #results = cursor.execute(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            return results
        else:
            return False
    except:
        print "Error: unable to fecth data"
    db.close()


def update_alert(hostname,itemname,alertoff,db_ip,db_user,db_pass):


    db = MySQLdb.connect(db_ip,db_user,db_pass,"enigma")
    cursor = db.cursor()

    sql = "update  alert_rule set Alertoff='"+alertoff+"' where Hostname='"+hostname+"' and Itemname='"+itemname+"'"

  #  sql=sql_base+sql_body
    try:

        results = cursor.execute(sql)
        #cursor.execute(sql)
    #results = cursor.fetchall()
        if results:
            return results
        else:
            return False
    except:
        print "Error: unable to fecth data"
    db.close()
