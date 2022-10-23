import json
with open('Matchups.txt') as f:
  champions = dict(champions.rstrip().split(None, 1) for champions in f)
print(champions)
def Matchups():
    champion = input("Qual champion pickaram? ")
    if champion.upper() not in champions:
        picked_counter = input("Que champion pickaste aqui? ")
        picked_counters = []
        picked_counters.append(picked_counter)
        champions.update({champion.upper():picked_counters})
        YesorNo= input("Queres adicionar mais um counter? ")
        while YesorNo.upper() == "SIM":
            picked_counter_update = input("Que champion pickaste aqui? ")
            picked_counters.append(picked_counter_update) 
            print(picked_counters)  
            champions.update({champion.upper():picked_counters})
            YesorNo= input("Queres adicionar mais um counter? ")
        else:
            print(f"Deves pickar {champions[champion.upper()]}")
    else:
        YesorNo= input("Queres mudar os counters? ")
        while YesorNo.upper() == "SIM":
            picked_counter_update = input("Que champion pickaste aqui? ")
            picked_counters=[]
            picked_counters.append(picked_counter_update) 
            print(picked_counters)  
            champions.update({champion.upper():picked_counters})
            YesorNo= input("Queres adicionar mais um counter? ")
        else:
            print(f"Deves pickar {champions[champion.upper()]}")
    with open("Matchups.txt", "w") as convert_file:
        convert_file.write(json.dumps(champions))

