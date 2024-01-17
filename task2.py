def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iterations = 0 

    if upper_bound < x:
        return -1
 
    while low <= high:
        iterations += 1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return mid, iterations
 
    return mid, iterations

arr = [2, 3, 4, 10, 20.5, 35.5, 37.2, 39.1, 41.9, 43, 44, 45, 46]
x = 37.1
result, iterations = binary_search(arr, x)

print("Result:", binary_search(arr, x))

if result != -1 and arr[result] == x:
    print(f"Element is present at index {result}")
else:
    print(f"Closest element is present at index {result}")

print(f"Number of iterations: {iterations}")
