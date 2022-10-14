from algorithms.bubble_sort import bubble_sort

def main() -> int:
    bubble_sort_input = [2,7,3,9,4,0,4]
    print(f"Bubble sort input {bubble_sort_input}")

    bubble_sort_output=bubble_sort(bubble_sort_input)
    print(f"Bubble sort output {bubble_sort_output}")
    return 0


if __name__ == "__main__":
    main()
