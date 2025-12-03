def sorting_input():
    user_raw = input("Enter numbers separated by spaces: ")
    arr = [int(x) for x in user_raw.split()]

    method = input("Choose sorting method (bubble / quick): ").strip().lower()

    if method == "bubble":
        return bubble_sort(arr)
    elif method == "quick":
        return quick_sort(arr)
    else:
        return arr
