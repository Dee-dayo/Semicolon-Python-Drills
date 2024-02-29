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


num = input("Enter a number: ")
display_screen(num)
