from linked_list import LinkedList,Node

class HashTable:
    def __init__(self, size):
        self.hashTable = [None for _ in range(size)]
        self.size = size


    def hash(self, key):
        if not isinstance(key, str):
            raise Exception("문자열이아님")
        return ord(key[0]) % self.size


    def saveData(self, data, val):
        hashAddr = self.hash(data)

        if self.hashTable[hashAddr] == None:
            s = LinkedList()
            s.add((data, val))
            self.hashTable[hashAddr] = s
        else:
            self.hashTable[hashAddr].add((data, val))


    def getData(self, data):
        hashAddr = self.hash(data)
        if self.hashTable[hashAddr] == None:
            return None
        return self.hashTable[hashAddr].search(data)

    def getAll(self):
        for linkedList in self.hashTable:
            if linkedList != None:
                linkedList.log()
        
        print()



table = HashTable(4)
table.saveData("승호", 7)
table.getAll()
table.saveData("태호", 5)
table.getAll()
table.saveData("정호", 1)
table.saveData("민호", 2)
table.saveData("구호", 3)
table.saveData("상호", 4)
table.saveData("휴휴", 6)
table.saveData("박박", 6.6)
table.saveData("강호", 8)
table.saveData("세호", 9)
table.saveData("정완", 9.9)
table.saveData("감완", 9.9)
table.saveData("ㅋ완", 9.9)
table.getAll()
print(table.getData("하하"))