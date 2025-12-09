def sorting_input():
    user_raw = input("Enter numbers separated by spaces: ")
    try:
        arr = [int(x) for x in user_raw.split() if x.strip() != ""]
    except ValueError:
        print("Invalid number in input. Please enter integers only.")
        arr = []

    method = input("Choose sorting method (bubble / quick): ").strip().lower()
    return arr, method
