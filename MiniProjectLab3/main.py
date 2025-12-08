from input import sorting_input
from sort_algorithms import bubble_sort, quick_sort
from output import show_output

def main():
    arr, method = sorting_input()

    if method == "bubble":
        result = bubble_sort(arr)
    elif method == "quick":
        result = quick_sort(arr)
    else:
        print("Invalid method! Showing original array.")
        result = arr

    show_output(result)

if name == "main":
    main()