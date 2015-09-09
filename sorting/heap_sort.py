'''heap sorting
'''

def sort(seq):
    import heapq
    heap = list(seq)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]


if __name__ == '__main__':
       
    print sort([1,2,3,1,2])
