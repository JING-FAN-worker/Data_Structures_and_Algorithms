class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.is_mirror = False

    def insert(self, key: int):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if (not self.is_mirror and key < root.key) or (self.is_mirror and key > root.key):
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root

        self.root = _insert(self.root, key)

    def search(self, key: int):
        def _search(root, key):
            if root is None:
                return False
            if key == root.key:
                return True
            if (not self.is_mirror and key < root.key) or (self.is_mirror and key > root.key):
                return _search(root.left, key)
            else:
                return _search(root.right, key)

        return _search(self.root, key)

    def remove(self, key: int):
        def _remove(root, key):
            if root is None:
                return root
            if (not self.is_mirror and key < root.key) or (self.is_mirror and key > root.key):
                root.left = _remove(root.left, key)
            elif (not self.is_mirror and key > root.key) or (self.is_mirror and key < root.key):
                root.right = _remove(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = self._min_value_node(root.right)
                root.key = temp.key
                root.right = _remove(root.right, temp.key)
            return root

        self.root = _remove(self.root, key)

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def mirror(self):
        def _mirror(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            _mirror(root.left)
            _mirror(root.right)

        _mirror(self.root)
        self.is_mirror = not self.is_mirror

    def preorder(self):
        def _preorder(root):
            if root is None:
                return
            print(root.key)
            _preorder(root.left)
            _preorder(root.right)

        _preorder(self.root)

    def postorder(self):
        def _postorder(root):
            if root is None:
                return
            _postorder(root.left)
            _postorder(root.right)
            print(root.key)

        _postorder(self.root)

    def inorder(self):
        def _inorder(root):
            if root is None:
                return
            _inorder(root.left)
            print(root.key)
            _inorder(root.right)

        _inorder(self.root)

    def breadthfirst(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node:
                print(node.key)
                queue.append(node.left)
                queue.append(node.right)

'''if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()         # 5 9 7 6 1 3 4 2

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))   # True
    Tree.preorder()         # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()         # 5 1 2 4 9 7 6 8'''