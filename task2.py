def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    closest_larger = None
    iterations = 0 
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            closest_larger = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return arr[mid], iterations
 
    return (closest_larger, iterations) if closest_larger is not None else (arr[-1], iterations)

arr = [2, 3, 4, 10, 20.5, 35.5, 37.2, 39.1, 41.9, 43, 44, 45, 46]
x = 35.6
result, iterations = binary_search(arr, x)

print("Result:", binary_search(arr, x))

if result == x:
    print(f"Element {x} is present at index {arr.index(x)}")
else:
    print(f"Closest element is {result}")
print(f"Number of iterations: {iterations}")
