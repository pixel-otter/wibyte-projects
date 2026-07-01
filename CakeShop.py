import tkinter as tk
import os
from colorama import Back

#Sorry, still dont know how to bring this properly. Please copy paste this in your repositary.

def append_s(n):
    return n+"s"

def pad(val, n):
    return str(val).ljust(n)

print(pad("test", 10), "end")

def listdictsmax(list_of_dicts):
    m = 0
    for d in list_of_dicts:
        for val in d.values():
            if len(str(val)) > m:
                m = len(str(val))
    return m
#cake = {"Name": "Common Vanilla", "Flavor": "Vanilla", "Icing": "Vanilla", "Tiers": 1, "Sections": 5, "Filling": "Vanilla", "Size(cm)": 15, "Structure": "None", "Price(USD)": 25}

keys = ["Flavor", "Icing", "Filling", "Tiers", "Sections per tier", "Size", "Special Structure", "Price"]

masterDict = {}


masterDict["Flavor"] = ["Vanilla", "Chocolate", "Strawberry", "Lemon", "Mango", "Peach", "Blueberry"]
masterDict["Icing"] = ["Vanilla Icing", "Chocolate Icing", "Strawberry Icing", "Lemon Icing", "Mango Icing", "Blueberry Icing", "Pinapple Icing"]
masterDict["Filling"] = ["Vanilla Filling", "Chocolate Filling", "Strawberry Filling", "Lemon Filling", "Mango Filling", "Almond Filling", "Acai Filling"]
masterDict["Special Structure"] = ["None", "Town", "Stadium", "Aquarium", "Praire", "Berry Crown"]

Order = ["Flavor", "Icing", "Filling", 0, 0, 0, "Special Structure", 0, 0]

#I did not have the time to create 150 cakes so that is where you SHOULD use AI
Encoded = [
    [3,6,3,1,2,15,3,60],   # Classic Strawberry Dream
    [7,4,5,2,3,20,1,66],   # Royal Blueberry Wonder
    [6,5,3,3,4,25,6,100],   # Golden Peach Oasis
    [7,5,6,4,5,30,1,94],   # Midnight Blueberry Delight
    [4,2,4,5,2,35,4,120],   # Velvet Lemon Harmony
    [3,2,1,1,3,40,3,90],   # Crimson Strawberry Haven
    [7,3,5,2,4,15,2,70],   # Emerald Blueberry Symphony
    [2,4,7,3,5,20,4,92],   # Silver Chocolate Treat
    [2,5,4,4,2,25,5,110],   # Sunny Chocolate Splendor
    [2,5,3,5,3,30,6,128],   # Frosted Chocolate Crown
    [3,6,7,1,4,35,4,94],   # Whispering Strawberry Celebration
    [4,6,3,2,5,40,4,97],   # Sapphire Lemon Surprise
    [1,3,5,3,2,15,2,73],   # Imperial Vanilla Cascade
    [7,2,4,4,3,20,6,103],   # Radiant Blueberry Fantasy
    [5,1,2,5,4,25,2,101],   # Enchanted Mango Glow
    [2,7,1,1,5,30,6,91],   # Majestic Chocolate Jubilee
    [7,6,4,2,2,35,3,93],   # Rustic Blueberry Festival
    [1,3,5,3,3,40,4,111],   # Bloom Vanilla Charm
    [4,5,3,4,4,15,4,95],   # Harvest Lemon Bliss
    [2,5,7,5,5,20,4,109],   # Celestial Chocolate Garden
    [6,4,5,1,2,25,2,75],   # Classic Peach Dream
    [7,7,4,2,3,30,3,93],   # Royal Blueberry Wonder
    [4,2,6,3,4,35,3,96],   # Golden Lemon Oasis
    [6,4,6,4,5,40,6,122],   # Midnight Peach Delight
    [6,1,1,5,2,15,4,98],   # Velvet Peach Harmony
    [7,7,3,1,3,20,2,64],   # Crimson Blueberry Haven
    [1,2,3,2,4,25,2,78],   # Emerald Vanilla Symphony
    [3,1,3,3,5,30,2,92],   # Silver Strawberry Treat
    [6,4,7,4,2,35,1,102],   # Sunny Peach Splendor
    [5,5,4,5,3,40,3,124],   # Frosted Mango Crown
    [3,2,6,1,4,15,1,60],   # Whispering Strawberry Celebration
    [4,4,7,2,5,20,3,82],   # Sapphire Lemon Surprise
    [2,5,6,3,2,25,3,96],   # Imperial Chocolate Cascade
    [7,4,5,4,3,30,4,103],   # Radiant Blueberry Fantasy
    [7,5,6,5,4,35,3,113],   # Enchanted Blueberry Glow
    [6,3,1,1,5,40,6,99],   # Majestic Peach Jubilee
    [6,7,6,2,2,15,3,71],   # Rustic Peach Festival
    [4,4,7,3,3,20,2,81],   # Bloom Lemon Charm
    [6,3,1,4,4,25,5,107],   # Harvest Peach Bliss
    [4,6,1,5,5,30,1,105],   # Celestial Lemon Garden
    [4,3,1,1,2,35,2,83],   # Classic Lemon Dream
    [5,5,5,2,3,40,2,97],   # Royal Mango Wonder
    [5,2,2,3,4,15,1,77],   # Golden Mango Oasis
    [1,7,5,4,5,20,1,91],   # Midnight Vanilla Delight
    [5,6,5,5,2,25,4,106],   # Velvet Mango Harmony
    [5,1,2,1,3,30,4,80],   # Crimson Mango Haven
    [3,7,1,2,4,35,3,90],   # Emerald Strawberry Symphony
    [7,1,7,3,5,40,4,108],   # Silver Blueberry Treat
    [5,4,3,4,2,15,3,88],   # Sunny Mango Splendor
    [3,5,6,5,3,20,1,94],   # Frosted Strawberry Crown
    [6,4,3,1,4,25,3,76],   # Whispering Peach Celebration
    [5,4,1,2,5,30,5,98],   # Sapphire Mango Surprise
    [4,1,3,3,2,35,5,112],   # Imperial Lemon Cascade
    [2,2,4,4,3,40,6,130],   # Radiant Chocolate Fantasy
    [6,4,3,5,4,15,5,110],   # Enchanted Peach Glow
    [1,2,6,1,5,20,3,65],   # Majestic Vanilla Jubilee
    [1,7,6,2,2,25,1,71],   # Rustic Vanilla Festival
    [2,7,2,3,3,30,4,97],   # Bloom Chocolate Charm
    [4,6,1,4,4,35,6,119],   # Harvest Lemon Bliss
    [3,6,4,5,5,40,2,117],   # Celestial Strawberry Garden
    [1,5,1,1,2,15,2,61],   # Classic Vanilla Dream
    [3,6,1,2,3,20,5,87],   # Royal Strawberry Wonder
    [1,3,3,3,4,25,2,89],   # Golden Vanilla Oasis
    [7,3,2,4,5,30,3,107],   # Midnight Blueberry Delight
    [2,7,7,5,2,35,2,117],   # Velvet Chocolate Harmony
    [7,2,5,1,3,40,3,95],   # Crimson Blueberry Haven
    [4,1,2,2,4,15,1,60],   # Emerald Lemon Symphony
    [4,2,4,3,5,20,5,90],   # Silver Lemon Treat
    [7,1,6,4,2,25,6,108],   # Sunny Blueberry Splendor
    [4,3,7,5,3,30,5,118],   # Frosted Lemon Crown
    [2,3,4,1,4,35,6,96],   # Whispering Chocolate Celebration
    [5,2,5,2,5,40,4,102],   # Sapphire Mango Surprise
    [1,1,7,3,2,15,1,74],   # Imperial Vanilla Cascade
    [1,1,1,4,3,20,6,108],   # Radiant Vanilla Fantasy
    [2,3,6,5,4,25,5,118],   # Enchanted Chocolate Glow
    [7,5,6,1,5,30,5,92],   # Majestic Blueberry Jubilee
    [6,1,7,2,2,35,5,106],   # Rustic Peach Festival
    [3,3,5,3,3,40,2,97],   # Bloom Strawberry Charm
    [6,4,1,4,4,15,2,81],   # Harvest Peach Bliss
    [5,4,1,5,5,20,6,111],   # Celestial Mango Garden
    [5,4,4,1,2,25,5,81],   # Classic Mango Dream
    [6,2,5,2,3,30,4,91],   # Royal Peach Wonder
    [5,6,6,3,4,35,5,109],   # Golden Mango Oasis
    [6,6,4,4,5,40,3,115],   # Midnight Peach Delight
    [5,3,7,5,2,15,4,103],   # Velvet Mango Harmony
    [5,2,6,1,3,20,4,77],   # Crimson Mango Haven
    [6,7,1,2,4,25,6,99],   # Emerald Peach Symphony
    [2,7,4,3,5,30,2,97],   # Silver Chocolate Treat
    [4,4,5,4,2,35,1,96],   # Sunny Lemon Splendor
    [5,2,2,5,3,40,6,130],   # Frosted Mango Crown
    [7,2,5,1,4,15,3,62],   # Whispering Blueberry Celebration
    [5,4,1,2,5,20,6,88],   # Sapphire Mango Surprise
    [2,1,7,3,2,25,5,98],   # Imperial Chocolate Cascade
    [4,6,1,4,3,30,2,100],   # Radiant Lemon Fantasy
    [3,7,4,5,4,35,2,114],   # Enchanted Strawberry Glow
    [4,2,4,1,5,40,1,84],   # Majestic Lemon Jubilee
    [4,3,7,2,2,15,5,84],   # Rustic Lemon Festival
    [2,2,2,3,3,20,3,90],   # Bloom Chocolate Charm
    [7,1,7,4,4,25,4,108],   # Harvest Blueberry Bliss
    [1,5,7,5,5,30,3,107],   # Celestial Vanilla Garden
    [6,5,3,1,2,35,1,73],   # Classic Peach Dream
    [1,6,2,2,3,40,1,87],   # Royal Vanilla Wonder
    [4,6,6,3,4,15,1,71],   # Golden Lemon Oasis
    [3,7,7,4,5,20,1,85],   # Midnight Strawberry Delight
    [5,6,4,5,2,25,6,119],   # Velvet Mango Harmony
    [1,6,5,1,3,30,3,81],   # Crimson Vanilla Haven
    [6,1,4,2,4,35,1,87],   # Emerald Peach Symphony
    [2,3,1,3,5,40,2,105],   # Silver Chocolate Treat
    [4,6,1,4,2,15,1,85],   # Sunny Lemon Splendor
    [3,1,4,5,3,20,3,107],   # Frosted Strawberry Crown
    [7,1,2,1,4,25,6,82],   # Whispering Blueberry Celebration
    [3,5,2,2,5,30,6,96],   # Sapphire Strawberry Surprise
    [1,1,3,3,2,35,1,90],   # Imperial Vanilla Cascade
    [3,3,3,4,3,40,5,120],   # Radiant Strawberry Fantasy
    [1,3,2,5,4,15,5,104],   # Enchanted Vanilla Glow
    [1,1,5,1,5,20,4,74],   # Majestic Vanilla Jubilee
    [6,6,1,2,2,25,3,84],   # Rustic Peach Festival
    [6,7,6,3,3,30,2,94],   # Bloom Peach Charm
    [2,2,3,4,4,35,5,120],   # Harvest Chocolate Bliss
    [1,7,7,5,5,40,2,122],   # Celestial Vanilla Garden
    [7,7,2,1,2,15,5,78],   # Classic Blueberry Dream
    [2,3,5,2,3,20,6,85],   # Royal Chocolate Wonder
    [3,5,6,3,4,25,3,87],   # Golden Strawberry Oasis
    [5,4,3,4,5,30,5,109],   # Midnight Mango Delight
    [1,3,7,5,2,35,4,119],   # Velvet Vanilla Harmony
    [5,3,4,1,3,40,5,97],   # Crimson Mango Haven
    [5,1,4,2,4,15,5,81],   # Emerald Mango Symphony
    [1,4,7,3,5,20,6,99],   # Silver Vanilla Treat
    [4,1,2,4,2,25,2,97],   # Sunny Lemon Splendor
    [6,6,6,5,3,30,5,123],   # Frosted Peach Crown
    [3,2,2,1,4,35,6,101],   # Whispering Strawberry Celebration
    [5,2,3,2,5,40,5,111],   # Sapphire Mango Surprise
    [3,1,2,3,2,15,6,88],   # Imperial Strawberry Cascade
    [7,5,5,4,3,20,4,94],   # Radiant Blueberry Fantasy
    [7,7,6,5,4,25,6,116],   # Enchanted Blueberry Glow
    [3,6,4,1,5,30,6,90],   # Majestic Strawberry Jubilee
    [3,1,2,2,2,35,1,84],   # Rustic Strawberry Festival
    [2,3,7,3,3,40,1,98],   # Bloom Chocolate Charm
    [1,6,7,4,4,15,2,86],   # Harvest Vanilla Bliss
    [1,7,3,5,5,20,1,96],   # Celestial Vanilla Garden
    [6,5,2,1,2,25,4,82],   # Classic Peach Dream
    [2,5,2,2,3,30,5,100],   # Royal Chocolate Wonder
    [7,2,3,3,4,35,1,98],   # Golden Blueberry Oasis
    [2,7,4,4,5,40,6,121],   # Midnight Chocolate Delight
    [2,7,2,5,2,15,4,97],   # Velvet Chocolate Harmony
    [3,7,1,1,3,20,4,71],   # Crimson Strawberry Haven
    [3,4,5,2,4,25,3,81],   # Emerald Strawberry Symphony
    [4,4,2,3,5,30,1,87],   # Silver Lemon Treat
    [1,3,5,4,2,35,4,113],   # Sunny Vanilla Splendor
    [2,5,6,5,3,40,2,119],   # Frosted Chocolate Crown
]

n_cakes = len(Encoded)
for i in range(n_cakes):
    for j in range(len(Encoded[i])):
        if Order[j] != 0:
            Encoded[i][j] = Encoded[i][j] - 1

print(Encoded)
Decoded = []

for r in Encoded:
    xlist = []
    for j in range(len(r)):
        if Order[j] != 0:
            xlist.append(masterDict[Order[j]][r[j]])
        else:
            xlist.append(r[j])
    Decoded.extend([xlist])


allCakes = []

for i in range(len(Decoded)):
    new = dict.fromkeys(keys)
    for j in range(len(new)):
        new[keys[j]] = Decoded[i][j]
    allCakes.append(new)

window = tk.Tk() 
window.geometry("800x700")
window.title("Araty Sallys cakes and treats")

window.config(bg = "white")

def check_selection():
    flavor = selected_flavor.get()
    icing = selected_icing.get()
    filling = selected_filling.get()

    mint = MinTiers.get()
    maxt = MaxTiers.get()
    try:
        if type(int(mint)) == int:
            if not int(mint) <=0:
                pass
            else:
                mint = "no prefrence"
        else:
            mint = "no prefrence"
    except:
        mint = "no prefrence"
    
    try:
        if type(int(maxt)) == int:
            if not int(maxt) <=0:
                pass
            else:
                maxt = "no prefrence"
        else:
            maxt = "no prefrence"
    except:
        maxt = "no prefrence"


    minl = MinLayers.get()
    maxl = MaxLayers.get()
    try:
        if type(int(minl)) == int:
            if not int(minl) <=0:
                pass
            else:
                minl = "no prefrence"
        else:
            minl = "no prefrence"
    except:
        minl = "no prefrence"
    
    try:
        if type(int(maxl)) == int:
            if not int(maxl) <=0:
                pass
            else:
                maxl = "no prefrence"
        else:
            maxl = "no prefrence"
    except:
        maxl = "no prefrence"

    mins = MinSize.get()
    maxs = MaxSize.get()
    try:
        if type(int(mins)) == int:
            if not int(mins) <=0:
                pass
            else:
                mins = "no prefrence"
        else:
            mins = "no prefrence"
    except:
        mins = "no prefrence"
    
    try:
        if type(int(maxs)) == int:
            if not int(maxs) <=0:
                pass
            else:
                maxs = "no prefrence"
        else:
            maxs = "no prefrence"
    except:
        maxs = "no prefrence"

    minp = MinPrice.get()
    maxp = MaxPrice.get()
    try:
        if type(int(minp)) == int:
            if not int(minp) <=0:
                pass
            else:
                minp = "no prefrence"
        else:
            minp = "no prefrence"
    except:
        minp = "no prefrence"
    
    try:
        if type(int(maxp)) == int:
            if not int(maxp) <=0:
                pass
            else:
                maxp = "no prefrence"
        else:
            maxp = "no prefrence"
    except:
        maxp = "no prefrence"



    label.config(
        text=f"Selected Flavor: {flavor}\nSelected Icing: {icing}\nSelected Filling: {filling}\n The number of tiers between {mint} and {maxt} \n The number of layers per tier between {minl} and {maxl}\n Size is between {mins} and {maxs}\n for info on which cakes to buy, check console:"
    )

    full = []
    varMatch = [flavor, icing, filling, f"{mint}|{maxt}", f"{minl}|{maxl}", f"{mins}|{maxs}", f"{minp}|{maxp}"]

    for i in allCakes:
        on = 0
        for j in range(len(varMatch)):
            k = list(i)[j]
            if "no prefrence" in varMatch[j]:
                continue
            else:
                if "|" in varMatch[j]:
                    s1 = ""
                    s2 = ""
                    t = 0
                    for w in varMatch[j]:
                        if not w == "|":
                            if t == 0:
                                s1 = s1 + w
                            else:
                                s2 = s2 + w
                        else:
                            t = 1
                    try:
                        if i[k] < int(s1):
                            on = 1
                    except:
                        print(s1)
                        quit()

                    try:
                        if i[k] > int(s2):
                            on = 1
                    except:
                        print(s2)
                        quit()

                else:
                    if i[k] != varMatch[j]:
                        on = 1
        
        if on == 0:
            full.append(i)
    print(full)
    os.system("clear")
    print("Options")
    print("Based on your prefrences, here are the options:")
    maxlen = listdictsmax(full)
    print(maxlen)
    for i in keys:
        print(pad(i, maxlen), end = "\t")
    print("\n")
    x = 0
    for i in full:
        q = x
        for j in i:
            if j == "Flavor":
                print(f"{x + 1}.", end = "")
            if q%2 == 0:
                print(Back.RED + pad(i[j], maxlen), end = Back.BLACK + "\t")
            else:
                print(Back.YELLOW + pad(i[j], maxlen), end = Back.BLACK + "\t")
            q += 1
        x += 1

        print("\n")
    print("Please give input for cake")
    input("1 for first cake, 2 for second, so on... ")
    print("Your purchase is unsucessful")


options_flavor = []

options_flavor.append("no prefrence")
options_flavor.extend(masterDict["Flavor"])

options_icing = []

options_icing.append("no prefrence")
options_icing.extend(masterDict["Icing"])

options_filling = []

options_filling.append("no prefrence")
options_filling.extend(masterDict["Filling"])

selected_flavor = tk.StringVar(window)
selected_flavor.set(options_flavor[0]) 
selected_icing = tk.StringVar(window)
selected_icing.set(options_icing[0]) 
selected_filling = tk.StringVar(window)
selected_filling.set(options_icing[0]) 

FlavorChoice = tk.OptionMenu(window, selected_flavor, *options_flavor)
FlavorChoice.place(x=150, y=20)
FlavorLabel = tk.Label(window, text="prefered flavor")
FlavorLabel.place(x=10, y=20)

IcingChoice = tk.OptionMenu(window, selected_icing, *options_icing)
IcingChoice.place(x=150, y=60)
IcingLabel = tk.Label(window, text="prefered icing")
IcingLabel.place(x=10, y=60)

FillingChoice = tk.OptionMenu(window, selected_filling, *options_filling)
FillingChoice.place(x=150, y=100)
FillingLabel = tk.Label(window, text="prefered filling")
FillingLabel.place(x=10, y=100)

MinTiers = tk. Entry(window    )
MinTiers.place(x = 10, y = 160)

MaxTiers = tk. Entry(window)
MaxTiers.place(x = 250, y = 160)

TiersLabel = tk.Label(window, text="prefered Tiers")
TiersLabel.place(x = 150, y = 130)

btn = tk.Button(window, text="Show Selection", command=check_selection)
btn.place(x=400, y=30)

MinLayers = tk. Entry(window    )
MinLayers.place(x = 10, y = 210)

MaxLayers = tk. Entry(window)
MaxLayers.place(x = 250, y = 210)

LayerLabel = tk.Label(window, text="prefered Layers per Tier")
LayerLabel.place(x = 150, y = 180)

MinSize = tk. Entry(window    )
MinSize.place(x = 10, y = 260)

MaxSize = tk. Entry(window)
MaxSize.place(x = 250, y = 260)

SizeLabel = tk.Label(window, text="prefered Size(cm)")
SizeLabel.place(x = 150, y = 240)

MinPrice = tk. Entry(window    )
MinPrice.place(x = 10, y = 300)

MaxPrice = tk. Entry(window)
MaxPrice.place(x = 250, y = 300)

PriceLabel = tk.Label(window, text="prefered Price(USD)")
PriceLabel.place(x = 150, y = 280)

btn = tk.Button(window, text="Show Selection", command=check_selection)
btn.place(x=400, y=30)

label = tk.Label(window, text="Selected Flavor: ")
label.place(x=400, y=60)
tk.mainloop()
