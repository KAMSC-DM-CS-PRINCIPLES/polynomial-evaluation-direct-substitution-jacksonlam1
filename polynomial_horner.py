def evaluate_polynomial_horner(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using Horner's method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    coeffs = coefficients
    S = coeffs[0]
    k = 1
    if len(coeffs) != degree:
        raise ValueError
    print("S0 = " + str(coeffs[0]))
    while k < degree:
        S = S * x + coeffs[degree-k]
        print("S" + str(k) + " = " + str(S))
        k = k + 1
    S+=constant_term
    print("S" + str(degree) + " = " + str(S))
    print("P(x) = " + str(S))
    return S
    pass

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial_horner function
    # TODO: Ask user if they want to run again
    person = "y"
    while person == "y":
        Degree = int(input("Degree:  "))
        x = float(input("x:  "))
        Constant = float(input("Constant term:  "))
        coeffs = []
        for i in range(1, Degree + 1):
            coeffs.append(int(input("Coefficient x^" + str(i) + ":  ")))
        print(Degree, x, Constant, coeffs)
        print(len(coeffs))
        evaluate_polynomial_horner(Degree, x, Constant, *coeffs)

        person = input("Run again(y/n)?  ")
    pass
