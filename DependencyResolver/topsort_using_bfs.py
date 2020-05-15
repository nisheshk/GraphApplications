"""
Author: Nishesh Kalakheti
Date: May 15, 2020 
Goal: To resolve the dependency between scripts. Say I have few scripts and one script is dependent
        on others. Then, we must find a way to run the scripts in the right order such that all the
        tasks are completed. This is solved by using topological sorting of the graph, where graph is
        represented as a dicitionary(adjacency list of the scripts). The scripts are the nodes and its
        depdendencies are the edges.
"""
from collections import deque

def dependency_resolver(dependency_dic):
    #Initialize all the incoming edges to the nodes to be zero
    #This is done as it covers all the nodes (including isolated nodes)
    #O(V) time complexity, where V are the number of scripts(nodes/vertices)
    in_degree = {u:0 for u in dependency_dic}

    #Check the incoming edges to the node and increment the value of the edge
    #in the in_degree dictionary
    #O(V+E) as we are traversing through all the nodes and its edges.
    for u in dependency_dic:
        for v in dependency_dic[u]:
            in_degree[v] += 1

    Q = deque()
    #The nodes with 0 incoming edges should be precessed first
    #As they have no dependency, hence they should occur first
    #O(V); as in_degree contains all the nodes
    for nodes in in_degree:
        if in_degree[nodes] == 0:
            Q.appendleft(nodes)


    result = []

    #We remove the node with 0 degree from the queue. Hence, we must
    #reduce the edge of those nodes value by 1 which was poiting to that node
    #If that node's edge whose value we have reduced by 1 becomes 0, append to the queue
    #Because they can be processed again, as their dependency is completed.
    #O(V+E) If the graph is acyclic, we traverse through all the edges and its vertices.
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

    


#The value of the dictionary depends on the key to be completed.
#Example "e.py":set(["c.py","d.py"] means that only after e.py executes,
#We can execute c.py and d.py
scripts_depdendency  = {"a.py":set(["d.py"]),"b.py":set(["a.py"]),"c.py":set(["f.py"]),"e.py":set(["c.py","d.py"]),"d.py":set(["c.py"]),"f.py":set([])}
res = dependency_resolver(scripts_depdendency)
if res: #No cycle exists
    print (res)
else:
    print ("Cycle exists", res)
