### Main Wrapper
def main():
    print("\033c")
    n = inputFunction()
    print("Finding all prime numbers smaller than or equal to " + str(n) + "...")
    final_list = runSieve(n)
    print_counter = 0
    print((i) for i in final_list)
    print("Number of primes between 2 and " + str(n) + ": " + str(len(final_list)))


### Get a positive integer greater than 2 from the user
def inputFunction():
    n = input("Please input a valid positive integer greater than 2: ")
    try:
        y = int(n)
    except ValueError:
        y = -1
    if not y > 2:
        print("Looks like that's not a valid input, try again!")
        n = inputFunction()
    return int(n)


### Perform Sieve of Erasthosenes Algorithm
def runSieve(n):
    mark_list = [False for i in range(2, n + 1)]
    for i in range(2, n + 1):
        if not mark_list[i - 2]:
            j = 2
            while i * j <= n:
                if not mark_list[i * j - 2]:
                    mark_list[i * j - 2] = True
                j += 1
    return [i for i in range(2, n + 1) if not mark_list[i - 2]]


if __name__ == "__main__":
    main()