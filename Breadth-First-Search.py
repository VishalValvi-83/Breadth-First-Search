graph = {
  '2' : ['3','6'],
  '3' : ['5', '4'],
  '6' : ['7'],  
  '5' : [],
  '4' : ['7'],
  '7' : []
}

def bfs(graph, node): #function for BFS
  if node not in graph:
        print(f"{node} not found in the graph.")
        return
  visited = [node]
  queue = [node]
  
  print("Following is the Breadth-First Search")
  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(graph, '2')  # 2 is starting node