import random
import sys

# Zad1


# numbers = input("wprowadz ciąg cyfr, rozdzielonych przecinkami\n")

# Zad2
# cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
#
# placesToVisit = input("podaj liczbę miejsc do odwiedzenia\n")
#
# try:
#    a = int(placesToVisit)
# except ValueError:
#    print("Nieprawidłowa liczba!\n")
#    sys.exit()
#
# print("Oto twój plan wycieczki\n")
# cities_list = cities.split(",")
#
# for i in range(0, int(placesToVisit)):
#    print(cities_list.pop(random.randint(0, len(cities_list) - 1)))
#
# print("Miłej wycieczki!")

# Zad3
rcp_list = ["papier", "nożyce", "kamień"]

print("Witaj w grze papier-kamień-nożyce!")

while True:
    rounds = input("Wybierz ilośc rund\n")
    try:
        a = int(rounds)
    except ValueError:
        print("Niepoprawna liczba!")
        continue
    break

print(rounds)

while True:
    gameMode = input("Wybierz tryb gry - |1p| by zagrać przeciwko CPU,"
                     " |2p| by zagrać przeciwko innemu graczowi\n")
    if gameMode == "1p" or gameMode == "2p":
        break
    else:
        print("Nieprawidłowa komenda!")
        continue

player1 = input("Wprowadz imię pierwszego gracza\n")
player2 = input("Wprowadz imię drugiego gracza\n")

if gameMode == "1p":
    player2 += " (CPU)"

score1p = 0
score2p = 0

if gameMode == "1p":
    for i in range(1, rounds + 1):
        print("Zaczyna się runda ", str(i))
        print("Ruch gracza pierwszego...")
        print("1 = papier, 2 = nożyce, 3 = kamień")
        while True:
            choicePL = input("Wybierz przedmiot...\n")

            try:
                a = int(choicePL)
            except ValueError:
                print("Niepoprawna liczba!")
                continue

            if choicePL in range(1, 4):
                print("Wybrałeś ", rcp_list[choicePL - 1])
                break
            else:
                print("Niepoprawna komenda!")
                continue

        print("Ruch gracza komputerowego...")
        choiceCPU = random.randint(0, 2)
        print("Komputer wybrał ", rcp_list[choiceCPU])

        choicePLtrue = rcp_list[choicePL - 1]
        choiceCPUtrue = rcp_list[choiceCPU]

        if (choicePLtrue == "kamień" and choiceCPUtrue == "nożyce") or (
                choicePLtrue == "nożyce" and choiceCPUtrue == "papier") or (
                choicePLtrue == "papier" and choiceCPUtrue == "kamień"):
            print("Wygrywa gracz 1 : ", player1)
            score1p += 1
        else:
            if (choicePLtrue == "nożyce" and choiceCPUtrue == "kamień") or (
                    choicePLtrue == "papier" and choiceCPUtrue == "nożyce") or (
                    choicePLtrue == "kamień" and choiceCPUtrue == "papier"):
                print("Wygrywa gracz komputerowy : ", player2)
                score2p += 1
            else:
                print("Remis!")