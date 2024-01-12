def evaluate_polynomial(coefficients, x):
    result = 0
    for i, coef in enumerate(coefficients):
        result += coef * (x ** i)
    return result

def evaluate_derivative(coefficients, x):
    result = 0
    for i, coef in enumerate(coefficients[1:]):
        result += (i + 1) * coef * (x ** i)
    return result

def newton_method(coefficients, initial_guess, tolerance=1e-6, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        f_x = evaluate_polynomial(coefficients, x)
        f_prime_x = evaluate_derivative(coefficients, x)

        if abs(f_prime_x) < tolerance:
            break

        x = x - f_x / f_prime_x

        if abs(f_x) < tolerance:
            break

    return x

# 例子：解 x^5 + 1 = 0
coefficients1 = [1, 0, 0, 0, 0, 1]
solution1 = newton_method(coefficients1, initial_guess=0.5)
print("Solution for x^5 + 1 = 0:", solution1)

# 例子：解 x^8 + 3x^2 + 1 = 0
coefficients2 = [1, 0, 3, 0, 0, 0, 0, 0, 1]
solution2 = newton_method(coefficients2, initial_guess=0.5)
print("Solution for x^8 + 3x^2 + 1 = 0:", solution2)
