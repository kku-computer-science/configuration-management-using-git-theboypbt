from input import sorting_input
from sort_algorithms import bubble_sort, quick_sort
from output import show_output

def main():
    arr, method = sorting_input()

    if not arr:
        print("No numbers provided. Exiting.")
        return

    try:
        arr = [int(x) for x in arr]
    except Exception:
        print("Input contains non-integer values. Exiting.")
        return

    method = str(method).strip().lower()
    if method in ("1", "b", "bubble"):
        method = "bubble"
    elif method in ("2", "q", "quick"):
        method = "quick"

    try:
        if method == "bubble":
            result = bubble_sort(list(arr))
        elif method == "quick":
            result = quick_sort(list(arr))
        else:
            print("Invalid method! Showing original array.")
            result = arr
    except Exception as e:
        print(f"Error during sorting: {e}")
        result = arr

    show_output(result)

if _name_ == "_main_":
    main()
