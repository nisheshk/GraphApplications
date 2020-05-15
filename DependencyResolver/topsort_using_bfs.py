"""
Author: Nishesh Kalakheti
Date: Oblivious of the date, due to COVID-19 effect.
Goal: To resolve the dependency between scripts. Say I have few scripts and one script is dependent
        on others. Then, we must find a way to run the scripts in the right order. So, I have used the
        concept of topological sorting using the degrees of the node.
"""
from collections import deque

def dependency_resolver(dependency_dic):
    #Initialize all the incoming edges to the nodes to be zero
    #This is done as it covers all the nodes (including isolated nodes)
    in_degree = {u:0 for u in dependency_dic}

    #Check the incoming edges to the node and increment the value of the edge
    #in the in_degree dictionary
    for u in dependency_dic:
        for v in dependency_dic[u]:
            in_degree[v] += 1

    #The nodes with 0 incoming edges should be precessed first
    #As they have no dependency, hence they should occur first
    Q = deque()
    for nodes in in_degree:
        if in_degree[nodes] == 0:
            Q.appendleft(nodes)


    result = []

    #We remove the node with 0 degree from the queue. Hence, we must
    #reduce the edge of those nodes value by 1 which was poiting to that node
    #If that node's edge whose value we have reduced by 1 becomes 0, append to the queue
    #Because they can be processed again, as their dependency is completed.
    while Q:
        u = Q.pop()
        result.append(u)
        for v in dependency_dic[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)

    #Eventually if all the dependencies are removed, then all the nodes should be
    #the part of the result. Else there is a cycle
    if len(result) == len(dependency_dic):
        return result
    return []   #Cycle

    



dependency_resolver  = {"a.py":set(["d.py"]),"b.py":set(["a.py"]),"c.py":set(["f.py"]),"e.py":set(["c.py","d.py"]),"d.py":set(["c.py"]),"f.py":set([])}
res = topsort(dependency_resolver)
if res: #No cycle exists
    print (res)
else:
    print ("Cycle exists", res)
