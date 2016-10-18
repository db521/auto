#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.3.182","root","daodao@test","daodao-cp" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()


#待执行的sql语句
sql = """select phone from cp_user;"""
try:
   # 使用execute方法执行SQL语句
   cursor.execute(sql)
   #使用fetchall获取所有结果
   results = cursor.fetchall()
   for x in results:
       print x
   #如果需要编辑数据，需要执行commit，提交到数据库执行
   # db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()