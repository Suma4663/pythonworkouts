def recurse_fact(arg):
    if arg == 1:
        return 1
    else:
        return (arg * recurse_fact(arg-1))
n=int(input("Input number: "))
print(f"Factorial of {n} is {recurse_fact(n)}")