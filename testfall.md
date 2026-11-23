# Inlämning 2 – Testfall och kommentar

## Testfall jag har provat

| Test | Indata | Förväntat resultat | Resultat |
|---|---|---|---|
| Lägg till användare | Anna, 17, anna@example.com | Användaren sparas i listan. | ✅ Godkänt |
| Fel ålder | Anna, sjutton, anna@example.com | Programmet visar felmeddelande och kraschar inte. | ✅ Godkänt |
| Dubblett av e-postadress | Lägg till två användare med anna@example.com | Den andra användaren sparas inte och ett tydligt meddelande visas. | ✅ Godkänt |
| Sök e-post | anna@example.com | Programmet hittar rätt användare. | ✅ Godkänt |
| Visa sorterat | Flera användare i osorterad ordning | Användarna visas alfabetiskt efter namn. | ✅ Godkänt |
| Ta bort användare | anna@example.com | Rätt användare tas bort och finns inte längre i listan. | ✅ Godkänt |
| Ta bort okänd användare | saknas@example.com | Programmet visar ett tydligt meddelande och fortsätter. | ✅ Godkänt |

## Hur jag använde listor, dictionaries och tuple

- **Lista:** Alla användare lagras i listan `users`.
- **Dictionary:** Varje användare är en dictionary med nycklarna `name`, `age` och `email`,
  t.ex. `{"name": "Anna", "age": 17, "email": "anna@example.com"}`. Då kan varje värde
  hämtas med ett tydligt namn.
- **Tuple:** Funktionen `read_name_and_email()` returnerar namn och e-post som en tuple,
  som packas upp med `name, email = read_name_and_email()`.
- **Sökning:** Linjär sökning – programmet går igenom listan en användare i taget,
  både i `search_user()` och i `find_index_by_email()`.
- **Sortering:** `sorted(users, key=lambda user: user["name"].lower())` sorterar efter namn
  utan att bry sig om stora och små bokstäver. Originallistan ändras inte.
- **Dubbletter:** E-post sparas med små bokstäver, och `find_index_by_email()` används för att
  kontrollera att adressen inte redan finns innan en ny användare läggs till.
