from sevensegment.sevensegmenterror import SevenSegmentError


def display_screen(number):
    if len(number) == 8:
        num = list(number)

        if num[7] == "1":

            if num[0] == "1":
                print("######")
            else:
                print()

            for _ in range(2):
                if num[5] == "1":
                    print("#", end="")
                else:
                    print(" ", end="")
                if num[1] == "1":
                    print("    #")
                else:
                    print()

            if num[6] == "1":
                print("######")
            else:
                print()

            for _ in range(2):
                if num[4] == "1":
                    print("#", end="")
                else:
                    print(" ", end="")
                if num[2] == "1":
                    print("    #")
                else:
                    print(" ")

            if num[3] == "1":
                print("######")
            else:
                print()

        raise SevenSegmentError("The board is Off")
    raise ValueError("The binary digit must be of length 8 only")


def main():
    try:
        user_input = input("Enter an 8-digit binary number: ")
        display_screen(user_input)
    except ValueError as e:
        print(e)
    except SevenSegmentError as e:
        print(e)


if __name__ == "__main__":
    main()
