# Inlämning 2 - Hantera en lista med användare


# Hjälpfunktion: Läs in namn och e-post, returneras som en tuple
def read_name_and_email():
    # Namnet får inte vara tomt
    name = input("Ange namn: ").strip()
    while name == "":
        print("Namnet får inte vara tomt.")
        name = input("Ange namn: ").strip()

    # E-post sparas med små bokstäver så att Anna@Example.com och
    # anna@example.com räknas som samma adress
    email = input("Ange e-post: ").strip().lower()
    while not is_valid_email(email):
        print("Ogiltig e-postadress. Den måste innehålla @ och en punkt efter @.")
        email = input("Ange e-post: ").strip().lower()

    return name, email  # Returneras som en tuple


# Hjälpfunktion: Enkel kontroll av att e-postadressen ser rimlig ut
def is_valid_email(email):
    if email.count("@") != 1 or " " in email:
        return False
    local, domain = email.split("@")  # split ger två delar som packas upp
    return local != "" and "." in domain and not domain.startswith(".") and not domain.endswith(".")


# Hjälpfunktion: Läs in en ålder och se till att det är ett giltigt heltal
def read_age():
    while True:
        text = input("Ange ålder: ").strip()
        try:
            age = int(text)
        except ValueError:
            print("Fel: åldern måste vara ett heltal, t.ex. 17.")
            continue
        if 0 <= age <= 130:
            return age
        print("Fel: åldern måste vara mellan 0 och 130.")


# Hjälpfunktion: Linjär sökning efter en användare med en viss e-post.
# Returnerar användarens index i listan, eller -1 om den inte finns.
def find_index_by_email(users, email):
    for i in range(len(users)):
        if users[i]["email"] == email:
            return i
    return -1


# Hjälpfunktion: Skriv ut en användare på ett snyggt sätt
def print_user(user):
    print(f"  {user['name']:<20} {user['age']:>4} år   {user['email']}")


# Funktion: Lägg till en användare
def add_user(users):
    name, email = read_name_and_email()  # Packar upp tuplen

    # Kontrollera att e-postadressen inte redan finns
    if find_index_by_email(users, email) != -1:
        print(f"Fel: e-postadressen {email} finns redan. Användaren sparades inte.")
        return

    age = read_age()

    user = {"name": name, "age": age, "email": email}
    users.append(user)
    print(f"Användaren {name} har lagts till.")


# Funktion: Sök efter en användare via namn eller e-post
def search_user(users):
    if not users:
        print("Det finns inga användare att söka bland.")
        return

    term = input("Sök på namn eller e-post: ").strip().lower()
    if term == "":
        print("Du måste skriva ett sökord.")
        return

    # Linjär sökning: gå igenom alla användare och spara de som matchar.
    # Sökningen matchar även delar av namnet, t.ex. "ann" hittar "Anna".
    results = []
    for user in users:
        if term in user["name"].lower() or term == user["email"]:
            results.append(user)

    if results:
        print(f"Hittade {len(results)} användare:")
        for user in results:
            print_user(user)
    else:
        print("Ingen användare matchade sökningen.")


# Funktion: Visa alla användare sorterade alfabetiskt efter namn
def show_users(users):
    if not users:
        print("Listan är tom.")
        return

    # sorted() skapar en ny sorterad lista, originallistan ändras inte.
    # key=lower gör att sorteringen inte bryr sig om stora/små bokstäver.
    sorted_users = sorted(users, key=lambda user: user["name"].lower())

    print(f"Alla användare ({len(users)} st), sorterade efter namn:")
    for user in sorted_users:
        print_user(user)


# Funktion: Ta bort en användare via e-postadress
def remove_user(users):
    email = input("Ange e-post för användaren som ska tas bort: ").strip().lower()
    index = find_index_by_email(users, email)

    if index == -1:
        print(f"Det finns ingen användare med e-postadressen {email}.")
        return

    removed = users.pop(index)
    print(f"Användaren {removed['name']} ({removed['email']}) har tagits bort.")


# Huvudfunktion: Sköter meny och programflöde
def main():
    users = []  # Här lagras användarna som dictionaries

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


# Starta programmet bara när filen körs direkt
if __name__ == "__main__":
    main()
