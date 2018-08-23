#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('dijkstraData.txt') as f:
    data = []
    list_data = []
    node_list = []
    u = []
    v = []
    data_u = []
    data_v = []
    dict_nested = {}
    list_nested = []
    for ln in f:
        if len(ln) >1:
            data = ln.split()
            list_data.append(data)           

    for i in range(len(list_data)):
        node_list.append(i+1)
        del list_data[i][0]
        
        for j in range(len(list_data[i])):
            u,v = list_data[i][j].split(',')            
            data_u.append(int(u))
            data_v.append(int(v))
        list_nested.append(dict(zip(data_u,data_v)))
        data_u,data_v = [],[]    
    dict_nested = dict(zip(node_list,list_nested))
    
f.close()

def dijkstra():
    scores = []
    V = node_list
    X = [1]
    A = {}
    A[1] = 0
    data_v = []
    data_w = []
    
    while X != V:
        for v in X:
            for w in dict_nested[v].keys():
                if w not in A:
                    data_v.append(v)
                    data_w.append(w)
                    scores.append(A[v] + dict_nested[v][w])
        find_w = 0
        find_w = data_w[scores.index(min(scores))]
        X.append(find_w)
        A[find_w] = min(scores)
        X.sort()
        scores = []
        data_v = []
        data_w = []                   
    tmp = []
    for keys in [7,37,59,82,99,115,133,165,188,197]:
        tmp.append(A[keys])
    print tmp



dijkstra()

