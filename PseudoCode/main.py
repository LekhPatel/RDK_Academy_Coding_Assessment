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
    #sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2 # Using floor division instead of integer division for Indexes
    else:
        return numbers[n // 2]

def sort(numbers):
    # Return the sorted numbers
    print("Sorted")

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
median = sortAndFindMedian(numbers)
print("Median:", median)