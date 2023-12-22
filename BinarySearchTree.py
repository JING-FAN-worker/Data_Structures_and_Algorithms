class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def search(self, key: int):
        def _search(root, key):
            if root is None:
                return False
            if key < root.key:
                return _search(root.left, key)
            elif key > root.key:
                return _search(root.right, key)
            else:
                return True
        return _search(self.root, key)

    def preorder(self):
        def _preorder(root):
            if root is None:
                return
            print(root.key)
            _preorder(root.left)
            _preorder(root.right)
        _preorder(self.root)

    def remove(self, key: int):
        def _remove(root, key):
            if root is None:
                return root
            if key < root.key:
                root.left = _remove(root.left, key)
            elif key > root.key:
                root.right = _remove(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = self._min_value_node(root.left)
                root.key = temp.key
                root.left = _remove(root.left, temp.key)
            return root
        self.root = _remove(self.root, key)

    def _min_value_node(self, node):
        while node.right is not None:
            node = node.right
        return node

'''if __name__ == "__main__":
    tree = BST()
    for num in (14, 19, 13, 23, 12, 17, 16, 10, 15, 11, 22, 28, 30, 25, 20):
        tree.insert(num)
    for num in (20, 25, 11, 29, 14):
        tree.remove(num)
    tree.preorder()  # Expected Output: 13 12 10 19 17 16 15 23 22 28 30'''