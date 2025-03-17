# build a min heap (heapify)
# time; o(n), space: o(1)

# lets say that you have an array representing a tree 
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)  # now techinally satisfies heap properties 

# Heap Push (inserting elements)
# time: o(log n)
heapq.heappush(A, 4)

# Heap Pop (extract min)
# time: o(log n)

min_A = heapq.heappop(A)

# Writing a Heap Sort 
# time: o(n log n) space: o(n)
# note: possible to do this in o(1) space via swapping, but is more complex to explain 

def heapsort(arr): 
    heapq.heapify(arr)  # rearranges the arr to satisfy the heap property 
    n = len(arr)
    new_list = [o] * n 

    for i in range(n): 
        min_val = heapq.heappop(arr)
        newlist[i] = min_val

    return new_list


# Heap Push Pop 
# time: o (log n)

heapq.heappushpop(A, 99)  # for example if we were to push 99 and then pop the minheap val 

# We can also just peek at the min in constant o(1) time 
# just looking at it without modifying the tree
A[0]

### MAX HEAP 
# there is no native way to create a max heap 
# easiest way is to negate the values that you are sorting for, create a minheap from that, which will then effectively be a maxheap of the original values 

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range (n): 
    B[i] = -B[i]

heapq.heapify(B)  # for example the largest value (12) will be the smallest negative value, being the top of the minheap

largest = -heapq.heappop(B) # when popping need to turn back to the native sign of the value 

heapq.heappush(B, -7)  # if we wanted to insert a positive 7, we need to be sure to remember to insert a negative value that we're evaluating


### building a heap from 'scratch' 
# useful in storing modified values in heap 
C = [-5, 4, 2, 1, 7, 0, 3]

heap = [] 

for x in C: 
    heapq.heappush(heap, x)


### if we wanted to put tuples of items in the heap 

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
from collections import Counter 
# create a frequency map 
counter = Counter(D)

heap = []

for key, value in counter.items(): 
    heapq.heappush(heap, (value, key))  # evaluates based on the first value of the tuple but saves the 'tied' information which is the key in this case
