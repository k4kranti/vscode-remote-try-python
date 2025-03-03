def bye() -> None:
    print('Bye, world!')

def greet() -> None:
    print('Hello, world!')

# good practice to create main() as more readable like psvm is java
def main() -> None:
    greet()
    bye()

if __name__ == '__main__':
    main()