from collections import deque
def isBipartite(graph):
    # can create a rep using an 
    # adjacency list 
    aj_list = {i: graph[i] for i in range(len(graph))}

    # Now we can run bfs and check if values in the same 
    # layer are connected, thus returning true if the case 
    # otherwise continue until false 
    visited, queue = set(),deque[list(aj_list)[0]]
    while queue:
        vertex = queue.popleft()
        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
            else:
               return False 
    return True

print(isBipartite([[1,3], [0,2], [1,3], [0,2]]))