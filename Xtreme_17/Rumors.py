from collections import defaultdict

n = int(input())
relations = []

for _ in range(n):
    relation = input().strip().split()
    relations.append(relation)


graph = defaultdict(list)
incoming_edges = defaultdict(int)

for relation in relations:
    p1, arrow, p2 = relation
    if arrow == "->":
        graph[p1].append(p2)
        incoming_edges[p2] += 1
    elif arrow == "??":
        if(relation != relations[len(relations)-1]):
            graph[p1].append(p2)
            graph[p2].append(p1)

# Find the possible sources (nodes with no incoming edges)
possible_sources = [node for node in graph if incoming_edges[node] == 0]

possible_sources.sort()

for source in possible_sources:
    print(source)