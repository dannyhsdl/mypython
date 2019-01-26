def factorial(k):
    if (k>1):
        result=k*factorial(k-1)
    elif k==1:
        result=1
    return result
print("\nThe example result:\n".title())
result=factorial(6)
print(result)