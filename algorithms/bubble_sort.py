from algorithms.bubble_sort

def bubble_sort(x):
    n = len(arr)
    
    for i in range(n-1):                                          # range(n) also work but outer loop will
        
        for j in range(0, n-i-1):                                  
            if arr[j] > arr[j + 1]:                                # Swap if the element found is greater
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main() -> int:
    bubble_sort_input = [2,7,3,9,4,0,4]
    print(f"Bubble sort input {bubble_sort_input}")

    bubble_sort_output=bubble_sort(bubble_sort_input)
    print(f"Bubble sort output {bubble_sort_output}")
    return 0


if __name__ == "__main__":
    main()
