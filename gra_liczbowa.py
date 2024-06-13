import random

class GraLiczbowa:
    def __init__(self, number=None, maks_proby=3):
        self.liczba = number if number is not None else random.randint(1, 10)
        self.maks_proby = maks_proby
        self.proby = 0
        self.wygrana = False

    def zgadnij(self, strzal):
        if self.proby >= self.maks_proby:
            raise Exception("Przekroczono maksymalną liczbę prób")
        self.proby += 1
        if strzal == self.number:
            self.wygrana = True
            return "Gratulacje! Zgadłeś!"
        elif self.proby == self.maks_proby:
            return f"Nie zgadłeś! Prawidłowa liczba to {self.number}."
        else:
            return "Spróbuj jeszcze raz!"

if __name__ == "__main__":
    gra = GraLiczbowa()
    print("Zgadnij liczbę od 1 do 10.")
    while not gra.wygrana and gra.proby < gra.maks_proby:
        strzal = int(input("Twój strzał: "))
        print(gra.zgadnij(strzal))
