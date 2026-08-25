from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print("Square:", square(number))

    if is_even(number):
        print("The number is even")
    else:
        print("The number is odd")

    print("Fahrenheit:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()