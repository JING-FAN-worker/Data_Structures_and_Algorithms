class HashLinear:
    def __init__(self, M):
        self.M = M
        self.table = [None] * M

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.M

    def insert(self, data):
        index = self.hash(data)
        original_index = index
        while True:
            if self.table[index] is None or self.table[index] == 'empty':
                self.table[index] = data
                break;
            if self.table[index] == data:
                break;
            index = (index + 1) % self.M 
            if index == self.M + 1:
                index = 0;
            if index == original_index:
                break;     

    def delete(self, data):
        index = self.hash(data)
        original_index = index
        while True:
            if self.table[index] == data:
                self.table[index] = 'empty'
            index = (index + 1) % self.M 
            if index == self.M + 1:
                index = 0;
            if index == original_index:
                break;

    def print(self):
        for data in self.table:
            if data is not None and data != 'empty':
                print(data + " ")

'''if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1'''