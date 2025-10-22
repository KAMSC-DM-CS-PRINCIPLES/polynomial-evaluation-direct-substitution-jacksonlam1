def evaluate_polynomial_horner(degree, x, constant_term, *coefficients):
   if len(coefficients) < degree: raise ValueError(f"need {degree} coefficient(s)")
    p = coefficients[-1]
    k = 1
    print(f"S{degree} (highest degree coefficient) = {coefficients[-1]}")
    while k < degree:
        print(f"S{k+1} (Horner step {k + 1}) = {p*x+coefficients[degree-k-1]}")
        p *= x
        p += coefficients[degree-k-1]
        k += 1
    print(f"S{degree+1} (add constant term) = {p*x + constant_term}")
    return p*x + constant_term

if __name__ == "__main__":
    # import sys
    # from io import StringIO
    # sys.stdin = StringIO("3\n2\n-7\n5\n2\n-1\ny\n1\n1\n3\n2\nn\n")

    while True:
        degree = int(input("Degree of the polynomial: "))
        x = float(input("Value of x: "))
        constant = float(input("Value of constant term:"))

        # coeffs = [print(f"Coefficient of the x^{i+1} term: ", end="") or
        #           float(input()) for i in range(degree)]
        coeffs = []
        for i in range(degree):
            coeffs.append(float(input(f"Coefficient of the x^{i + 1} term: ")))
        print(f"P(x) = {evaluate_polynomial_horner(degree, x, constant, *coeffs)}")

        print("Do you want to evaluate another polynomial? (y/n): ")
        if input() == "n":
            break
    pass
