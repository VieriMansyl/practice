def divide(dividend: int, divisor: int) -> int:        
    if dividend == -2**31 and divisor == -1:
        return 2**31-1

    sign = 1 if (dividend > 0) == (divisor > 0) else -1

    absDividend = abs(dividend)
    absDivisor = abs(divisor)

    quotient = 0

    while absDividend >= absDivisor:
        multiplier = 0

        while absDividend > (absDivisor<<(multiplier + 1)):
            multiplier += 1
        
        absDividend -= absDivisor << multiplier
        quotient += 1 << multiplier

    return sign * quotient

print(divide(10, 3))