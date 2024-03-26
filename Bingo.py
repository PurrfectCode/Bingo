import numpy as np # Importera numpy för att göra arrayerna snabbare

def Bingo(BingoCard, BingoUser):
    sequence = []
    vertical = 0
    diagonalR = 0 # Diagonalt höger
    diagonalL = len(BingoCard[0]) - 1 # Diagonalt vänster

    # Kontrollera diagonalt till vänster
    for row in BingoCard:
        # Lägg till element från första elementet i den första raden till det sista elementet i den sista raden
        sequence.append(row[diagonalR])
        diagonalR += 1
        # Konvertera till en mängd så att vi kan kontrollera om samma nummer som användaren valt finns i BingoCard (sekvens)
        tuple_row = set(sequence)
        tuple_user = set(BingoUser)
        # Kontrollera mängderna
        if tuple_row.issubset(tuple_user):
            print("BINGO")
            return True

    # Kontrollera diagonalt till höger
    sequence = []
    for row in BingoCard:
        # Vi gör samma som ovan men minskar värdet istället för att öka det så att vi går från höger till vänster
        sequence.append(row[diagonalL])
        diagonalL -= 1
        tuple_row = set(sequence)
        tuple_user = set(BingoUser)
        if tuple_row.issubset(tuple_user):
            print("BINGO")
            return True
    
    # Kontrollera horisontellt
    for row in BingoCard:
        # Vi kontrollerar helt enkelt om varje rad matchar användarens val
        tuple_row = set(row)
        tuple_user = set(BingoUser)
        if tuple_row.issubset(tuple_user):
            print("BINGO")
            return True

    # Kontrollera vertikalt
    for _ in range(5):
        # Vi kontrollerar om det första elementet i alla rader matchar användarsekvensen, från första raden till den sista raden
        sequence = []
        for row in BingoCard:
            sequence.append(row[vertical])
        tuple_row = set(sequence)
        tuple_user = set(BingoUser)
        if tuple_row.issubset(tuple_user):
            print("BINGO")
            return True
        vertical += 1

    return False

def AddUserNumber(turn, UserNumbers): # Fråga användaren efter numren
     # Loopa tills ett giltigt värde returneras
     while True:
        # Försök förhindra fel med värdestyper (till exempel om användaren skriver in något annat än ett heltal)
        try:
            userNumber = int(input(f"{turn} : "))
            
            if userNumber in UserNumbers:
                print("\n\n[!] Fel [!] Du har redan valt det här numret.\n\n")
            # Validera att heltal inte är mindre än 1 eller större än 25
            elif userNumber < 1 or userNumber > 25:
                print("\n\n[!] Fel [!] Numret får inte vara större än 25 eller mindre än 1.\n\n")
            else:
                return userNumber
        # Kastar undantag om vi hittar ett fel med värdestypen
        except ValueError:
            print("\n\n[!] Fel [!] Du måste skriva ett heltal.\n\n")
    

def GenerateBingoCard(): # Generera 5x5-brädet med slumpmässiga nummer från 1 till 25

    maxNumberInArray = 25
    maxNumberCount = 25

    # Generera en 5x5-vektor med slumpmässiga nummer från 1 till 25
    # Använder även numpy eftersom det använder mindre utrymme än en vanlig array (minnesmässigt)
    gameBoard = np.random.choice(np.arange(1, maxNumberInArray + 1), maxNumberCount, replace=False).reshape(5, 5)

    return gameBoard

# Koden kommer bara att köras om skriptet körs som huvudprogram
if __name__ == '__main__':
    # Skapa en tom array för att lagra användarens val
    UserSequence = []

    bingoCard = GenerateBingoCard()

    print(bingoCard)

    print("-" * 20)
    print("Välj dina nummer: \n")

    # Lagra användarens val i arrayen "UserSequence"
    for turn in range(10):
        user_pick = AddUserNumber(turn + 1, UserSequence)
        UserSequence.append(user_pick)

    print("-" * 20 + "\n")
    print("[+][+] Nummer valda! [+][+]\n")

    # Visa numren som användaren valt
    for number in range(len(UserSequence)):
        print(f"|\tNummer {number + 1} : {UserSequence[number]}\t|")
    print("\n\n")
    
    # Generera Bingo-kortet

    result = Bingo(bingoCard, UserSequence)

    if not result:
        print("Du förlorade")
        print("Programmet avslutat")