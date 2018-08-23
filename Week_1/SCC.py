#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import sys

start = time.time()
print datetime.datetime.now()

with open('SCC.txt') as f:
    #a = [[int(x) for x in ln.split()] for ln in f]
    data_set_u = []
    data_set_v = []
    for ln in f:
        if len(ln) >1:
            u,v = ln.split()
            u = int(u)
            v = int(v)            
            data_set_u.append(u)
            data_set_v.append(v)
f.close()

print 'Open file time: '+ str(time.time() - start) + 's'
print datetime.datetime.now()
    
sys.setrecursionlimit((max(data_set_u+data_set_v)+ len(data_set_u))*100)

def DFS_Loop():
    num = max(data_set_u+data_set_v)
    
    start_time_DFS_Loop = time.time()
    global t
    t = 0
    global s
    s = None
    global visited
    visited = [False]* num
    global leader
    leader = [None] * num
    global f
    f = [None] * num
    
    
    for i in range(num,0,-1):
        if visited[i-1] == False:
            s = i
            DFS(i)
    print 'End with func DFS_Loop() time: '+ str(time.time() - start_time_DFS_Loop)+ 's'
    print 'End with func DFS_Loop() whole time: '+ str(time.time() - start)+ 's'    
# For debug
#print data_set_u
#print data_set_v
    
            
def DFS(node):
    start_time_DFS = time.time()
    
    global t
    visited[node-1] = True
    #print visited
    #print visited
    leader[node-1] = s
    #print leader
    arc = []
    arc = [data_set_v[i] for i,x in enumerate(data_set_u) if x==node] 
    #print arc
    for i in arc:
        if visited[i-1]==0:
            DFS(i)

    t+=1
    f[node-1] = t
    print 'End with func DFS time: '+ str(time.time() - start_time_DFS)+ 's'
    print 'End with func DFS whole time: '+ str(time.time() - start)+ 's'
    
DFS_Loop()
print 'DFS_Loop time: '+ str(time.time() - start)+ 's'


##reverse tail and head data

rev_u,rev_v = data_set_v,data_set_u
new_u = [None] * (len(rev_u))
new_v = [None] * (len(rev_v))

for i,val in enumerate(f):
    for i_v,val_v in enumerate(rev_v):
        if val_v == i+1:
            new_v[i_v] = val
    
    for i_u,val_u in enumerate(rev_u):
        if val_u == i+1:
            new_u[i_u] = val    
    
data_set_u = new_u
data_set_v = new_v

print 'Reverse data time: '+ str(time.time() - start)+ 's'

DFS_Loop()
print 'DFS_Loop time: '+ str(time.time() - start)+ 's'

# Print leader
# Calculate repeated times appearancing in leader list

count_list = [0]*len(leader)
indices = [0]*len(leader)

i_count_list = 0
while len(leader) > 0:
    count_list[i_count_list] = leader.count(leader[0])
    indices = [i for i, x in enumerate(leader) if x == leader[0]]

    for i in xrange(len(indices)):
        del leader[leader.index(leader[0])]
    i_count_list = i_count_list+1
print 'calc time: '+ str(time.time() - start)+ 's'

sorted_count_list = sorted(count_list, key=int, reverse=True)
print '5 largest SCC sizes are:'
print sorted_count_list[0:5]
print datetime.datetime.now()
