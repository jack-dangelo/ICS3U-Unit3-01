#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: Sep 2019
# This program adds two integers together


def main():
    # This function calculates the answer of two integers added to eachother
    # input
    first_integer = int(input("Enter first integer: "))
    second_integer = int(input("Enter second integer: "))
    # process
    total_value = first_integer + second_integer
    # output
    print("")
    print(first_integer, "+", second_integer, "=", total_value)


if __name__ == "__main__":
    main()
