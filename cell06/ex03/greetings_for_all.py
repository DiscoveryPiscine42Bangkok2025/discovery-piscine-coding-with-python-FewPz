def greetings(name=""):
    if isinstance(name, str):
        name = "noble stranger" if not name else name
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
