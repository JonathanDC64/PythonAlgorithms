
from inspect import _void


def selection_sort(input: list[int]) -> None:
  for i in range(len(input)):
    # Find the lowest value element in remaining input
    min_index = i
    for j in range(i + 1, len(input)):
        if input[min_index] > input[j]:
            min_index = j

    # Swap the lowest value with the current first value
    input[i], input[min_index] = input[min_index], input[i]
