class NumberOutOfRange(ValueError):
    """An extension to the standard ValueError exception."""
    pass

def to_roman(arabic_num):
    """Convert Hindu-Arabic number to Roman number."""
    if not 0 < arabic_num < 4000:
        raise NumberOutOfRange("Number out of range (1 to 3999)")

    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    result = ""
    for numeral, value in roman_numerals:
        while arabic_num >= value:
            result += numeral
            arabic_num -= value

    return result

# Example usage:
try:
    arabic_number = int(input("Enter an integer between 1 and 3999: "))
    roman_number = to_roman(arabic_number)
    print(f"The Roman numeral representation is: {roman_number}")
except ValueError as ve:
    print(f"Error: {ve}")
except NumberOutOfRange as noor:
    print(f"Error: {noor}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    