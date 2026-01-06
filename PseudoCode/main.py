# FUNCTION sortAndFindMedian(numbers)
# CALL sort(numbers)
# DEFINE n AS length of numbers
# IF n MOD 2 = 0
# RETURN (numbers[n/2 - 1] + numbers[n/2 ) / 2
# ELSE
# RETURN numbers[n/2]
# ENDIF
# ENDFUNCTION

# FUNCTION sort(numbers)
# // Implement a sorting algorithm (e.g., bubble sort, selection sort, etc.)
# // Sort the 'numbers' array in ascending order
# // Pseudocode for the sorting algorithm is not provided; implement as per your
# understanding
# ENDFUNCTION

def sortAndFindMedian(numbers):
    sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2 # Using floor division instead of integer division for Indexes
    else:
        return numbers[n // 2]

def sort(numbers):
    n = len(numbers) # storing the length for simplicity/
    
    for i in range(n): # Outer loop that runs for the number of elements

        for j in range(0, n - i - 1): # iterates through elements and avoids the sorted bubbles in the end

            if numbers[j] > numbers[j + 1]: 
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # Larger bubble moves towards the end of the list.
    print(f"sorted numbers: {numbers}")

numbers = list(map(float, input("Enter numbers separated by spaces: ").split())) # reads inputs, splits by space, and maps the float values in the numbers lits
median = sortAndFindMedian(numbers) # Calling the function to find the median
print(f"Median: {median}")