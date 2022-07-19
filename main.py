class Tree:
    def __init__(self):
        self.Nodes = []
        self.root = None
        self.open = []
        self.closed = []

    def add(self, node):
        if self.root is None:
            self.root = node
            self.open.insert(0, self.root)
        self.Nodes.append(node)

    def print_open(self):
        arr = []
        for node in self.open:
            arr.append(node.letter)

        print('Open: ', arr)
        arr = []

    def print_closed(self):
        arr = []
        for node in self.closed:
            arr.append(node.letter)

        print('Closed: ', arr)
        arr = []

    def depth_first_search(self, curr_node, goal):

        self.print_open()
        self.print_closed()

        if curr_node.right is not None:
            self.open.insert(0, curr_node.right)

        if curr_node.left is not None:
            # add to the front of the list
            self.open.insert(0, curr_node.left)

        self.open.remove(curr_node)
        self.closed.insert(0, curr_node)

        if curr_node.letter is goal:
            print(goal, 'was found')
            exit()

        if curr_node.left is not None:
            self.depth_first_search(curr_node.left, goal)

        if curr_node.right is not None:
            self.depth_first_search(curr_node.right, goal)

    def breadth_first_search(self, curr_node, goal):

        self.print_open()
        self.print_closed()

        if curr_node.left is not None:
            # add to the front of the list
            self.open.append(curr_node.left)

        if curr_node.right is not None:
            self.open.append(curr_node.right)

        self.open.remove(curr_node)
        self.closed.insert(0,curr_node)

        if curr_node.letter is goal:
            print(goal, 'was found')
            exit()

        for x in self.open:
            self.breadth_first_search(x, goal)



def make_tree():
    t1 = Tree()
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G1 = Node('G1')
    H = Node('H')
    I = Node('I')
    J = Node('J')
    K = Node('K')
    L = Node('L')
    M = Node('M')
    N = Node('N')
    G2 = Node('G2')

    A.set_values(None, B, C)
    B.set_values(A, D, E)
    C.set_values(A, F, H)
    D.set_values(B, I, J)
    E.set_values(B, G1, K)
    F.set_values(C, L, M)
    G1.set_values(E, None, None)
    H.set_values(C, N, G2)
    I.set_values(D, None, None)
    J.set_values(D, None, None)
    K.set_values(E, None, None)
    L.set_values(F, None, None)
    M.set_values(F, None, None)
    N.set_values(H, None, None)
    G2.set_values(H, None, None)

    t1.add(A)
    t1.add(B)
    t1.add(C)
    t1.add(D)
    t1.add(E)
    t1.add(F)
    t1.add(G1)
    t1.add(H)
    t1.add(I)
    t1.add(J)
    t1.add(K)
    t1.add(L)
    t1.add(M)
    t1.add(N)
    t1.add(G2)

    return t1


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.parent = None
        self.left = None
        self.right = None

    def set_values(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


tree = make_tree()
tree.breadth_first_search(tree.root, 'F')
