Aim: Implementation of travelling sales man problem

Program:
from sys import maxsize
from itertools import permutations
v=4
def travellingsalesmanproblem(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
        if min_path>current_pathweight:
            min_path=current_pathweight
        path1=i
    print(path1)
    return min_path
if __name__=="__main__":
    graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    s=0
    print(travellingsalesmanproblem(graph,s))  
    
Output:
(3, 2, 1)
80   
