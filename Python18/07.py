def solve(coefficients):
    n = len(coefficients)
    if n == 3:
        a, b, c = coefficients
        x = (b**2 - 4*a*c)**0.5
        return x
    elif n == 2:
        a, b = coefficients
        x = (b - a)/(a)
        return x
    else:
        return "No roots"

def print_roots(coefficients):
    n = len(coefficients)
    if n == 3:
        a, b, c = coefficients
        x1, x2 = solve(coefficients)
        print(f"Roots: {x1} and {x2}")
    elif n == 2:
        a, b = coefficients
        x = solve(coefficients)
        print(f"Root: {x}")
    else:
        print("No roots")


coefficients = [2, 4]
print_roots(coefficients)

