class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearch:
    def __init__(self):
        self.root = None

    def ins(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._ins(self.root, key)

    def _ins(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._ins(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._ins(node.right, key)

    def balance(self):
        return self._balance(self.root) is not None

    def _balance(self, node):
        if node is None:
            return 0

        left_height = self._balance(node.left)
        if left_height is None:
            return None

        right_height = self._balance(node.right)
        if right_height is None:
            return None

        if abs(left_height - right_height) > 1:
            return None

        return max(left_height, right_height) + 1


numbers = list(map(int, input().split()))
tree = BinarySearch()
for num in numbers:
    if num == 0:
        break
    tree.ins(num)
balance = tree.balance()
print("YES" if balance else "NO")
