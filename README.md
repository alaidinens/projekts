# Projekts Nedēļas Budžeta Plānotājs

## Apraksts
Es izvēlejos izdarīt programmu, kura man, ka studentam palīdzēs efektīvi plānot un uzraudzīt manas izmaksas uz nedēļu. Programma automātiski sadala pieejamo naudu procentuāli dažādām izmaksu kategorijām, un var uzraudzīt savu tēriņu. Kā arī es izvēlejos investēt 20 eiro katru nedēļu uz uzkrājuma kontu, kuras ir likme 5% gadā, jo gribas domāt par savu nākotni arī.

## Izmantotās Python bibliotēkas
Šajā porgrammā tika lietotas sekojošas bibliotekas:
- `input`: Lai iegūtu lietotāja ievadi par pieejamo naudu.
- `datetime`: Lai noteiktu nedēļas dienas un veiktu savlaicīgus paziņojumus par plānotajām izmaksām.
- `matplotlib`: Lai veiktu vizuālu izmaksu datu attēlojumu.

## Programmatūras izmantošana
1. Vispirms ir jāievada kopējo summu, cik plānojat tērēt uz nedēļu.
2. Pēc tam programma automātiski sadala naudu procentuāli dažādām izmaksu kategorijām.
3. Sekojiet prognozētajam izmaksu sadalījumam dienas un kopējās nedēļas laikā.
4. **Ieguldījums:** Katru nedēļu automātiski tiks ieguldīti 20 eiro, kuras tiek pārskaitītas uz uzkrājuma kontu ar 5% likmi.
5. Katras dienu programma paziņo par to, cik lielā apmērā jau ir iztērēta no plānotajām izmaksām un cik uzkrāta nauda no ieguldījumiem.

## Papildus iespējas
- Katru dienu paziņot par esošo naudas atlikumu un atlikušo dienu skaitu nedēlē.
- Vizuāls attēlojums: Izmantojot `matplotlib`, programma automātiski veido grafisku izmaksu diagrammu, lai lietotājiem būtu vieglāk izprast savu izdevumu struktūru.
- **Uzkrājuma aprēķini:** Aprēķina un uzkrāj uzkrājuma peļņu tabulā, piedāvājot prognozes par uzkrājuma veiksmi katru nedēlu un galējo uzrkājumu gadā beigās.
