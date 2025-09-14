def famous_births(persons):
    sorted_persons = sorted(persons.values(), key=lambda p: int(p["date_of_birth"]))
    for person in sorted_persons:
        name = person["name"]
        birth_year = person["date_of_birth"]
        print(f"{name} is a great scientist born in {birth_year}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)