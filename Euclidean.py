def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def adjust_to_z26(value):
    return (value % 26 + 26) % 26  # Ensures non-negative values in range 0-25

if __name__ == "__main__":  # Corrected here
    # Get user input for a and b
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))

    # Call the extended Euclidean function
    gcd, x, y = extended_euclidean(a, b)

    # Print initial values of x and y
    print(f"Initial values: x = {x}, y = {y}")

    # Adjust x and y to be in the Z26 range
    x_z26 = adjust_to_z26(x)
    y_z26 = adjust_to_z26(y)

    # Display the results
    print(f"GCD: {gcd}")
    print(f"x in Z26: {x_z26}, y in Z26: {y_z26}")
