# Problem 1 — Payment Processing Queue (Foundational)
# Visa's payment processor handles requests using a priority system. 
# You are given a list of n payment requests, where each request is [paymentId, priority, arrivalTime]. 
# The processor handles one payment at a time and follows these rules:

# The processor always picks the highest priority payment from the waiting queue.
# If two payments have the same priority, the one with the earlier arrival time goes first.
# If both priority and arrival time are the same, the one with the smaller paymentId goes first.
# Each payment takes exactly 1 unit of time to process.
# Processing starts at time = 0.

# Return a list of paymentIds in the order they are processed.
# Important: A payment can only be picked if its arrivalTime <= currentTime. 
# If no payments are available at the current time, the processor jumps forward to the next available arrival time.
# Example:
# Input:
# requests = [
#   [101, 3, 0],
#   [102, 5, 0],
#   [103, 5, 1],
#   [104, 2, 0],
#   [105, 3, 3]
# ]

# Output: [102, 103, 101, 105, 104]

# Explanation:
# time=0: available=[101(p3),102(p5),104(p2)] → pick 102 (highest priority)
# time=1: available=[101(p3),103(p5),104(p2)] → pick 103 (highest priority)
# time=2: available=[101(p3),104(p2)] → pick 101 (higher priority)
# time=3: available=[104(p2),105(p3)] → pick 105 (higher priority)
# time=4: available=[104(p2)] → pick 104
# Constraints: 1 <= n <= 10^5, 1 <= priority <= 100, 0 <= arrivalTime <= 10^6
# Think about what data structure gives you efficient access to the highest priority element.

import heapq

def processPayments(requests):
    # sort by arrival time
    requests.sort(key=lambda x: x[2])
    
    heap = []
    result = []
    time = 0
    i = 0
    n = len(requests)

    while i < n or heap:
        
        # if nothing is available, jump time forward
        if not heap and time < requests[i][2]:
            time = requests[i][2]

        # add all available requests to heap
        while i < n and requests[i][2] <= time:
            paymentId, priority, arrival = requests[i]
            heapq.heappush(heap, (-priority, arrival, paymentId))
            i += 1

        # process highest priority
        if heap:
            _, _, paymentId = heapq.heappop(heap)
            result.append(paymentId)
            time += 1

    return result


requests = [
  [101, 3, 0],
  [102, 5, 0],
  [103, 5, 1],
  [104, 2, 0],
  [105, 3, 3]
]

print(processPayments(requests))