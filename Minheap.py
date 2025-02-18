class MinHeap:
    def __init__(self, data=None):
        
        self.heap = data[:] if data else []  
        self.build_min_heap()

    
    def parent(self, i):
        return (i - 1) >> 1  

    def left_child(self, i):
        return (i << 1) + 1  

    def right_child(self, i):
        return (i << 1) + 2  

    def build_min_heap(self):
        """
        Build a min heap from an unordered list.
        Starts heapifying from the last non-leaf node.
        """
        for i in range(len(self.heap) // 2 - 1, -1, -1):  
            self.heapify(i)

    def heapify(self, i):
        """
        Ensures the heap property is maintained at index `i`.
        """
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def insert(self, value):
       
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def remove(self):
      
        if not self.heap:
            raise IndexError("Heap is empty, cannot remove element.")
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        if self.heap:  # Only heapify if heap is not empty
            self.heapify(0)
        return root_value

    def get_root(self):
        """
        Returns the root element without removing it.
        """
        if not self.heap:
            raise IndexError("Heap is empty, cannot fetch root.")
        return self.heap[0]

    def __str__(self):
        return "MinHeap---->" + str(self.heap)


# Example usage
if __name__ == "__main__":
    # Test Case 1: Integer values
    data1 = [42, 20, 35, 10, 4, 18, 3]
    print("Initial unsorted list:", data1)
    min_heap1 = MinHeap(data1)
    print("Min Heap:", min_heap1)
    print("Remove root:", min_heap1.remove())
    print("Heap after removal:", min_heap1)
    min_heap1.insert(2)
    print("Heap after inserting 2:", min_heap1)
    print("Peek at root:", min_heap1.get_root())
    print()

    # Test Case 2: Floating point values
    data2 = [12.5, 7.3, 25.8, 3.9, 9.6, 30.1]
    print("Initial unsorted float list:", data2)
    min_heap2 = MinHeap(data2)
    print("Min Heap:", min_heap2)
    print("Remove root:", min_heap2.remove())
    print("Heap after removal:", min_heap2)
    min_heap2.insert(5.2)
    print("Heap after inserting 5.2:", min_heap2)
    print("Peek at root:", min_heap2.get_root())
    print()

    # Test Case 3: Negative numbers
    data3 = [-5, -10, -3, -1, -20, -8]
    print("Initial unsorted negative numbers:", data3)
    min_heap3 = MinHeap(data3)
    print("Min Heap:", min_heap3)
    print("Remove root:", min_heap3.remove())
    print("Heap after removal:", min_heap3)
    min_heap3.insert(-15)
    print("Heap after inserting -15:", min_heap3)
    print("Peek at root:", min_heap3.get_root())
