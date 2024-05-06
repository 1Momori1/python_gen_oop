def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main():
    number = int(input("Введите число: "))
    factors = find_factors(number)
    print(f"Множители числа {number}:")
    for factor in factors:
        print(f"{factor[0]} * {factor[1]}")

if __name__ == "__main__":
    main()
