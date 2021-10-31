class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        

    def insert(self, v, data):
        if self.search(v) == False:
            print("삽입 불가능")
            return
        node = self.head
        while node.next:
            if v == node.data:
                s = Node(data)
                s.next = node.next
                node.next = s
            node = node.next
        if node.data == v:
            node.next = Node(data)
    
    def remove(self, data):
        if not self.search(data):
            print("데이터가 없음")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
    
    def log(self):
        node = self.head
        s = ""
        while node.next:
            s += "%.2f, " % (node.data)
            node = node.next
        s += "%.2f" % (node.data)
        print(s)
            
    def search(self, data) -> bool:
        node = self.head
        while node.next:
            if node.data == data:
                return True
            node = node.next
        if node.data == data:
            return True
        return False
        






l = LinkedList()
for i in range(1, 14):
    l.add(i)
print(l.search(13))
l.insert(8, 9.5)
l.log()
l.remove(1)
l.log()
l.remove(13)
l.log()















# def add(data):
#     node = head
#     while node.next:
#         node = node.next
#     node.next = Node(data)

# node1 = Node(1)
# head = node1
# for index in range(2, 10):
#     add(index)

# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print (node.data)

# print()

# node3 = Node(2.5)
# node = head
# save = 0
# while node.next:
#     if node.data == 2:
#         save = node.next
#         node.next = node3
#         node3.next = save
#         break
#     else: node = node.next
# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print (node.data)