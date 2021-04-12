#Incomplete
#Problem. Solce maze with input x, you can remove 1 wall. Find the fastest distance and return it
#EX:  
#[0, 1, 1, 0], 
#[0, 0, 0, 1], 
#[1, 1, 0, 0], 
#[1, 1, 1, 0]
#Output: 7


class Node:
    def __init__(self, dist, val, x ,y, count):
        self.dist = dist
        self.val = val
        self.x = x
        self.y = y
        self.processed = False
        self.num = count
        
    def updateVal(self, nVal):
      self.val = nVal

    def updateDist(self, nDist):
      self.dist = nDist
    
    def process(self):
      self.processed = True
            
def solutionOld(map):
    width = len(map[0])
    nodesO= []
    mapC = [item for sublist in map for item in sublist]
    fastest = float('inf')
    fastestN = []
    nodesO.append(Node(0,1))
    del mapC[0]
    for i in range(len(mapC)):
        node = Node(1 + (mapC[i] * 999) , float('inf'))
        nodesO.append(node)
    for wall in range(len(nodesO)):
      x = wall
      nodes = []
      for node in nodesO:
          nodes.append(Node(node.dist, node.val))
      if nodes[wall].dist == 1000:
        nodes[wall].updateDist(1)
      for i in range(len(nodes)):
          node = nodes[i] 
          u = i - width if i - width in range(0, len(nodes)) else False
          r = i + 1 if i + 1 in range(0, len(nodes)) else False
          l = i - 1 if i - 1 in range(0, len(nodes)) else False
          d = i + width if i + width in range(0, len(nodes)) else False
          if r and nodes[r].val > node.val + nodes[r].dist:
              nodes[r].updateVal(nodes[r].dist + node.val)
          if d and nodes[d].val > node.val + nodes[d].dist:
              nodes[d].updateVal(nodes[d].dist +  node.val)
          if l and nodes[l].val > node.val + nodes[l].dist:
              nodes[l].updateVal(nodes[l].dist +  node.val)
          if u and nodes[u].val > node.val + nodes[u].dist:
              nodes[u].updateVal(nodes[u].dist +  node.val)
      if nodes[len(nodes) - 1].val < fastest:
          print(wall)
          fastest = nodes[len(nodes) - 1].val
          fastestN = nodes
    fList = []
    i = 0
    for x in range(len(map)):
      toadd = []
      for y in range(width):
        toadd.append(fastestN[i].val)
        i += 1
      fList.append(toadd)
    print(fList)
    print(fastest)
    return fastest

#-------------------------------------------------------------
#Implementation using djiktra's algo. Does not currently function
def deepCopy(input):
  return [x for x in input]

def copyList(input):
  output = []
  for row in input:
    output.append(deepCopy(row))
  return output

def solution(map):
  fastest = float('inf')
  mapM = copyList(map)
  output = Dijkstra(mapM)
  if output < fastest:
    fastest = output
  for r, row in enumerate(mapM):
    for i, cell in enumerate(row):
      if cell == 1:
        mapC = copyList(mapM)
        mapC[r][i] = 0
        output = Dijkstra(mapC)
        if output < fastest:
          fastest = output
  return fastest

def Dijkstra(map):
  #assemble array of nodes
  nodes = []
  firstD = False
  made = 1
  for y in range(len(map)):
    toadd = []
    for x in range(len(map[y])):
      nodeO = None
      if not firstD:
        nodeO = Node(1,1,x,y, made)
        firstD = True
      else:
        nodeO = Node(1 + (map[y][x] * 999) , float('inf'),x,y, made)
      made += 1
      toadd.append(nodeO)
    nodes.append(toadd)
  visited = []
  notVisited = [item for sublist in nodes for item in sublist]
  current = nodes[0][0]
  while len(notVisited) > 0:
    nNodes = nearby(nodes, current)
    if nNodes == []:
      break
    for node in nNodes:
      node.updateVal(node.dist + current.val)
    sortedNodes = sorted(nNodes, key=lambda x: x.val)
    visited.append(current)
    index = notVisited.index(current)
    del notVisited[index]
    current.process()
    current = sortedNodes[0]
  return nodes[len(map)-1][len(map[0]) - 1].val
    
def nearby(map, node):
  output = []
  width = len(map[0])
  height = len(map)
  #Check above
  if node.y - 1 >= 0 and not map[node.y - 1][node.x].processed:
    output.append(map[node.y - 1][node.x])
    #check below
  if node.y + 1 < height and not map[node.y + 1][node.x].processed:
    output.append(map[node.y + 1][node.x])
  if node.x - 1 >= 0 and not map[node.y][node.x - 1].processed:
    output.append(map[node.y][node.x - 1])
  if node.x + 1 < width and not map[node.y][node.x + 1].processed:
    output.append(map[node.y][node.x + 1])
  return output
#print(solution([[0,0,0,0,1],[0,1,1,1,0],[0,0,0,0,0],[1,0,1,1,0],[1,0,0,0,0]]))
print("the output is ")
print("\n")
print(solution([[0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]))#[[0, 0, 0, 1, 1, 1],[0, 1, 0, 0, 0, 0],[0, 1, 1, 1, 1, 0],[0, 1, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]))
#[[0,0,0,0,1], [0,1,1,1,0],[0,0,0,0,0],[0,1,1,1,0],[0,1,1,1,0]]