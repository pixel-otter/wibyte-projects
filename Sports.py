import csv

def readcsv(name):
    filename = name + ".csv"
    with open(filename, mode = "r") as file:
        csvFile = csv.DictReader(file)
        tournament_data = list(csvFile)
    return tournament_data

def pad(val, n):
    return str(val).ljust(n)

def init():
    filename = "Analysis.dat"
    with open(filename, mode = "w") as file:
        file.write("Results")

init()
WimbledonData = readcsv("WorldChampionship")
FrenchOpenData = readcsv("WorldCup")
#I am using old names but this is for chess

def printline(data):
    filename = "Analysis.dat"

    with open(filename, mode = "a") as file:
        file.write(data)

def printtable(datadict):
    for i in datadict:
        for j in i:
            printline((pad(j, 30)))
        printline("\n")
        break
    for i in datadict:
        for j in i:
            printline((pad(i[j], 30)))
        printline("\n")

def analyze(name, data):
    
    def analyzeStreaks(wonlist,namelist):
        continuity = []
        for i in namelist:
            continuity.append(i["Year"])
        print(continuity)
        yearswon = sorted(list(map(int, wonlist)))
        yd = []
        for i in range(len(yearswon)):
            j = yearswon[i]
            item1 = continuity.index((str(j)))
        for i in range(len(yearswon)):
            if not i == 0:
                diff = continuity.index((str(yearswon[i]))) - continuity.index((str(yearswon[i - 1])))
            else:
                diff = 1
            yd.append(diff)

        max = 0
        streak = 0
        for i in range(len(yd)):
            if yd[i] == 1:
                streak += 1
            else:
                streak = 0
            if streak > max:
                max = streak
        return max

        
    winners = []

    for i in data:
        winners.append(i["Winner"])

    uniqueWinners = set(winners)

    printline("")
    printline("")

    printline(f"\n{name} Data\n")
    printline(f"Total Games: {len(winners)}\n")
    printline(f"Unique Winners: {len(uniqueWinners)}\n")

    printline("Games: \n")

    printtable(data)

    winnerInfo = []

    for i in uniqueWinners:
        info = {}
        selected = [chosen for chosen in data if chosen["Winner"] == i]

        info["Name"] = i
        info["Country"] = selected[0]["Country"]
        info["Times Won"] = len(selected)
        info["Years Won"] = []
        for year in selected:
            info["Years Won"].append(year["Year"])

        winnerInfo.append(info)
    multiWinners = set()

    for i in uniqueWinners:
        multiWinners.add(i)

    for i in uniqueWinners:
        selected = [chosen for chosen in winnerInfo if chosen["Name"] == i]
        if selected[0]["Times Won"] == 1:
            multiWinners.remove(i)

    winningstreaks = []

    for i in multiWinners:
        selectedNew = [chosen for chosen in winnerInfo if chosen["Name"] == i]
        streaks = {}
        streaks["Name"] = i
        streaks["Longest"] = analyzeStreaks(selectedNew[0]["Years Won"], data)
        winningstreaks.extend([streaks])

    return uniqueWinners, winningstreaks


WimbledonWinners, WimbledonMulti = analyze("Chess World Champion", FrenchOpenData)
FrenchOpenWinners, FrenchOpenMulti = analyze("Chess World Cup", WimbledonData)

#The swap is intentional

AllWinners = WimbledonWinners | FrenchOpenWinners
BothWinners = WimbledonWinners & FrenchOpenWinners
WimbledonOnly = WimbledonWinners - FrenchOpenWinners
FrenchOpenOnly = FrenchOpenWinners - WimbledonWinners
NotBothWinners = WimbledonWinners ^ FrenchOpenWinners

printline("\nlist of all players who have won Chess World Championship and/or Chess World Cup\n")

for i in AllWinners:
    printline(i + "\n")

printline("\nlist of all players who have won both Chess World Championship and Chess World Cup\n")

for i in BothWinners:
    printline(i + "\n")

printline("\nlist of all players who have won Chess World Championship but not Chess World Cup\n")

for i in FrenchOpenOnly:
    printline(i + "\n")

printline("\nlist of all players who have won Chess World Cup but not Chess World Championship\n")

for i in WimbledonOnly:
    printline(i + "\n")

printline("\nlist of all players who have won either Chess World Cup or Chess World Championship but not both\n")

for i in NotBothWinners:
    printline(i + "\n")

printline("\nstreaks of all players who have won the world championship more than once\n")

printtable(FrenchOpenMulti)

printline("\nstreaks of all players who have won the world cup more than once\n")

printtable(WimbledonMulti)
