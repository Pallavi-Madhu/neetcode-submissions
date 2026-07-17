class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums , k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#LOGIC
#--> heapify will sort the array nums and store in minHeap
#--> [1,2,3,4,5] and k =3 then pop smallest element as long as len(list) is 5 > k ie 3.
#--> so remaining [3,4,5] and 3rd largest is 3 
#--> while adding ,heapq.heappush..and if len > k:
#--> heapq.heappop() will remove the smaleest elemnet to satisfy len <= k
#--> return minHeap[0] -- smallest element