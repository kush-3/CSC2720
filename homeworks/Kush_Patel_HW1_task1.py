# Kush patel
# homework1 task 1:

def next_greater_elements(arr):
    n = len(arr)
    # initialize result array with -1
    result = [-1] * n 
    # stack to store elements
    stack = []

# traverse the array from right to left 
    for i in range(n - 1, -1, -1):
# remove elements from stack that are less than or equalt to the current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
# if stack is not empty then teh top is the next greater element
        if stack:
            result[i] = stack[-1]
        # push the current element to the stack 
        stack.append(arr[i])

    return result


# driver code:
if __name__ == "__main__":
    arr = [2,1,4,3]
    output = next_greater_elements(arr)

    print("Input array:", arr)
    print("Output arrat: ", output)