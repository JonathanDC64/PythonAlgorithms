def bubble_sort(input: list[int]) -> None:
  input_size = len(input)
  for i in range(input_size):
    for j in range(0, input_size - i - 1):

      # From index 0 ti input_size - i - 1, 
      # we can swap elements (j) 
      # that are greater than the next (j+1)
      if input[j] > input[j + 1]:
        input[j], input[j + 1] = input[j + 1], input[j]