
class Graph:
    '''This is supposed to be a graph(mathematical) class. Has only the most basic of functionalities'''
    def __init__(self):
        self.nodes = []
        self.connections = {}

    def add_node(self, node):
        assert node not in self.nodes
        self.nodes.append(node)
        self.connections[node] = []

    def add_connection(self, node1, node2):
        assert node1 in self.nodes
        assert node2 in self.nodes
        self.connections[node1].append(node2)
        self.connections[node2].append(node1)

    def remove_node(self, node):
        assert node in self.nodes
        for con in self.connections:
            con.remove(node)

        self.connections.pop(node)
        self.nodes.remove(node)


    def remove_connection(self, node1, node2):
        assert node1 in self.nodes
        assert node2 in self.nodes
        assert node1 in self.connections[node2]
        assert node2 in self.connections[node1]
        self.connections[node1].remove(node2)
        self.connections[node2].remove(node1)

if __name__ == '__main__':
    '''Some testing'''
    g = Graph()
    g.add_node(2)
    g.add_node(3)
    g.add_connection(2,3)
    g.remove_connection(3,2)
    print(g.connections)
