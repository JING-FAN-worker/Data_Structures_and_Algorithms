class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.contains(key):
            self.root = self.insert_help(self.root, key)

    def contains(self, key):
        return self.contains_help(self.root, key)

    def contains_help(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        if key < node.key:               
            return self.contains_help(node.left, key)
        else:
            return self.contains_help(node.right, key)      #compare the node of the tree and bulid the tree

    def insert_help(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert_help(node.left, key)
        else:
            node.right = self.insert_help(node.right, key)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if key < node.left.key:                            #check it if it is balanced
                return self.right_rotation(node)
            else:
                return self.left_right_rotation(node)
        if balance < -1:                                       #check it if it is balanced
            if key > node.right.key:
                return self.left_rotation(node)
            else:
                return self.right_left_rotation(node)
        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):                                    #find the difference of node of two sides.
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotation(self, node):
        new_root = node.right                                             #change the location of the nodes
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def right_rotation(self, node):
        new_root = node.left                 
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def left_right_rotation(self, node):                                #change the location of nodes, more that one rotation
        node.left = self.left_rotation(node.left)
        return self.right_rotation(node)

    def right_left_rotation(self, node):
        node.right = self.right_rotation(node.right)
        return self.left_rotation(node)

    def preorder(self):
        self.preorder_helper(self.root)
        print()

    def preorder_helper(self, node):                           #print the node with the order node left then right
        if node:
            print(f"{node.key};{-self.get_balance(node)}", end=" ")
            self.preorder_helper(node.left)
            self.preorder_helper(node.right)