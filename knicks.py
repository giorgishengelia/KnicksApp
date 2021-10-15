class Player:
    Name = ""
    Points = 0
    Rebounds = 0
    Assists = 0

players = []

f = open("knicks.txt")
records = f.read().split("\n")
f.close()

for rec in records:
    cols = rec.split(" ")
    p = Player()
    p.Name = cols[0]
    p.Points = int(cols[1])
    p.Rebounds = int(cols[2])
    p.Assists = int(cols[3])
    players.append(p)
    
    

def MostScorer(players):
    most = players[0]
    
    for p in players:
        if p.Points > most.Points:
            most = p
    
    print(most.Name, "is the most scorer.")
    

def DoubleDouble(players):
    for p in players:
        if (p.Points > 9 and p.Rebounds > 9) or (p.Points > 9 and p.Assists > 9) or (p.Rebounds > 9 and p.Assists > 9):
            print(p.Name, "did double double.")
        

while(True):
    print("1- Most Scorer Player")
    print("2- Double-Double")
    print("3- Triple-Double")
    print("4- Report")
    print("0- Exit")
    choice = int(input("Choice:"))
    
    if choice == 1:
        MostScorer(players)
        
    if choice == 2:
        DoubleDouble(players)
    if choice == 0:
        break






