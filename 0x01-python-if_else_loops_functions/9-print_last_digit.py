#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        pos_num = number * -1
        print(f"Positive number: {pos_num}")
        last_digit = pos_num % 10
        last_digit = last_digit * -1
    else:
        last_digit = number % 10
    print(f"{last_digit}", end="")
    return last_digit
