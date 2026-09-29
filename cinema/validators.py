def get_int(prompt, low=0, high=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if value < low:
            print("Value must be at least", low)
        elif high is not None and value > high:
            print("Value must be at most", high)
        else:
            return value
