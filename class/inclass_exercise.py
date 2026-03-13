# def oN_cube(nums):
#     result = []
#     for num in nums:
#         result.append(num ** 3)
#         for i in range(nums):
#             for j in range(nums):
#                 print(num * i * j)
#     return result

# # write a function that is equivalent to the composite function f(n) = n + O(n^2)

# def f(n):
#     return n
# def g(nums):
#     for i in range(nums):
#         for j in range(nums):
#             print(nums + i + j)
#     return nums

# def h(nums):
#     return f(nums) + g(nums)


def anagram(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2



def anagram2(str1, str2):
    if len(str1) != len(str2):
        return False 

    temp = list(str2)

    for char in str1:
        check = False
        for i in range(len(temp)):
            if char == temp[i]:
                temp[i] = None
                check = True
                continue
        if not check:
            return False 
    return True




print(anagram2("abc", "cb"))