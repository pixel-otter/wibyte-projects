import csv
import random
import bisect # Full Insertion sort Module

def findmax(lst): 
    return len(max(lst, key=len)) if lst else 0

def pad(value, length): 
    spaces = " " * (length - len(value)) 
    return value + spaces

def DisplayDictionary(dictionary): 
    max_len = findmax(dictionary)
    for key, value in dictionary.items():
        print(f"{pad(str(key), max_len)} : {value}")


def MeanStandard(list):
    Mean = sum(list)
    Mean = Mean/len(list)
    return Mean

def MeanListList(listlist):
    Means = []
    for i in listlist:
        Mean = sum(i)
        Mean = Mean/len(i)
        Means.append(float(round(Mean, 2)))
    return Means

def InsertionSort(list):
    end = []
    for i in range(len(list)):
      bisect.insort(end, list[i])  
    return end

with open("TopTrumpsAnimals.csv", mode = "r") as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)
order = [1, 1, 0, 1, 0]
releventKeys = list(all_cards[0].keys())
releventKeys = releventKeys[2::]

random.shuffle(all_cards)

PlayerCards = all_cards[::4] + all_cards[2::4]
ComputerCards = all_cards[1::4] + all_cards[3::4]
TableCards = []

RankedHeight = []
for i in all_cards:
    RankedHeight.append(float(i["Height (ft)"]))

RankedHeight = InsertionSort(RankedHeight)

RankedFloors = []
for i in all_cards:
    RankedFloors.append(float(i["NumFloors"]))

RankedFloors = InsertionSort(RankedFloors)

RankedYearAge = []
for i in all_cards:
    RankedYearAge.append(float(i["Year Built"]))

RankedYearAge = InsertionSort(RankedYearAge)
invert = []
for i in range(len(RankedYearAge) - 1, -1, -1):
    invert.append(float(RankedYearAge[i]))
RankedYearAge = invert

RankedFloorSpace = []
for i in all_cards:
    RankedFloorSpace.append(float(i["Floor Space (million sq ft)"]))

RankedFloorSpace = InsertionSort(RankedFloorSpace)

RankedTimeBuild = []
for i in all_cards:
    RankedTimeBuild.append(float(i["Time to Build (yrs)"]))

RankedTimeBuild = InsertionSort(RankedTimeBuild)

invert = []
for i in range(len(RankedTimeBuild) - 1, -1, -1):
    invert.append(RankedTimeBuild[i])
RankedTimeBuild = invert

Names = []
for i in all_cards:
    Names.append(i["Individual"])

tKeys = [j for i in releventKeys for j in i if j == i[0]]
mKeys = dict.fromkeys(tKeys)

for i in range(len(tKeys)):
    j = tKeys[i]
    mKeys[j] = releventKeys[i]


print("Top Trumps Aresenal")
rb = input("This new varient on the classic top trumps game is way more interesting and way more crazy! Do you need a rulebook(y/n)")
if rb == "y":
    print("So, you/conmputer pick up a card and whos turn it is they pick a category(H/N/Y/F/T) and compare... but wait!\n theres more!\n The computer has acess to their whole deck, but you can pick 2 cards on your turn and use both!")

flip = ["player", "computer"]
chance = random.choice(flip)

while len(PlayerCards) > 0 and len(ComputerCards) > 0:
    player = PlayerCards.pop(0)
    player2 = None
    if chance == "player":
        player2 = PlayerCards.pop(random.randint(0, len(PlayerCards)))
    computer = ComputerCards.pop(0)
    TableCards.extend([player, computer]) #Just quicker
    print("Your Card is:")
    DisplayDictionary(player)
    if player2:
        print("Second Aresnal")
        DisplayDictionary(player2)

    if chance == "player":
        val = ""
        while not val in mKeys:
            val = input("Pick any item for comparison")
        chosen = mKeys[val]
        value = list(mKeys.keys()).index(val)
        chance = "computer"
    elif chance == "computer":
        chosen = random.choice(releventKeys)
        chance = "player"
        
        #Ranks
        RankHeight = RankedHeight.index(float(computer["Height (ft)"]))
        RankFloor = RankedFloors.index(float(computer["NumFloors"]))
        RankYear = RankedYearAge.index(float(computer["Year Built"]))
        RankSpace = RankedFloorSpace.index(float(computer["Floor Space (million sq ft)"]))
        RankTime = RankedTimeBuild.index(float(computer["Time to Build (yrs)"]))

        #This is the same as looking in your cards and finding the max you dont have
        unavailableHeight = RankedHeight.index(min(float(item["Height (ft)"]) for item in PlayerCards))
        unavailableFloor = RankedFloors.index(min(float(item["NumFloors"]) for item in PlayerCards))
        unavailableAge = RankedYearAge.index(max(float(item["Year Built"]) for item in PlayerCards))
        unavailableSpace = RankedFloorSpace.index(min(float(item["Floor Space (million sq ft)"]) for item in PlayerCards))
        unavailableTimeBuild = RankedTimeBuild.index(max(float(item["Time to Build (yrs)"]) for item in PlayerCards))
        t = []

        if RankHeight > unavailableHeight:
            t.append("h")
        if RankFloor > unavailableFloor:
            t.append("f")
        if RankYear < unavailableAge:
            t.append("a")
        if RankSpace > unavailableSpace:
            t.append("s")
        if RankTime < unavailableTimeBuild:
            t.append("b")

        ranks = [RankHeight, RankFloor, RankYear, RankSpace, RankTime]
        if len(t) < 1:
            chosen = releventKeys[ranks.index(max(ranks))]
        else:
            if t[0] == "h":
                chosen = "Height (ft)"
            elif t[0] == "f":
                chosen = "NumFloors"
            elif t[0] == "a":
                chosen = "Year Built"
            elif t[0] == "s":
                chosen = "Floor Space (million sq ft)"
            elif t[0] == "b":
                chosen = "Time to Build (yrs)"
            else:
                raise("Error in Choosing. Game over from technical issues")
        print(f"The computer picked {chosen}")
        value = list(mKeys.values()).index(chosen)
    else:
        raise("Error in Flip. Game over from technical issues")

        

    playerVal = player[chosen]
    if player2:
        if (player[chosen] < player2[chosen] and order[value] == 1) or (player[chosen] > player2[chosen] and order[value] == 0):
            playerVal = player2[chosen]
    computerVal = computer[chosen]
    print(order[value])

    if (float(playerVal) > float(computerVal) and order[value] == 1) or (float(computerVal) > float(playerVal) and order[value] == 0):
        won = "player"
    elif playerVal == computerVal:
        won = "draw"
    else:
        won = "computer"
    if won == "player":
        PlayerCards.extend(TableCards)
        TableCards = []
    elif won == "computer":
        ComputerCards.extend(TableCards)
        TableCards = []
    else:
        continue

    print("Computer Card is:")
    DisplayDictionary(computer)

    if won == "player":
        print("You Win Round")
    elif won == "computer":
        print("You Lose Round")
    else:
        print("Draw")
    
    print(f"Number of Cards you have {len(PlayerCards)}\n Number of Cards the computer has {len(ComputerCards)} \n Number of Cards in the table {len(TableCards)}")
