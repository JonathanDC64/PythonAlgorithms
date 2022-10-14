def insertion_sort(input: list[int]) -> None:
  for i in range(1, len(input)):
    key = input[i]

    # Move values up to i - 1 that are greater than  the 
    # value at the key index to one position ahead
    j = i - 1
    while j >= 0 and key < input[j]:
      input[j + 1] = input[j]
      j -= 1
    input[j + 1] = key