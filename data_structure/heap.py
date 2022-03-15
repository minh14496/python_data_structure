"""Time complexity :

build Heap is O(n) because if build heap with sift down
the only time it takes O(log(n)) is at the root while building heap
with sift up there are many times (leaves) that it takes O(log(n)).
-> build heap with sift up would take O(nlog(n))

sift down is O(log(n))
sift up is O(log(n))
"""

# firstChildIdx = parentIdx * 2 + 1
# secondChildIdx = parentIdx * 2 + 2

def maxHeap(array):
    firstParentIdx = (len(array)-1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
    firstChildIdx = currentIdx*2 + 1
    while firstChildIdx <= endIdx:
        secondChildIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else - 1
        if secondChildIdx != -1 and heap[secondChildIdx] > heap[firstChildIdx]:
            swapIdx = secondChildIdx
        else:
            swapIdx = firstChildIdx

        if heap[swapIdx] > heap[currentIdx]:
            swap(currentIdx, swapIdx, heap)
            currentIdx = swapIdx
            firstChildIdx = currentIdx * 2 + 1
        else:
            return 

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
def siftUp(self, currentIdx, heap):
    # Write your code here.
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
        self.swap(currentIdx, parentIdx, heap)
        currentIdx = parentIdx
        parentIdx = (currentIdx - 1) // 2

def peek(self):
    # Write your code here.
    return self.heap[0]

def remove(self):
    # Write your code here.
    self.swap(0, len(self.heap)-1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, self.heap)
    return valueToRemove

def insert(self, value):
    # Write your code here.
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)

def swap(self, i, j, array):
    array[i], array[j] = array[j], array[i]
