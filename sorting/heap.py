# !/usr/bin/python
# coding:utf8

class MaxHeap():

    def __init__(self, seq=None):
        if seq:
            self.heapify(seq)
        else:
            self._elements = []

    def __len__(self):
        return len(self._elements)

    def add(self, value):
        pass

    def _shiftup(self, index):
        """Shift the value at the index element up the tree."""
        while index:
            parent = (index-1) / 2
            if self._elements[index] > self._elements[parent]:
                self._elements[index], self._elements[parent] = self._elements[parent], \
                            self._elements[index]
            index = parent

    def _buildheap(self):
        """Build the max heap."""
        length = len(self)
        for i in range(length):
            self._shiftup(length-i-1)

    def heapify(self, seq):
        """Transform the seq into a heap."""
        if hasattr(seq, '__iter__'):
            self._elements = list(seq)
            self._buildheap()
        else:
            raise TypeError('the seq is not iterable')


    def iter(self):
        """Yield value in order."""
        for i in range(len(self)):
            yield self._elements[i]


if __name__ == '__main__':
    heap = MaxHeap([1,3,2,3,4,1])
    for item in heap.iter():
        print item,

