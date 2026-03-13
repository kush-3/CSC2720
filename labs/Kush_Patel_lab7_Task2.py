def print_subsets(arr):
    result = []
    
    def helper(index, current_subset):
        # Base case: if we reach the end of the list
        if index == len(arr):
            result.append(current_subset[:])
            return
        
        # Include the current element
        current_subset.append(arr[index])
        helper(index + 1, current_subset)
        
        # Exclude the current element (backtrack)
        current_subset.pop()
        helper(index + 1, current_subset)
    
    # Start recursion
    helper(0, [])
    
    # Print all subsets
    for subset in result:
        print(subset)



print("Test Case 1:")
print_subsets([1, 2, 3])

print("\nTest Case 2:")
print_subsets(['a', 'b'])

print("\nTest Case 3:")
print_subsets([])