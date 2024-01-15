import datetime
import matplotlib.pyplot as plt

GADA_LIKME = 0.05
IKGADA_INVESTICIJA = 20
uzkrajuma_konts = [0]

def sadalit_naudu(pieejama_nauda):
    izmaksas = {
        'Ēšana': 30,
        'Transportlīdzekļi': 20,
        'Izklaide': 15,
        'Citas izmaksas': 35
    }

    sadalijums = {k: (v / 100) * pieejama_nauda for k, v in izmaksas.items()}
    return sadalijums

pieejama_nauda_budzets = float(input("Ievadiet pieejamo naudu uz nedēļu: "))

izmaksu_sadalijums = sadalit_naudu(pieejama_nauda_budzets)

print("\nPrognozētais izmaksu sadalījums:")
for k, v in izmaksu_sadalijums.items():
    print(f"{k}: {v:.2f} EUR")
    
def ieguldijumi_uzkrajuma_konta(uzkrajuma_konts, ieguldijums):
    uzkrajuma_konts.append(ieguldijums)
    return uzkrajuma_konts

sodienas_datums = datetime.date.today()
atlikusie_dieni = 7 - sodienas_datums.weekday()
print(f"\nŠodienas datums: {sodienas_datums}")
print(f"Atlikušie dienas nedēlē: {atlikusie_dieni}")

kategorijas_budzets = izmaksu_sadalijums.keys()
izmaksu_summas_budzets = izmaksu_sadalijums.values()

plt.pie(izmaksu_summas_budzets, labels=kategorijas_budzets, autopct='%1.1f%%')
plt.title('Izmaksu sadalījums')
plt.show()

def ieguldijumi_uzkrajuma_konta(uzkrajuma_konts):
    ieguldijums = IKGADA_INVESTICIJA
    uzkrajuma_konts.append(uzkrajuma_konts[-1] + ieguldijums)
    return uzkrajuma_konts

for nedela in range(1, 53):
    uzkrajuma_konts = ieguldijumi_uzkrajuma_konta(uzkrajuma_konts)

gada_beigas_nauda = uzkrajuma_konts[-1] * (1 + GADA_LIKME)

print("\nInvestīciju un uzkrājuma konta prognoze katrā nedēlā:")
print(f"{'Nedēļa':<10}{'Uzkrājuma konta summa'   :<30}{'Piemaksa gada beigās':<25}")
print("-" * 75)

kopsumma_uzkrajums = 0

for i, summa in enumerate(uzkrajuma_konts[1:], start=1):
    kopsumma_uzkrajums += summa
    piemaksa_gada_beigas = kopsumma_uzkrajums * GADA_LIKME

    print(f"{i:<10}{summa:.2f} EUR{' ' * 5}{piemaksa_gada_beigas:.2f} EUR")

print(f"\nKopējā summa gada beigās ar {GADA_LIKME * 100}% likmi: {gada_beigas_nauda:.2f} EUR")


nedelas = list(range(1, 53))
plt.plot(nedelas, uzkrajuma_konts[1:], label='Uzkrājuma konta summa')
plt.xlabel('Nedēļa')
plt.ylabel('Summa EUR')
plt.title('Investīciju un uzkrājuma konta prognoze')
plt.legend()
plt.show()
