# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from text.word_json import wordcloud_json, table_json, all_json,filter_json

def index(request):
    clouds = wordcloud_json()
    alltable = all_json()
    # print(alltable)
    return render(request, 'words/index.html', {'clouds': clouds, 'alltable': alltable})

def ajax_table(request):
    keyword = request.GET['keyword']

    #print('keyword')
    table = table_json(keyword)
    return JsonResponse(table, safe=False)

def ajax_select_table(request):
    clouds = wordcloud_json()
    # print(request)
    filterQuery = request.GET['filterQuery']
    # print("filterQuery")
    # print(filterQuery)
    filtertable = filter_json(filterQuery)
    return JsonResponse(filtertable, safe=False)
