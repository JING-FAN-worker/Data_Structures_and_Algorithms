class HashBucket:
    
    def __init__(self, M, B):
        self.M = M
        self.B = B
        self.table = [None]*M
        self.over = []*M
        
    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.B
    
    def insert(self, data):
        for i in range(self.M):
            if self.table[i] == data:
                return 
        for i in range(len(self.over)):
            if self.over[i] == data:
                return    
        try:
            bucket_size = int(self.M / self.B)
            bucket_index = self.hash(data)
        except Exception:
            return
        slot = bucket_index * bucket_size
        if self.table[slot] == None:
            self.table[slot] = data
        else:
            while (self.table[slot] != None): 
                slot = slot + 1
                if slot >= (bucket_index+1)*bucket_size:
                    self.over.append(data)
                    return
            self.table[slot] = data  
            
    def delete(self, data):
        for i in range(self.M):
            if self.table[i] == data:
                self.table[i] = None
                return
        for i in range(len(self.over)):
            if self.over[i] == data:
                self.over.remove(self.over[i])
                return
            #I learnt this method from my friend since my code is too long and it is't clear. 
    
    def print(self):
        for i in range(self.M):
            if self.table[i] != None:
                print( self.table[i]+" ")
        for i in range(len(self.over)):
            print( self.over[i]+" ")

'''if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1'''