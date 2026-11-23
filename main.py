# Returnerar namn och e-post (tuple)
def read_name_and_email():
    name = input("Ange namn: ").strip()
    email = input("Ange e-post: ").strip().lower()
    return name, email


# Frågar tills åldern är giltig
def read_age():
    while True:
        try:
            age = int(input("Ange ålder: "))
            if age >= 0:
                return age
            print("Åldern kan inte vara negativ.")
        except ValueError:
            print("Fel: åldern måste vara ett heltal, t.ex. 17.")


# Linjär sökning, blir -1 om det saknas
def find_index_by_email(users, email):
    for i in range(len(users)):
        if users[i]["email"] == email:
            return i
    return -1


# Lägger till en ny användare
def add_user(users):
    name, email = read_name_and_email()  # Packar upp tuplen

    # Förhindrar dubbletter
    if find_index_by_email(users, email) != -1:
        print("Fel: e-postadressen finns redan. Användaren sparades inte.")
        return

    age = read_age()
    users.append({"name": name, "age": age, "email": email})
    print(f"Användaren {name} har lagts till.")


# Söker på namn eller e-post
def search_user(users):
    term = input("Sök på namn eller e-post: ").strip().lower()

    found = False
    for user in users:
        # Matcha del av namn eller exakt e-post
        if term in user["name"].lower() or term == user["email"]:
            print(f"{user['name']}, {user['age']} år, {user['email']}")
            found = True

    if not found:
        print("Ingen användare hittades.")


# Visar alla användare i bokstavsordning
def show_users(users):
    if not users:
        print("Listan är tom.")
        return

    # Sortera efter namn
    for user in sorted(users, key=lambda user: user["name"].lower()):
        print(f"{user['name']}, {user['age']} år, {user['email']}")


# Tar bort användare via e-post
def remove_user(users):
    email = input("Ange e-post för användaren som ska tas bort: ").strip().lower()
    index = find_index_by_email(users, email)

    if index == -1:
        print("Det finns ingen användare med den e-postadressen.")
    else:
        removed = users.pop(index)
        print(f"Användaren {removed['name']} har tagits bort.")


# Meny
def main():
    users = []  # Lista med dictionaries

    while True:
        print("\n1. Lägg till användare")
        print("2. Sök användare")
        print("3. Visa alla användare")
        print("4. Ta bort användare")
        print("5. Avsluta")
        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            add_user(users)
        elif choice == "2":
            search_user(users)
        elif choice == "3":
            show_users(users)
        elif choice == "4":
            remove_user(users)
        elif choice == "5":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val, försök igen.")


main()
