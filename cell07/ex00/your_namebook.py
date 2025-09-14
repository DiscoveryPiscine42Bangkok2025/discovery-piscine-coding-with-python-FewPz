def array_of_names(people: dict) -> list:
    full_names = []
    for firstname, lastname in people.items():
        full_name = firstname.capitalize() + " " + lastname.capitalize()
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))