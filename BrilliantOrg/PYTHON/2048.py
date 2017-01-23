from urllib.request import urlopen

# class Graph():
#     def __init__(self, width, V = set())
#         self.width = width
#         self.adj = {}
#         for L in V:
#             x, y = L[0]
#             value = L[1]
#             v = x*self.width + y
#             self.adj[v] = [value,set()] # [value, neighbours]
#             reachable = (v+self.width, v+self.width+1,v+self.width-1,v-self.width,v-self.width-1,v-self.width+1,v+1,v-1)
#             for w in reachable:
#                 if w in self.adj:
#                     self.adj[w][1].add(v)
#                     self.adj[v][1].add(w)
#     def L(self):
#         for v in self.adj.keys():
#             x, y = divmod(v, self.width)
#             if x > 1:
#                 if v-self.width in self.adj:
#                     if self.adj[v-self.width][0] == self.adj[v][0]:
#                         self
                    
            
class Graph():
    def __init__(self, M):
        self.width = len(M)
        self.adj = M

    def shift(self, letter):
        letter = letter.decode("utf-8")
            
        if letter == 'L':
            for x in range(self.width):
                previous_y = 0
                for y in range(1, self.width):
                    if self.adj[x][y] == 0:
                        continue
                    if bool(self.adj[x][previous_y]) and self.adj[x][previous_y] == self.adj[x][y]:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        self.adj[x][previous_y] = 2*v
                    else:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        if self.adj[x][previous_y] == 0:
                            self.adj[x][previous_y] = v
                        else:
                            self.adj[x][previous_y+1] = v
                    previous_y +=1
                    
        elif letter == 'R':
            for x in range(self.width):
                previous_y = -1
                for y in range(self.width-2, -1, -1):
                    if self.adj[x][y] == 0:
                        continue
                    if bool(self.adj[x][previous_y]) and self.adj[x][previous_y] == self.adj[x][y]:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        self.adj[x][previous_y] = 2*v
                    else:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        if self.adj[x][previous_y] == 0:
                            self.adj[x][previous_y] = v
                        else:
                            self.adj[x][previous_y-1] = v
                    previous_y -=1
                    
        elif letter == 'U':
            for y in range(self.width):
                previous_x = 0
                for x in range(1,self.width):
                    if self.adj[x][y] == 0:
                        continue
                    if bool(self.adj[previous_x][y]) and self.adj[previous_x][y] == self.adj[x][y]:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        self.adj[previous_x][y] = 2*v
                    else:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        if self.adj[previous_x][y] == 0:
                            self.adj[previous_x][y] = v
                        else:
                            self.adj[previous_x+1][y] = v
                    previous_x+=1
                
        elif letter == 'D':
            for y in range(self.width):
                previous_x = -1
                for x in range(self.width-2, -1, -1):
                    if self.adj[x][y] == 0:
                        continue
                    if bool(self.adj[previous_x][y]) and self.adj[previous_x][y] == self.adj[x][y]:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        self.adj[previous_x][y] = 2*v
                    else:
                        v = int(self.adj[x][y])
                        self.adj[x][y] = 0
                        if self.adj[previous_x][y] == 0:
                            self.adj[previous_x][y] = v
                        else:
                            self.adj[previous_x-1][y] = v
                    previous_x-=1
        else:
            raise ValueError

G = Graph([[0,0,2,4],[0,0,4,8],[0,2,16,32],[0,2,2,16]])

with urlopen("http://pastebin.com/raw/rcCVvfWS") as f:
    i = 1
    for line in f:
        command = line.strip().split()
        if len(command) > 1:
            G.adj[int(command[1])-1][int(command[2])-1]=int(command[3])
        elif len(command)==1:
            print(i)
            G.shift(command[0])
        i+=1
    print(G.adj, sum([i for sublist in G.adj for i in sublist])) 
                