# Inlämning 2 – Testfall och kommentar

## Testfall

| Test | Indata | Förväntat resultat | Resultat |
|---|---|---|---|
| Lägg till användare | Anna, 17, anna@example.com | Användaren sparas i listan. | ✅ Godkänt |
| Fel ålder | Anna, sjutton, anna@example.com | Programmet visar felmeddelande och kraschar inte. | ✅ Godkänt |
| Dubblett av e-postadress | Lägg till två användare med anna@example.com | Den andra användaren sparas inte och ett tydligt meddelande visas. | ✅ Godkänt |
| Sök e-post | anna@example.com | Programmet hittar rätt användare. | ✅ Godkänt |
| Visa sorterat | Flera användare i osorterad ordning | Användarna visas alfabetiskt efter namn. | ✅ Godkänt |
| Ta bort användare | anna@example.com | Rätt användare tas bort och finns inte längre i listan. | ✅ Godkänt |
| Ta bort okänd användare | saknas@example.com | Programmet visar ett tydligt meddelande och fortsätter. | ✅ Godkänt |
