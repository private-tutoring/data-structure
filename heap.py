class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def findall(self):
        print(self.heap_array)

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        c_node_index = len(self.heap_array)-1
        p_node_index = c_node_index // 2
        while c_node_index != 1 and data > self.heap_array[p_node_index]:   
            self.heap_array[c_node_index] = self.heap_array[p_node_index]
            self.heap_array[p_node_index] = data
            c_node_index = p_node_index
            p_node_index //= 2
        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        pop_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        self.heap_array.pop()
        length = len(self.heap_array)
        p_n_i = 1
        r_n_i = p_n_i * 2 + 1
        l_n_i = p_n_i * 2

        if r_n_i >= length and l_n_i < length:
            if self.heap_array[l_n_i] > self.heap_array[p_n_i]:
                self.heap_array[l_n_i], self.heap_array[p_n_i] = self.heap_array[p_n_i], self.heap_array[l_n_i]

        if r_n_i < length:
            while self.heap_array[p_n_i] < self.heap_array[r_n_i] or self.heap_array[p_n_i] < self.heap_array[l_n_i]:
                if self.heap_array[r_n_i] < self.heap_array[l_n_i]:
                    self.heap_array[p_n_i], self.heap_array[l_n_i] = self.heap_array[l_n_i], self.heap_array[p_n_i]   
                    p_n_i = l_n_i
                else:
                    self.heap_array[p_n_i], self.heap_array[r_n_i] = self.heap_array[r_n_i], self.heap_array[p_n_i]
                    p_n_i = r_n_i
                r_n_i = p_n_i * 2 + 1
                l_n_i = p_n_i * 2
                if l_n_i >= length:
                    break
                elif r_n_i >= length and self.heap_array[l_n_i] > self.heap_array[p_n_i]:
                    self.heap_array[l_n_i], self.heap_array[p_n_i] = self.heap_array[p_n_i], self.heap_array[l_n_i]
                    break

        return pop_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.findall()
heap.insert(7)
heap.insert(11)
heap.insert(50)
heap.insert(70)
heap.insert(1)
heap.insert(12)
heap.findall()

print(heap.pop())
heap.findall()


