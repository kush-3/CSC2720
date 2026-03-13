"""
CSC 2720 - Lab 2
Name: Kush Patel
PantherId : 002884216

Problem:
You are given an array that consists of n ≥ 0 pairs of integers and one unique number
(total 2n + 1 numbers).

Tasks:
a) Find the unique number using a brute force approach
b) Find the unique number in O(n) time and O(n) space
c) Find the unique number in O(n) time and O(1) extra space
"""


def find_unique_brute_force(arr):
    """
    Brute force approach:
    For each element, count it's occurence 
    time complexity: O(n^2)
    space complexity: O(1)
    """
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return None


def find_unique_ON_ON(arr):
    """
    O(n) time and O(n) soace task:
    using a dictionary to count frequency 
    time and space complexity of the approach: O(n)
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for num, count in freq.items():
        if count == 1:
            return num
    return None


def find_unique_ON_O1(arr):
    """
    task 3 : find the unique number in O(n) time and use only 
    constant space no extra. 
    Use XOR property:
    a ^ a = 0 and a ^ 0 = a
    """
    result = 0
    for num in arr:
        result ^= num
    return result 



# driver code 

if __name__ == "__main__":

    arrays = [
        [0,2,-4, 5,2,0,-4],
        [3,3,3,3,6,6,7],
        [1,1,1,1,1,1,1,1,2],
        [1,0,1,2,4,2,4],
        [3]
    ]
    expected = [
        5, 
        7,
        2,
        0,
        3
    ]

    for idx, i in enumerate(arrays):
        print("=======================================")
        print("array:", i)
        print("expected:", expected[idx])
        print("unique number(brute force):", find_unique_brute_force(i))
        print("unique number (task 2):", find_unique_ON_ON(i))
        print("unique number (task 3): ", find_unique_ON_O1(i))
        print("========-============================================")