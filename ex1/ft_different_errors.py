#!/usr/bin/env python3

def garden_operations():
    # ValueError
    print("\nTesting ValueError...")
    try:
        int("Hello")
    except ValueError as e:
        print("Caught ValueError: ", e)

    # ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: ", e)

    # FileNotFoundError
    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: ", e)

    # KeyError
    print("\nTesting KeyError...")
    try:
        dict = {"Rose": 5}
        dict["missing_plant"]
    except KeyError as e:
        print("Caught KeyError: ", e)

    # Testing multiple errors
    print("\nTesting multiple error together...")
    try:
        int("hello")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
