def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    print()
    coeffs = coefficients
    S = constant_term
    k = 1
    if len(coeffs) != degree:
        raise ValueError
    print("S0 = " + str(S))

    while k<=degree:
        S = coeffs[k-1] * pow(x,k) + S
        print("S"+str(k)+" = "+ str(S))
        k = k+1
    print("P(x) = " + str(S))
    return S


    pass

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again
    person ="y"
    while person=="y":
        Degree = input("Degree:  ")
        x = input("x:  ")
        Constant = input("Constant term:  ")
        coeffs = []
        for i in range(1,Degree+1):
            coeffs.insert(input("Coefficient x^"+str(i)+":  "))
        print(Degree, x, Constant, coeffs)
        evaluate_polynomial(Degree, x, Constant, coeffs)

        person = input("Run again(y/n)?  ")
    pass