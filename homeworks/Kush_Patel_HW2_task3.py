

import heapq
import math


class SeventyFifthPercentileMonitor:
    def __init__(self):
        # Max-heap (stored as negatives) for the lowest ceil(0.75 * n) values.
        self.lower = []
        # Min-heap for the remaining largest values.
        self.upper = []
        self.count = 0

    def add(self, num):
        """Add a number and rebalance the heaps in O(log n) time."""
        self.count += 1

        # Decide which heap gets the new number first.
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        self._rebalance()

    def get_75th(self):
        """Return the 75th percentile in O(1) time."""
        if self.count == 0:
            return None
        return -self.lower[0]

    def _rebalance(self):
        """Keep exactly ceil(0.75 * n) values in the lower heap."""
        target_lower_size = math.ceil(0.75 * self.count)

        # Move elements until lower has the correct size.
        while len(self.lower) > target_lower_size:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

        while len(self.lower) < target_lower_size and self.upper:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

        # Fix ordering if an element in lower is bigger than one in upper.
        if self.lower and self.upper and (-self.lower[0] > self.upper[0]):
            lower_top = -heapq.heappop(self.lower)
            upper_top = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -upper_top)
            heapq.heappush(self.upper, lower_top)


if __name__ == "__main__":
    monitor1 = SeventyFifthPercentileMonitor()
    case1 = [7, 12, 15, 18, 23, 27, 31, 34, 39, 42, 46, 51, 55, 61, 66, 70, 74, 82, 89, 95]

    for num in case1:
        monitor1.add(num)

    print("Case 1 75th percentile:", monitor1.get_75th())

    monitor2 = SeventyFifthPercentileMonitor()
    case2 = [7, 12, 15, 18, 23, 27, 31, 34, 39, 42, 46, 51, 55, 61, 66, 70, 74, 82, 89, 95, 100]

    for num in case2:
        monitor2.add(num)

    print("Case 2 75th percentile:", monitor2.get_75th())