# Search methods

import search

ab = search.GPSProblem('S', 'P'
                       , search.romania)

print('Búsqueda anchura')
print(search.breadth_first_graph_search(ab).path())
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('Búsqueda profundidad')
print(search.depth_first_graph_search(ab).path())
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('Rafimifación y salto')
print(search.bab(ab).path())
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('Rafimifación y salto con Subestimacion')
print(search.babSub(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
