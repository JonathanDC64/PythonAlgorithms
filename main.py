from algorithms.selection_sort import selection_sort

def main() -> int:
    selection_sort_input = [2,7,3,9,4,0,4]
    print(f"Selection sort input {selection_sort_input}")

    selection_sort(selection_sort_input)
    print(f"Selection sort output {selection_sort_input}")
    return 0


if __name__ == "__main__":
    main()
