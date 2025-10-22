def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # set P and k
    k = 1
    P = constant_term
    print(f"S0 (value of the constant term) = {P}")
    if len(coefficients) != degree:
        raise ValueError(f"need {degree} coefficient(s)")
     while k <= degree:
        P = str(int(P) + coefficients[k-1] * (x ** (k)))
        print(f"S{k} (Sum of the {k+1} lowest terms) = {P}")
        k = k + 1
    print(f"P(x)= {P}")
    return int(P)

if __name__ == "__main__":
    while True:
        coefficients = ()
        degree = int(input("Degree of the polynomial: "))
        x = int(input("Value of x: "))
        constant_term = int(input("Value of constant term: "))
        for i in range(degree):
            coefficients+=(int(input("Value of coefficient: ")), )
        evaluate_polynomial(degree, x, constant_term, *coefficients)
        again = input("Run again? (y/n): ")
        if again != "y":
            break
