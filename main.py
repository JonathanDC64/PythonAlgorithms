from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort


def main() -> int:

    ### Selection Sort ###
    selection_sort_input = [2, 7, 3, 9, 4, 0, 4]
    print(f"Selection sort input {selection_sort_input}")

    selection_sort(selection_sort_input)
    print(f"Selection sort output {selection_sort_input}")

    ### Insertion Sort ###
    insertion_sort_input = [6, 2, 1, 7, 4, 3, 2, 7]
    print(f"Insertion sort input {insertion_sort_input}")

    insertion_sort(insertion_sort_input)
    print(f"Insertion sort output {insertion_sort_input}")

    ### Bubble Sort ###
    bubble_sort_input = [4, 5, 8, 3, 1, 3, 5, 9, 0]
    print(f"Bubble sort input {bubble_sort_input}")

    bubble_sort(bubble_sort_input)
    print(f"Bubble sort output {bubble_sort_input}")

    return 0

if __name__ == "__main__":
    main()
