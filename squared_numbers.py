#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program calculates the square of every number from 0 until the number
# inserted.


def main():
    # This function calculates the square of every number from 0 until the
    # number inserted.
    print("This program calculates the square of every"
          "number from 0 until the number inserted.\n")

    try:
        integer = int(input("Insert a positive integer: "))

        print()
        if integer > 0:
            for counter in range(integer + 1):
                result = counter ** 2

                print("{0}² = {1}".format(counter, result))
        else:
            print(
                "\nThis input is invalid, please, insert a positive integer.")
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
