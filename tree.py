from typing import ParamSpec


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
            return 

        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else: 
                    self.current_node.right = Node(value)
                    break
    
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def remove(self, value):
        self.parent_node = self.head
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                # leaf Node 일때
                if self.current_node.left == None and self.current_node.right == None:
                    if self.parent_node.value < value:
                        self.parent_node.right = None
                    else: self.parent_node.left = None
                
                # child Node가 1개 있을때
                elif self.current_node.left != None and self.current_node.right == None:
                    if self.parent_node.value < value:
                        self.parent_node.right = self.current_node.left
                    else: self.parent_node.left = self.current_node.left
                elif self.current_node.left == None and self.current_node.right != None:
                    if self.parent_node.value < value:
                        self.parent_node.right = self.current_node.right
                    else: self.parent_node.left = self.current_node.right

                #child Node가 2개 있을때
                else:
                    # 오른쪽에서 가장작은값 찾기
                    min_node = self.current_node.right
                    parent_min_node = self.current_node

                    while min_node.left:
                        parent_min_node = min_node
                        min_node = min_node.left
                    min_node.left = self.current_node.left

                    if self.current_node != parent_min_node:
                        parent_min_node.left = min_node.right
                        min_node.right = self.current_node.right
                        
                    self.parent_node.right = min_node
                return True

            elif value < self.current_node.value:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right
        print("없음")








tree = Tree()
tree.insert(7)
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(8)
tree.insert(9)
tree.insert(13)
tree.insert(11)
tree.insert(19)

tree.remove(10)




print(tree.search(5))