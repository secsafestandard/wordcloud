# -*- coding: utf-8 -*-
import pyodbc
import json
from bson import json_util
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import *  
import time

def display():
    py = Connect('SELECT * FROM 0505 WHERE 是否可安装 = \'是\'')
    py.connect_access()

class Connect:
    def __init__(self,query='select * from 0505',DBfile=r"C:\Users\weihong\Documents\test\0505_0518.accdb"):
        # self.tablename = '0505'
        # self.query ='select * from %s' % self.tablename
        self.query =query
        self.DBfile =  DBfile# 数据库文件 ";Uid=;Pwd=;"

    def connect_access(self):
        print("connect_access")
        print(self.query)
        print(self.DBfile)
        conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + self.DBfile )
        cursor = conn.cursor()
        # SQL = "SELECT * from table1;"
        SQL = self.query
        print(SQL)
        count = 0
        data = []
        for row in cursor.execute(SQL):
            if(count > 20):
                break;
            count = count + 1
            # print (row.最后更新时间)
            # print (type(row.最后更新时间))
            tmpList = [
                str(row.ID),
                str(row.应用来源),
                str(row.应用一级类别),
                str(row.应用二级类别),
                str(row.应用全称),
                str(row.应用名称),
                str(row.版本号),
                str(row.是否可安装),
                str(row.是否可运行),
                str(row.测试流水线),
                str(row.测试人),
                str(row.备注信息),
                row.最后更新时间.strftime("%Y-%m-%d %H:%M:%S"),
            ]
            data.append(tmpList)
            # print(tmpJson)
        cursor.close()
        conn.close()
        # print (type(data))
        retDict ={
            "data":data,
            "columns": [
                "ID", 
                "应用来源", 
                "应用一级类别", 
                "应用二级类别", 
                "应用全称", 
                "应用名称", 
                "版本号", 
                "是否可安装", 
                "是否可运行", 
                "测试流水线", 
                "测试人", 
                "备注信息", 
                "最后更新时间"
            ]
        }
        print(retDict)
        return retDict

if __name__ == '__main__':
    py = Connect('SELECT * FROM 0505 WHERE 应用来源 = \'多特\'')
    py.connect_access()



def ConnectAccess(self):
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + self.DBfile )
    cursor = conn.cursor()
    # SQL = "SELECT * from table1;"
    SQL = self.query
    count = 0
    data = []
    for row in cursor.execute(SQL):
        if(count > 1):
            break;
        # print (row.最后更新时间)
        # print (type(row.最后更新时间))
        tmpList = [
            row.ID,
            row.应用来源,
            row.应用一级类别,
            row.应用二级类别,
            row.应用全称,
            row.版本号,
            row.是否可安装,
            row.是否可运行,
            row.测试流水线,
            row.测试人,
            row.备注信息,
            str(row.最后更新时间),
        ]
        data.append(tmpList)
        # print(tmpJson)
    cursor.close()
    conn.close()
    # print (type(data))
    retDict ={
        "data":data,
        "columns": [
            "ID", 
            "应用来源", 
            "应用一级类别", 
            "应用二级类别", 
            "应用全称", 
            "应用名称", 
            "版本号", 
            "是否可安装", 
            "是否可运行", 
            "测试流水线", 
            "测试人", 
            "备注信息", 
            "最后更新时间"
        ]
    }
    # tmpJson = json.dumps(data, default=json_util.default)
    # out = json.loads(tmpJson, object_hook=json_util.object_hook)
    # print(retDict)
    # print(type(out))
    # return HttpResponse(out)
    return retDict
