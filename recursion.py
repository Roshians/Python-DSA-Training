# # Printing N Natural numbers using Recursion (1 to n)
# def printing(n):
#     if n == 0:
#         return
#     printing(n-1)
#     print(n, end=' ')
# printing(10)



# # Printing N Natural numbers using Recursion (n to 1)
# def prnt(n):
#     if n> 0:
#         print(n, end=' ')
#         return prnt(n-1)
# prnt(10)

# # Calculating Factorial using Recursion
# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n-1)*n 

# print(fact(5))


# Calculating fibonnaci series using recursion.
def fib(n):
    if n==1 or n==2:
        return (n-1)
    return fib(n-1) + fib(n-2)

print(fib(7))