
# Python script that does something



num = 100

fib_memory = [-1] * (num + 1)

fib_memory[0] = 1
fib_memory[1] = 1



def fib(n: int) -> int:
    if n <= 1:
        return 1
    
    if fib_memory[n] == -1:
        fib_num = fib(n - 1) + fib(n - 2)
        fib_memory[n] = fib_num

        return fib_num
    
    return fib_memory[n]



print(f"The first {num} Fibonacci Numbers:")

for i in range(num + 1):
    print(f"{i}: {fib(i)}")
