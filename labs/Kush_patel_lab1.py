"""
QUESTION 1:
Order the following functions by asymptotic growth rate.

Given functions:
1) 4n log n + 2n
2) 2^10
3) 2^{log n}
4) 3n + 100 log n
5) 4n
6) 2^n
7) n^2 + 10n
8) n^3
9) n log n

Simplified Big-O forms:
2^10 -> O(1)
2^{log n} -> O(n)
4n -> O(n)
3n + 100 log n -> O(n)
n log n -> O(n log n)
4n log n + 2n -> O(n log n)
n^2 + 10n -> O(n^2)
n^3 -> O(n^3)
2^n -> O(2^n)

FINAL ORDER (smallest to largest growth):
-->2^10
--> 2^{log n}
--> 4n
--> 3n + 100 log n
--> n log n
--> 4n log n + 2n
--> n^2 + 10n
--> n^3
--> 2^n
"""
# Question number 2: Time complexity for each function in lab1_exercises.py


def example1(S):
    """
    Time Complexity: O(n)
    Explanation: The function iterates once over the list S of length n.
    --> Therefore, total runtime grows linearly with n.
    """
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total


def example2(S):
    """
    Time Complexity: O(n)
    Explanation: The loop increments by 2, so it runs approx. n/2 times. as 2 is a constant factor, it is ignored.
    --> Therefore, the time complexity is O(n).
    """
    n = len(S)
    total = 0
    for j in range(0, n, 2):       # note the increment of 2
        total += S[j]
    return total


def example3(S):
    """
    Time Complexity: O(n^2)
    Explanation: The outer loop runs n times and the inner loop runs j+1 times for each iterationn.
    - This simplifies to O(n^2).
    """
    n = len(S)
    total = 0
    for j in range(n):             # loop from 0 to n-1
        for k in range(1+j):       # loop from 0 to j
            total += S[k]
    return total


def example4(S):
    """
    Time Complexity: O(n)
    Explanation: The function uses a single loop that runs n times and prefix is computed in constant time.
    - Therefore, the total runtime is O(n).
    """
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


def example5(A, B):                # assume that A and B have equal length
    """
    Time Complexity: O(n^3)
    Explanation: The outer loop runs n times, the middle loop runs n times and the innner loop runs j+1 times for each iteration.
    - Total operations:
      n * (1 + 2 + ... + n) = n * n(n+1)/2 --> O(n^3)    
    """        
    n = len(A)                  
    count = 0
    for i in range(n):             # loop from 0 to n-1
        total = 0
        for j in range(n):         # loop from 0 to n-1
            for k in range(1+j):   # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count


# Question number 3: Python function with O(1) space complexity in the best case and O(n^@) in the worst case>

def space_complexity_example(n, build_matrix=False):
    """
    Best Case Space Complexity: O(1)
    Worst Case Space Complexity: O(n^2)
    Explanation:
    - If build_matrix is False, only a few variables are used → O(1) space.
    - If build_matrix is True, an n x n 2D list is created → O(n^2) space.
    """

    if not build_matrix:
        # Best case: constant space
        return 0

    # Worst case: n^2 space
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i + j)
        matrix.append(row)

    return matrix


print(space_complexity_example(3, build_matrix=True))

