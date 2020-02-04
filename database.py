#from PyQt4 import QtSql,QtGui
import sqlite3

connection = sqlite3.connect("pulp.db")

def create_db():
    db = connection.cursor()
    db.execute("create table if not exists working_days(days varchar(20))")
    db.execute("create table if not exists missing_sku(id integer primary key autoincrement,sku_name varchar(20))")
    db.execute("create table if not exists tenative_schedule(date varchar(20),depos varchar(100))")
    db.execute("create table if not exists sku_tab(sku_code varchar(8) primary key,blend_code varchar(20) not null ,sku_desc varchar(50) not null,packet_size decimal ,case_size decimal,gross_wt decimal ,net_wt decimal,box_vol decimal)")
   # db.execute("create table if not exists machines(id int primary key,mac_code varchar(10),sku_code varchar(8),rate_hr decimal,case_shift int)")
    db.execute("create table if not exists skudimpath(id int primary key,path varchar(200))")
   # db.execute("drop table machines")
    db.execute("create table if not exists mach_hopper_path(int id primary key,path varchar(500))")
    db.execute("create table if not exists machines(machine_id varchar(4),sku_code varchar(8),rate_hr decimal,case_shift int)")
    db.close()

def insert_into_work(data):
    db = connection.cursor()
    for i in data:
        db.execute("insert into working_days values(?)",[i])
    connection.commit()    
    db.close()

def insert_into_mach_hopper_path():
    pass

def select_date_from_table(tablename):
    db = connection.cursor()
    res = db.execute("select days from "+tablename)
    return res 
    db.close()


def drop_machines():
    db = connection.cursor()
    db.execute("delete from machines")
    connection.commit()
    db.close()

def insert_into_machines(data1,data2,data3,data4):
    db = connection.cursor()
    db.execute("insert into machines values(?,?,?,?)",[data1,data2,data3,data4])
    connection.commit()
    db.close()

def delete_dates_from_table(data):
    db = connection.cursor()
    db.execute("delete from working_days where days=?",(data,))
    connection.commit()
    db.close()

def insert_into_tenative(data):
    db = connection.cursor()
    db.execute("insert into tenative_schedule values(?,?)",[data[0],data[1]])
    connection.commit()
    db.close()

def delete_from_tenative():
    db = connection.cursor()
    db.execute("delete from tenative_schedule")
    connection.commit()
    db.close()

def select_from_tenative():
    db = connection.cursor()
    res = db.execute("select * from tenative_schedule")
    return res
    db.close()


def insert_into_skudim(data):
    db = connection.cursor()
    res = select_from_skudimpath()
    isvail=0
    for i in res:
        isvail+=1
    if(isvail==0):
        db.execute("insert into skudimpath values(?,?)",[1,data])
    else:
        db.execute("update skudimpath set path = ? where id=1",[data])
    connection.commit()
    db.close()

def select_from_skudimpath():
    db = connection.cursor()
    res = db.execute("select * from skudimpath")
    return res
    db.close()

def insert_into_missing_sku(data):
    db = connection.cursor()
    for i in data:
        db.execute("insert into missing_sku(sku_name) values(?)",[i])
    connection.commit()
    db.close()

def select_from_missing_sku():
    db = connection.cursor()
    res = db.execute("select sku_name from missing_sku")
    return res
    db.close()

def delete_missing_sku(data):
    db = connection.cursor()
    for i in data:
        db.execute("delete from missing_sku where sku_name = ?",(i,))
    connection.commit()
    db.close()


create_db()

#a=select_date_from_table("working_days")
#insert_into_work(['2019-10-19'])
