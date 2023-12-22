class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.next = nextNode
    
class LinkedList:
    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None, self.tail)
        self.len = 0
    def append(self, data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.len += 1

    def insert(self, data, i):
        insert_node = Node(data)
        if i < 0:
            raise IndexError("Index out of range (negative index)")
        if i == 0:
            insert_node.next = self.head
            self.head = insert_node
            return
        current_node = self.head
        for num in range(i-1):
            if current_node is None:
                raise IndexError("Index out of range (index too large)")
            current_node = current_node.next
        if current_node is None:
            raise IndexError("Index out of range (index too large)")
        insert_node.next = current_node.next
        current_node.next = insert_node

    def delete(self, i):
        if i < 0:
            raise IndexError("Index out of range (negative index)")
        if i == 0:
            if self.head is not None:
                delete = self.head.data
                self.head = self.head.next
                return delete
            else:
                raise IndexError("Index out of range (empty list)")
        current_node = self.head
        for num in range(i-1):
            if current_node is None or current_node.next is None:
                return None
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            return None
        delete = current_node.next.data
        current_node.next = current_node.next.next
        return delete
        
    def print(self):
        sentence = ''
        current_node = self.head
        while current_node is not None:
            if current_node.data is not None:
                sentence = sentence + str(current_node.data) + " -> "
            current_node = current_node.next
        print(sentence[:-4])
    
    def index(self, data):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == data:
                return index
            index += 1
            current_node = current_node.next
        return -1
                
    def swap(self, i, j):
        if i < 0 or j < 0:
            return
        if i == j:
            return
        current_node = self.head
        prev_node_i = None
        prev_node_j = None
    # Find the nodes at positions i and j
        for num in range(i):
            if current_node is None:
                return
            prev_node_i = current_node
            current_node = current_node.next
        node_i = current_node
        current_node = self.head
        for num in range(j):
            if current_node is None:
                return
            prev_node_j = current_node
            current_node = current_node.next
        node_j = current_node
        if node_i is None or node_j is None:
            return
    # Update the previous nodes to point to the new nodes
        if prev_node_i:
            prev_node_i.next = node_j
        else:
            self.head = node_j

        if prev_node_j:
            prev_node_j.next = node_i
        else:
            self.head = node_i
    # Swap the next pointers of node_i and node_j
        temp = node_i.next
        node_i.next = node_j.next
        node_j.next = temp

'''if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()'''