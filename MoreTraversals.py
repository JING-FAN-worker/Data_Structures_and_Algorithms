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
    Tree.postorder()        # 1 3 2 4 9 7 6 5
    Tree.inorder()          # 1 2 3 4 5 6 7 9
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6'''