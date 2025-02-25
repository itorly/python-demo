def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Generate a random array
import random

def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]
# Test code
def test_quicksort_inplace():
    # Generate a random array
    arr = generate_random_array(10, 1, 100)
    print("Original array:", arr)

    # Sort the array in place
    quicksort_inplace(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)

    # Verify the sorting result
    assert arr == sorted(arr), "Quicksort result is incorrect"
    print("Quicksort result is correct")


# Run the test
test_quicksort_inplace()
