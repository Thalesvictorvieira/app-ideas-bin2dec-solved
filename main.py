# Convert Decimal to Binary
def to_binary(value):
    result = bin(value)
    updated_result = result.replace("0b", "")
    print(f"Result: {updated_result}")
    print("")


while True:
    option = int(input(
        "Welcome to the binary/decimal conversion system\n"
        "\nWhich option do you want?"
        "\n[1] Decimal -> Binary"
        "\n[2] Binary -> Decimal"
        "\n[3] Exit program"
        "\nOption: "
    ))

    match option:
        case 1:
            print("Option 1")
            decimal_number = int(input("Enter a decimal number: "))
            to_binary(decimal_number)

        case 2:
            print("Option 2")
            binary_number = int(input("Enter a binary number: "), 2)
            print(f"Result: {binary_number}")
            print("")

        case 3:
            print("You chose option 3 'Exit program'. See you later!")
            break

        case _:
            print("Invalid option. Available options are only 1, 2, or 3.")
