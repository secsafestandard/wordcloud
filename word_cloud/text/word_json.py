import os
import json
import pyodbc
import json
from bson import json_util
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import *  
import time
from text.connectdb import Connect 

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
    #     
    # all_json=ConnectAccess()
    # return all_json
    py = Connect()
    all_json=py.connect_access()
    # all_json=ConnectAccess()

    return all_json

def filter_json(typye):

    # with open(path+'word_cloud/json/all.json','rb') as f:
    #     all_json = json.load(f)
    filterQuery=''

    if typye=="1" :
        filterQuery ='SELECT * FROM 0505 WHERE 测试流水线 = \'1\''
    elif typye=="installed":
        filterQuery ='SELECT * FROM 0505 WHERE 是否可安装 = \'是\' or 是否可安装 = \'否\''
    elif typye=="executed":
        filterQuery ='SELECT * FROM 0505 WHERE 是否可安装 = \'是\' and 是否可安装 = \'是\''
    print(filterQuery)
    DBfile = r"C:\Users\weihong\Documents\test\0505_0518.accdb"  # 数据库文件 ";Uid=;Pwd=;"
    py = Connect(filterQuery,DBfile)
    all_json=py.connect_access()
    # all_json=ConnectAccess()

    return all_json

# DBfile = r"C:\Users\weihong\Documents\test\0505_0518.accdb"  # 数据库文件 ";Uid=;Pwd=;"
# tablename = "0505"
# query ='select * from %s' % tablename


isnotInstalledButTriedQuery ='SELECT * FROM 0505 WHERE 是否可安装 = \'是\' or  是否可安装 = \'否\''


# def ConnectAccess():
#     conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile )
#     cursor = conn.cursor()
#     # SQL = "SELECT * from table1;"
#     SQL = isInstalledQuery
#     count = 0
#     data = []
#     for row in cursor.execute(SQL):
#         tmpList = [
#             str(row.ID),
#             str(row.应用来源),
#             str(row.应用一级类别),
#             str(row.应用二级类别),
#             str(row.应用全称),
#             str(row.应用名称),
#             str(row.版本号),
#             str(row.是否可安装),
#             str(row.是否可运行),
#             str(row.测试流水线),
#             str(row.测试人),
#             str(row.备注信息),
#             row.最后更新时间.strftime("%Y-%m-%d %H:%M:%S"),
#         ]
#         data.append(tmpList)

#     cursor.close()
#     conn.close()
#     retDict ={
#         "data":data,
#         "columns": [
#             "ID", 
#             "应用来源", 
#             "应用一级类别", 
#             "应用二级类别", 
#             "应用全称", 
#             "应用名称", 
#             "版本号", 
#             "是否可安装", 
#             "是否可运行", 
#             "测试流水线", 
#             "测试人", 
#             "备注信息", 
#             "最后更新时间"
#         ]
#     }
#     return retDict