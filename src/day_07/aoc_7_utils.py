import igraph as ig


def read_data_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            rules = {}
            for word in [data.strip().split() for data in f.readlines()]:
                i = 4
                outer = word[0] + word[1]
                inner = {}
                while True:
                    if i >= len(word) or word[i] == 'no':
                        break
                    inner[word[i+1] + word[i+2]] = int(word[i])
                    i += 4
                rules[outer] = inner
            return rules
    except OSError as identifier:
        return []


def generate_bags_graph(rules) -> ig.Graph:
    rules_graph = ig.Graph(directed=True)
    for outer, inner in rules.items():
        for inner_elem, count in inner.items():
            rules_graph.add_vertex(inner_elem)
            rules_graph.add_vertex(outer)
            rules_graph.add_edge(outer, inner_elem, contains=count)
    return rules_graph


def count_bags(vertex: ig.Vertex):
    return 1 + sum(edge['contains'] * count_bags(edge.target_vertex) for edge in list(vertex.out_edges()))
