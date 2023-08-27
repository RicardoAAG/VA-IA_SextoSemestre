graph = {
'a':{'b':2, 'f':1},
'b':{'a':2, 'c':2, 'd':2},
'c':{'b':2, 'e':3, 'z':1},
'd':{'b':2, 'e':4, 'f':3},
'e':{'c':3, 'd':4, 'g':7},
'f':{'a':1, 'd':3, 'g':5},
'g':{'e':7, 'f':5, 'z':6},
'z':{'c':1, 'g':6}
}

def dijikstra (graph, start, goal):
    
     shortest_distance = {}
     track_predecessor = {}
     unseenNodes = graph
     infinity = 9999999
     track_path =[]
     
     for node in unseenNodes:
         shortest_distance[node] = infinity
     shortest_distance[start] = 0
     
     while unseenNodes: 
         min_distance_node = None
         for node in unseenNodes:
             print(node)
             if min_distance_node is None:
                 min_distance_node = node
             if shortest_distance[node] <= shortest_distance[min_distance_node]:
                 min_distance_node = node
         path_options = graph[min_distance_node].items()
         
         for child_node, weight in path_options:
             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                 shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                 track_predecessor[child_node] = min_distance_node
         unseenNodes.pop(min_distance_node)        
     currentNode = goal

     while currentNode != start:         
         try:
             track_path.insert(0, currentNode)
             currentNode =track_predecessor[currentNode]
         except KeyError:
             print("Path is not reachable")
             
     track_path.insert(0,start)
     
     if shortest_distance[goal] != infinity:
         print("Shortest distance is " + str(shortest_distance[goal]))
         print("Optimal path is " + str(track_path))
         
         
dijikstra(graph, 'a', 'z')