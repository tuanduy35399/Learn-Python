import Sort
import time
import Math
import random
a = random.sample(range(0, 10000), 10000)
b = a.copy()
c = a.copy()
print(a)
result=Math.sum(a)
print("Sum of array {} = {}".format(a, result))
start= time.time()
Sort.quicksort(a, 0, len(a)-1)
end= time.time()
print("Quick Sort in {:.10f}s".format(end-start))
start= time.time()
b.sort()
end= time.time()
print("Func sort() in {:.10f}s".format(end-start))

start= time.time()
Sort.merge_sort(a, 0, len(a)-1)
end= time.time()
print("Merge sort in {:.10f}s".format(end-start))