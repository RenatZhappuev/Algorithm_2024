class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearch:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def one_child(self):
        return sorted(self._one_child(self.root))

    def _one_child(self, node):
        if node is None:
            return []
        nodes = []
        if (node.left is None and node.right is not None) \
                or (node.left is not None and node.right is None):
            nodes.append(node.val)
        nodes.extend(self._one_child(node.left))
        nodes.extend(self._one_child(node.right))
        return nodes


numbers = list(map(int, input().split()))

tree = BinarySearch()
for num in numbers:
    if num == 0:
        break
    tree.insert(num)

nodes = tree.one_child()
print(' '.join(map(str, nodes)))
