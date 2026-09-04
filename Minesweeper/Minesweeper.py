import tkinter as tk
import random
import sys

sys.setrecursionlimit(2000)
#Supossedly this is needed?


window = tk.Tk()
window.title("Minesweeper")
window.geometry("400x400")

def flag(event, r, c):
    print(f"Report: Location {r} {c} Likely Bomb")
    button = buttons[r][c]
    if button["state"] == "disabled":
        return
    else:
        if button["text"] != "🚩":
            button["text"] = "🚩"
        else:
            button["text"] = ""

def sonar(event, r, c):
    print("Report: Sonar Sucessful")
    global energy
    if energy > 500:
        energy -= 500
        item = field[r][c]
        button = buttons[r][c]
        tl = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(-1, 1),(1, -1),(-1, -1)]
        for i in tl:
            bn = buttons[r + i[0]][c + i[1]]
            bn["text"] = field[r + i[0]][c + i[1]]
        print(f"Sonar Run: Total energy = {energy}")

energy = 0
def onclick(r, c):
    global gameOver
    if not gameOver:
        button = buttons[r][c]
        if button["text"] != "🚩":
            if field[r][c] == 9:
                print("Report: Bomb Hit!")
                for i in range(Nrows):
                    for j in range(Ncols):
                        buttons[i][j]["state"] = "disabled"
                        buttons[i][j].config(relief = tk.SUNKEN)
                        if field[i][j] == 9:
                            buttons[i][j].config(disabledforeground = "black")
                            if buttons[i][j]["text"] != "🚩":
                                buttons[i][j]["text"] = "💣"
                            else:
                                buttons[i][j]["text"] = "✅"
                        else:
                            if buttons[i][j]["text"] == "🚩":
                                buttons[i][j]["text"] = "❌"
                button["text"] = "💥"
            elif field[r][c] > 0:
                print(f"Report: Location no Bomb. Found {field[r][c]} bombs adjecent, could not pinpoint")
                button.config(relief = tk.SUNKEN)
                button["state"] = "disabled"
                button["text"] = field[r][c]
                button.config(disabledforeground = colors[field[r][c]])
        
            else:
                global energy
                pe = 0
                for i in range(energy):
                    pe += 1
                global energies
                energies = []
                def neighborUp(x, y):
                    global energies
                    buttons[x][y].config(relief = tk.SUNKEN)
                    if buttons[x][y]["state"] == "disabled":
                        return
                    buttons[x][y]["state"] = "disabled"
                    buttons[x][y]["text"] = 0
                    buttons[x][y].config(relief = tk.SUNKEN)

                    if field[x][y] == 0:
                        energies.append(0)
                        tl = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(-1, 1),(1, -1),(-1, -1)]
                        e = search_around(x, y, field)
                        """for q in e:
                            if q == 9:
                                return"""
                        for i in range(len(e)):
                            if e[i] != 9 and e[i] != None:
                                item = tl[i]
                                pos = (x + item[0], y + item[1])
                                if not ((pos[0] < 0 or pos[0] >= Nrows) or (pos[1] < 0 or pos[1] >= Ncols)):
                                    neighborUp(x + item[0], y + item[1])
                    else:
                        nb = buttons[x][y]
                        nb["text"] = field[x][y]
                        nb.config(disabledforeground = colors[field[x][y]])
                neighborUp(r, c)
                energy += len(energies)
                print(f"Report: Massive no bomb area. Collecting {energy - pe} power. Total energy is {energy}")
            print(f"Report: You can perform {energy//500} sonar locators")
        else:
            pass
    p = 0
    for i in buttons:
        for j in i:
            if j["state"] != "disabled":
                p = 1
    if p == 0:
        gameOver = True
        print("Report: Mine Cleared")
    else:
        gameOver = False

gameOver = False
Nrows = 30
Ncols = 30  
#Approx
MineRatio = 10
Nmines = MineRatio * (Nrows*Ncols//100)

colors = ["white", "blue", "green", "red", "dark blue", "brown", "cyan", "black", "gray"]

buttons = []

def create_field():
    field = [[0 for _ in range(Ncols)] for _ in range(Nrows)]
    return field

field = create_field()
for i in range(Nrows):
  buttons.append([])
  for j in range(Ncols):
    b = tk.Button(window, command = lambda r = i, c = j: onclick(r, c))
    b.bind("<Enter>", lambda event, btn=b: btn.focus_set())
    b.bind("<Button-2>", lambda event, r = i, c = j: flag(event, r, c))
    b.bind("b", lambda event, r = i, c = j: sonar(event, r, c))
    #mac right click/windows middle click      
    b.grid(row=i, column = j)
    b["width"] = 1
    b["font"] = 40
    b["text"] = " "

    buttons[i].append(b)

def reset(event):
    print("Reset")
    field = create_field()
    summon_bombs()
    for i in buttons:
        for j in i:
            j["state"] = "active"
            j["text"] = ""

window.bind("<a>", reset)


def display_field(field):
    for i in field:
       print(i)




def search_around(x, y, field):
    def search(x, y):
        if 0 <= x < len(field) and 0 <= y < len(field[0]):
            return field[x][y]
        return None

    around = []
    around.append(search(x + 1, y))
    around.append(search(x - 1, y))
    around.append(search(x, y + 1))
    around.append(search(x, y - 1))
    around.append(search(x + 1, y + 1))
    around.append(search(x - 1, y + 1))
    around.append(search(x + 1, y - 1))
    around.append(search(x - 1, y - 1))
    return around

def summon_bombs(): 
    locations = [x for x in range(Nrows*Ncols)] 
    mines = random.sample(locations, Nmines)

    mineTuples = []
    for i in mines:
        row = i//Ncols
        col = i%Ncols
        mineTuples.append((row, col))

    for i in range(len(mineTuples)):
        row = mineTuples[i][0]
        col = mineTuples[i][1]
        field[row][col] = 9
    for i in range(Nrows):
        for j in range(Ncols):
            if field[i][j] == 9:
                continue  
            around = around = search_around(i, j, field)
            number = 0
            for t in around:
                if t == 9:
                    number += 1
            field[i][j] = number

    #display_field(field)
for i in range(Nrows):
    for j in range(Ncols):
        button = buttons[i][j]
print("You have been assigned to examine an old minefield, be careful. Remember this is console intergrated")
print("""Instructions:
<Left Click> : Test Location for Bomb
<Right Click> : Flag Location for Bomb
<b key> : Perform High Energy Sonar
""")
summon_bombs()

tk.mainloop()