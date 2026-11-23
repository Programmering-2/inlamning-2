# Inlämning 2 – Testfall och kommentar

## Testfall jag har provat

| Test | Indata | Förväntat resultat | Resultat |
|---|---|---|---|
| Lägg till användare | Anna, 17, anna@example.com | Användaren sparas i listan. | ✅ Sparades |
| Fel ålder | Anna, sjutton, anna@example.com | Felmeddelande visas, programmet kraschar inte. | ✅ Felmeddelande, programmet frågar efter åldern igen |
| Negativ ålder | -3 | Felmeddelande, programmet frågar igen. | ✅ "Åldern kan inte vara negativ." |
| Dubblett av e-postadress | Bertil, anna@example.com | Den andra användaren sparas inte, tydligt meddelande visas. | ✅ Sparades inte, meddelande visades |
| Dubblett med stora bokstäver | Anna@Example.com | Räknas som samma e-post och sparas inte. | ✅ Sparades inte |
| Sök e-post | anna@example.com | Programmet hittar rätt användare. | ✅ Hittade Anna |
| Sök del av namn | ce | Programmet hittar Cecilia. | ✅ Hittade Cecilia |
| Visa sorterat | Anna, Bertil, Cecilia, adam (inlagda i den ordningen) | Användarna visas alfabetiskt efter namn. | ✅ adam, Anna, Bertil, Cecilia |
| Ta bort användare | anna@example.com | Rätt användare tas bort och finns inte längre i listan. | ✅ Anna borttagen, syns inte i listan |
| Ta bort okänd användare | saknas@example.com | Tydligt meddelande, programmet fortsätter. | ✅ Meddelande visades, menyn visas igen |
| Ogiltigt menyval | x | Felmeddelande, menyn visas igen. | ✅ "Ogiltigt val, försök igen." |
| Avsluta | 5 | Programmet avslutas. | ✅ "Programmet avslutas." |

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
