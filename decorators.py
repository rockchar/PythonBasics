def func():
    return 1


print(func())


def say_hello(name="rohit"):
    print(f"Saying hello to {name}!")

    def hello_in_hello():
        return f"\tHello inside hello from {name}"

    def bye_in_hello():
        return f"\tBye from {name}"

    print(hello_in_hello())
    print(bye_in_hello())

    return "say_hello complete"

print(say_hello())