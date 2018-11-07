"""
>>> print(dijkstra({}))
({}, {})
>>> graph = {
...     'start': {'a': 6, 'b': 2},
...     'a': {'fin': 1},
...     'b': {'a': 3, 'fin': 5},
...     'fin': {}
... }

        graph:     a
               --- | ---
           6---    |   ---1
        ---       3|     ---
    ---            |       ---
  start ----2----- b ---5--- fin

>>> costs, parents = dijkstra(graph)
>>> costs
{'start': 0, 'a': 5.0, 'b': 2.0, 'fin': 6.0}
>>> parents
{'a': 'b', 'b': 'start', 'fin': 'a'}


>>> graph1 = {
...     'start': {'a': 5, 'b': 2},
...     'a': {'c': 4, 'd': 2},
...     'b': {'a': 8, 'd': 7},
...     'c': {'d': 6, 'fin': 3},
...     'd': {'fin': 1},
...     'fin': {}
... }
>>> costs1, parents1 = dijkstra(graph1)
>>> costs1
{'start': 0, 'a': 5.0, 'b': 2.0, 'c': 9.0, 'd': 7.0, 'fin': 8.0}
>>> parents1
{'a': 'start', 'b': 'start', 'd': 'a', 'c': 'a', 'fin': 'd'}


>>> graph2 = {
...     'start': {'a': 10},
...     'a': {'c': 20},
...     'b': {'a': 1},
...     'c': {'b': 1, 'fin': 30},
...     'fin': {}
... }
>>> costs2, parents2 = dijkstra(graph2)
>>> costs2
{'start': 0, 'a': 10.0, 'b': 31.0, 'c': 30.0, 'fin': 60.0}
>>> parents2
{'a': 'start', 'c': 'a', 'b': 'c', 'fin': 'c'}


>>> graph3 = {
...     'start': {'a': 3, 'b': 4},
...     'a': {'fin': 2},
...     'b': {'a': -2, 'fin': 2},
...     'fin': {}
... }
>>> costs3, parents3 = dijkstra(graph3)
>>> costs3
{'start': 0, 'a': 2.0, 'b': 4.0, 'fin': 5.0}
>>> parents3
{'a': 'b', 'b': 'start', 'fin': 'a'}

# You should never use Dijkstra's algorithm when graph contains negative-weight(negative-cost).

# graph3 is a wrong example.
# If you follow the shortest path then you'll find the cost(from start to fin) is wrong(should be 4.0 not 5.0).

"""


def dijkstra(graph, start='start'):
    """
    Use Dijkstra's algorithm to find shortest path

    :return: costs(cost table) and parents(parents table)
    """

    parents, costs, not_used = {}, {}, []

    def initial():
        for n in graph:
            not_used.append(n)
            if n == start:
                costs[n] = 0
            else:
                costs[n] = float('inf')

    initial()

    def consume(node):
        """
        Consume the node. Add node cost and parent to costs(cost table) and parents(parents table)
        if cost less than costs(cost table)
        :param node:
        :return:
        """
        # print(node, neighborhood)
        neighborhood = graph[node]
        for n, cost in neighborhood.items():
            cost = float(cost)
            c = cost + costs[node]
            if c < costs[n]:
                costs[n] = c
                parents[n] = node
        not_used.remove(node)

    def find_shortest():
        """
        Find the shortest node in not_used_list
        :return:
        """
        min_cost, shortest_node = float('inf'), '_'
        for n in not_used:
            cost = costs[n]
            if cost < min_cost:
                min_cost = cost
                shortest_node = n
        return shortest_node

    while not_used:
        shortest = find_shortest()
        consume(shortest)

    return costs, parents


if __name__ == "__main__":
    import doctest
    doctest.testmod()

