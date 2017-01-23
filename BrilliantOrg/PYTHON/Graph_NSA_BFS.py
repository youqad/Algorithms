import urllib.request
class Graph():
    def __init__(self, file):
        self.adj = {}
        with urllib.request.urlopen(file) as f:
            next(f)
            for line in f:
                    edge = [int(i) for i in line.split()]            
                    if edge[1] in self.adj:
                        self.adj[edge[1]].add(edge[0])
                    else:
                        self.adj[edge[1]]={edge[0]}
                    if edge[0] in self.adj:
                        self.adj[edge[0]].add(edge[1])
                    else:
                        self.adj[edge[0]]={edge[1]}
    def count(self, List, counters = []):
        if not List:
            return counters, sum(counters)/len(counters)
        counter=-1
        stack = [(List.pop(),0)] # (vertice, proximity to the original one)
        already_seen = set()
        while stack:
            v = stack.pop()
            if v[0] in already_seen or v[1] > 3:
                continue
            counter += 1
            already_seen.add(v[0])
            if v[0] in self.adj:
                for w in self.adj[v[0]]:
                    stack.append((w,v[1]+1))
        counters.append(counter)
        return self.count(List,counters)

G = Graph('https://d18l82el6cdm1i.cloudfront.net/uploads/documents/2015_march_calls-ebAECyfYVJ.txt')
print(G.count([1 , 17, 793, 1200, 3402]))

            
        
            
            
                