from calculator_backend.add import add
from calculator_backend.multiply import multiply


def cli() -> None:
    while (action := input("What do you want to do (add/multiply)? ")) in ("add", "multiply"):
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))

        match action:
            case "add":
                r = add(a, b)

            case "multiply":
                r = multiply(a, b)

        print(f"The result is: {r}")

    print("Bye!")
