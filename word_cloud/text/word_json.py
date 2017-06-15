import os
import json
import pyodbc
import json
from bson import json_util
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import *  
import time

path='E:/GitDir/work/wordcloud/'

def wordcloud_json():

    with open(path+'word_cloud/json/wordWeightRelatedtext.json','rb') as f:
        words = json.load(f)
    return json.dumps(words)

def table_json(keyword):
    with open(path+'word_cloud/json/jsondata/'+keyword.replace(':', '-')+'.json','rb') as f:
        table = json.load(f)
    return table

def all_json():

    # with open(path+'word_cloud/json/all.json','rb') as f:
    #     all_json = json.load(f)
    all_json=ConnectAccess()

    return all_json

DBfile = r"C:\Users\weihong\Documents\test\0505_0518.accdb"  # 数据库文件 ";Uid=;Pwd=;"
tablename = "0505"
query ='select * from %s' % tablename

isInstalledQuery ='SELECT * FROM 0505 WHERE 是否可安装 = \'是\''
isnotInstalledButTriedQuery ='SELECT * FROM 0505 WHERE 是否可安装 = \'是\' or  是否可安装 = \'否\''
def ConnectAccess():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile )
    cursor = conn.cursor()
    # SQL = "SELECT * from table1;"
    SQL = isInstalledQuery
    count = 0
    data = []
    for row in cursor.execute(SQL):
        # if(count > 1):
        #     break;
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
        # count = count +1

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