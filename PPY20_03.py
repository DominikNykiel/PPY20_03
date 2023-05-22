import random
import sys
import getpass

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
    for i in range(1, int(rounds) + 1):
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

            if int(choicePL) in range(1, 4):
                print("Wybrałeś ", rcp_list[int(choicePL) - 1])
                break
            else:
                print("Niepoprawna komenda!")
                continue

        print("Ruch gracza komputerowego...")
        choiceCPU = random.randint(0, 2)
        print("Komputer wybrał ", rcp_list[choiceCPU])

        choicePLtrue = rcp_list[int(choicePL) - 1]
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
    if score1p > score2p:
        print("Wygrywa gracz: ", player1)
    else:
        if score2p > score1p:
            print("Wygrywa gracz: ", player2)
        else:
            print("Remis!")
else:
    for i in range(1, int(rounds) + 1):
        print("Zaczyna się runda ", str(i))
        print("Ruch gracza pierwszego...")
        print("1 = papier, 2 = nożyce, 3 = kamień")
        while True:
            choicePL = getpass.getpass("Wybierz przedmiot...\n")

            try:
                a = int(choicePL)
            except ValueError:
                print("Niepoprawna liczba!")
                continue

            if int(choicePL) in range(1, 4):

                break
            else:
                print("Niepoprawna komenda!")
                continue

        print("Ruch gracza drugiego...")
        print("1 = papier, 2 = nożyce, 3 = kamień")
        while True:
            choiceP2 = getpass.getpass("Wybierz przedmiot...\n")

            try:
                a = int(choiceP2)
            except ValueError:
                print("Niepoprawna liczba!")
                continue

            if int(choiceP2) in range(1, 4):

                break
            else:
                print("Niepoprawna komenda!")
                continue

        choicePLtrue = rcp_list[int(choicePL) - 1]
        choiceP2true = rcp_list[int(choiceP2) - 1]

        if (choicePLtrue == "kamień" and choiceP2true == "nożyce") or (
                choicePLtrue == "nożyce" and choiceP2true == "papier") or (
                choicePLtrue == "papier" and choiceP2true == "kamień"):
            print("Wygrywa gracz 1 : ", player1)
            score1p += 1
        else:
            if (choicePLtrue == "nożyce" and choiceP2true == "kamień") or (
                    choicePLtrue == "papier" and choiceP2true == "nożyce") or (
                    choicePLtrue == "kamień" and choiceP2true == "papier"):
                print("Wygrywa gracz drugi : ", player2)
                score2p += 1
            else:
                print("Remis!")
    if score1p > score2p:
        print("Wygrywa gracz: ", player1)
    else:
        if score2p > score1p:
            print("Wygrywa gracz: ", player2)
        else:
            print("Remis!")
