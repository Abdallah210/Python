
"""
Sommaire :

1- key      : sorted() et sort()
2- reverse  : sorted() et sort()
3- end      : print()

"""


# 1 - key :

"""
Les outils qui acceptent des fonctions clef sont : sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(),
                                                   itertools.groupby(), list.sort(), heapq.merge()
""" 

liste = [(2, "a", 0.3),(1, "c", 0.2),(5, "b", 0.1)]

#sorted(liste)   -->  [(1, 'c', 0.2), (2, 'a', 0.3), (5, 'b', 0.1)]  comparaison du premier éléments

print(sorted(liste,key=lambda x : x[1]))


# 2 - reverse :



#3 - end :