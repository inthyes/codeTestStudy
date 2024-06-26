import sys
import heapq

heap = []
n = int(input())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
