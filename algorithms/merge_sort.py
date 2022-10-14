def merge_sort(input: list[int]) -> None:
  input_size = len(input)

  if input_size > 1:

    # Get the middle of the input
    middle_point = input_size // 2

    # Divide the 2 halfs of the input
    left_input = input[:middle_point]
    right_input = input[middle_point:]

    # Sort each half
    merge_sort(left_input)
    merge_sort(right_input)

    # Initialize indices
    i = 0
    j = 0
    k = 0

    left_input_size = len(left_input)
    right_input_size = len(right_input)

    while i < left_input_size and j < right_input_size:
      if left_input[i] <= right_input[j]:
        input[k] = left_input[i]
        i = i + 1
      else:
        input[k] = right_input[j]
        j = j + 1
      k = k + 1

    while i < left_input_size:
      input[k] = left_input[i]
      i = i + 1
      k = k +1

    while j < right_input_size:
      input[k] = right_input[j]
      j = j + 1
      k = k + 1