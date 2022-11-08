import random
import time

class Player:
    def __init__(self, hp, damage, coins, healpotion, attackpotion, armor):
        self.hp = hp
        self.damage = damage
        self.coins = coins
        self.healpotion = healpotion 
        self.attackpotion = attackpotion
        self.armor = armor

player_1 = Player(100, 0, 40, 0, 1, 0)

class Monster:
    def __init__(self, name, hp, damage, agro):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.agro = agro


storMonster = Monster("Ugluck förgöraren", 50, random.randint(10,30), 50)
spindel = Monster ("Aragog",30, 75, 75)
diskmaskin = Monster("Emmy", 100, 10, 100)
BossMonster = Monster("Mr.Boss", 100, 100, 75)

def wait():
    time.sleep(0.4)
    print("-\n")
    time.sleep(0.4)
    print("-\n")
    time.sleep(0.4)
    print("-\n")
    time.sleep(0.4)
    print("-\n")
#göra så man kan få coins när man dödar monster tack:)
def fight (monster, player):
    while not monster.hp <= 0 :
        luckyhit = random.randint(1, 4)
        time.sleep(1.2)

        player_1.hp = monsterslag(monster, player) 
        time.sleep(1)
        fight = int(input('Tryck (1) för att attackera tillbaka eller tryck (2) för att springa iväg '))
        time.sleep(0.5)
        if fight == 2:
            print(f"Du springer iväg och gömer dig bakom ett träd tills {monster.name} har gått iväg")
            break
        elif fight == 1 and luckyhit == 3 :
            monster.hp = monster.hp - 2*player.damage
            print("Luckyhit du gjorde dubbla skada")
        elif fight == 1:
            monster.hp = monster.hp - player.damage
        time.sleep(0.8)

        if monster.hp<=0:
            print(f'Bra du dödade {monster.name}')
            player.coins += random.randint(10,20)
            print(f"{monster.name} droppade lite coins när du döda den\nDu har nu {player.coins} styckna coins")
        else:
            print (f'Bra du attackerar {monster.name}, dess nya hp är {monster.hp}') 
    
    shop(player_1)
    return player

def bossbattle(monster, player):
    print(f"Nu är det en boss fight mot {monster.name}, var försiktig hans yxa skadar mycket.")

    while not monster.hp   <= 0:
        luckyhit = random.randint(1, 4)
        time.sleep(1.5)
        
        time.sleep(1.5)
        player.hp = monsterslag(monster, player) 
        if player.hp <= 0:
            print(f"{monster.name} dödade dig")
            exit()

        fight = int(input("Tryck (1) för att slå mot hans ben\nTryck (2) för att slå mot hans överkropp\n"))
        if fight == 1 and luckyhit == 1:
            monster.hp = monster.hp - 2 * player.damage
            print("luckyhit du gjorde dubbla skadda")
        elif fight == 2 and luckyhit == 1:
            monster.hp = monster.hp - 3 * player.damage
            print("luckyhit du gjorde dubbla skadda")
        elif fight == 1:
            monster.hp = monster.hp - player.damage
        elif fight == 2:
            monster.hp = monster.hp - 1.5 * player.damage
        else:
            print(f"{monster.name} dödade dig")
            exit()

        if  monster.hp <= 0:
            player.coins += 50
            print(f"Grattis du dödade {monster.name}, han droppade 50 coins du har nu {player.coins}")
        else:
             print (f'Bra du attackerar {monster.name}, dess nya hp är {monster.hp}')
    shop(player_1)        
    return player.hp

def monsterslag(monster, player):
    totAgro = 100
    minHP = player.hp
    damage = 0
    agro = totAgro/random.randint(1,monster.agro)
    fight = agro < 5
    if fight:
        damage = random.randint(0, monster.damage)
    minHP = minHP - damage
    if minHP < player.hp:
        print(f"Monstret slog dig och du tappade {damage} HP")
    else:
        print("Monstret slår mot dig men missar dig precis och du tappar ingen HP")
        
    return minHP

def healpotion(player):
    print("Ditt HP ser ganska lågt ut, vilken tur att du har lite magisk hälso-dryck som ger + 50% av din hälsa")
    heal = int(input("Tryck (1) för att heala dig med den magiska drycken\nTryck (2) för att inte använda den\n"))
    if heal == 1 and player.healpotion >=1:
        player.hp = round(player.hp * 1.5)
        print(f"Du använde en healpotion ditt nya HP är {player.hp}")
    elif heal == 1 and player.healpotion < 1:
        print("Du har inga healpotions att använda")
    elif heal == 2:
        print("Hejdå")

def attackpotion(player):
    attackP = int(input("Tryck (1) för att använda attackpotion för att få permanent mer skada\nTryck (2) för att inte använda den\n"))
    if attackP == 1 and player.attackpotion >=1:
        player.damage = round(player.damage * 1.1)
        print(f"Du använde en attackpotion din nya skada är {player.damage} per slag")
    elif attackP == 1 and player.attackpotion < 1:
        print("Du har inga attackpotions att använda")
    elif attackP == 2:
        print("Hejdå")

def shop(player):
    shop_in = int(input("\nTryck (1) för att gå in i shoppen\nTryck (2) för att lämmna shoppen\n"))
    if shop_in == 1:
        print("Välkommen till Shoppen\nHär kan du köpa massa olika saker som kan hjälpa dig att döda fler monster")
        wait() 

        while True:
            print(f"Du har {player.coins} coins att spendera\n-")
            buy = int(input("Tryck (1) för att ta en närmare titt på Healpotions\n-\nTryck (2) för att ta en närmare titt på attackpotion\n-\nTryck (3) för att ta en närmare titt på armor\n-\nFör att använda heal eller attackpotion tryck (5)\n-\nFör att lämna shopen tryck (9)\n"))
            print("-\n-\n-\n")
            
            if buy == 1:
                print(f"Du har {player.healpotion} styckna healpotion\nEn healpotion kostar 10 coins du har {player.coins}\n")
                buy_heal = input("Om du vill köpa healpotion skriv Köp annars skriv Avbryt\n").lower()
                if buy_heal == "köp" and player.coins >=10:
                    player.healpotion += 1
                    player.coins -= 10
                    print("Du köpte en healpotion för 10 coins\n-\n")
                    print(f"Du har nu {player.healpotion} styckna healpotion")
                elif buy_heal == "avbryt":
                    pass
                else: 
                    print("Du har tyvär inte råd, din fattiga jävel")
            elif buy == 2:
                print(f"Du har {player.attackpotion} styckna attackpotion\nEn attackpotion kostar 15 coins du har {player.coins}\n")
                buy_attack = input("Om du vill köpa healpotion skriv Köp annars skriv Avbryt\n").lower()
                if buy_attack == "köp" and player.coins >15:
                    player.attackpotion += 1
                    player.coins -= 15
                    print("Du köpte en attackpotion för 15 coins\n-\n")
                    print(f"Du har nu {player.attackpotion} styckna attackpotion")
                elif buy_attack == "avbryt":
                    pass
                else: 
                    print("Du har tyvär inte råd, din fattiga jävel")
            elif buy == 3:
                buy_armor = input("Om du vill köpa armor skriv Köp annars skriv Avbryt\n").lower()
                if buy_armor == "köp" and player.coins >=40:
                    player.armor += 1
                    player.coins -= 40
                    print("Du köpte en armor för 40 coins\n-\n")
                    print(f"Du har nu {player.armor} styckna armor")
                elif buy_armor == "avbryt":
                    pass
                else: 
                    print("Du har tyvär inte råd, din fattiga jävel")
            elif buy == 5:
                healpotion(player_1)        #måste fixa den här lite så den ser bättre ut
                attackpotion(player_1)
            elif buy == 9:
                print("Du lämna shopet\n-\nVälkomen åter")    
                break
            wait()
    elif shop_in == 2:
        pass

def storyline():
    story = random.randint(1, 6)
    if story == 1:
        print("""Du var hungrig och försökte få lite honung från en bikupa,
men mislyckades och gjorde bina arga och de börja jaga dig.
För att undvika bina springer du till floden brevid,
men ser inte monstret som sitter och tvättar sig i vattnet.\n 
        """)
    elif story == 2:
        print("Du sprang villse i skogen när ett monster hoppade ner från ett träd\n")
    elif story == 3:
        print("Du har blivit omringad av tre monster\n")
    elif story == 4:
        print("Du ramlade ner i en grop med ett monster i för att ta dig upp måste du döda monstret\n")
    elif story == 5:
        print("Du råkade gå in på en stor monster fest och blev utmanad till en fajt till döden, för att inte bli uppäten\n")
    elif story == 6:
        print("""Det börjar att bli mörkt så du gör upp en eld för att se något
tyvärr vet monstrena exat vart du är nu, och är på väg för att äta upp dig.\n     
        """)
    elif story == 7:
        print("""Ute på ditt äventyr ser du en intresant grotta som ser rolig ut, 
du går in i grottan och råkar väcka monstret som låg och sov.\n
        """)

    time.sleep(1)

shop(player_1)

name = input('Vad heter du?: ')
time.sleep(0.5)
print(f"{name} ett väldigt passande namn för en monster jägare")
time.sleep(1.3)
print ('Här är en lista på det vapen du akn välja mellan')
time.sleep(1.)
print('Yxa(1)\nSvärd(2)\nNuke(3)\nFist(4)')
time.sleep(1.5)
vapen = int(input('Skriv den siffra för det vapen du vill ha: '))

if vapen == 1:
    player_1.damage =10
elif vapen == 2:
    player_1.damage = 8
elif vapen == 3:
    player_1.damage = 999
elif vapen == 4:
    player_1.damage = 1
else:
    exit()

bossbattle(BossMonster, player_1)

wait()

'''Monster_1'''
storyline()
fight(storMonster, player_1)

wait()

'''Monster_2'''
storyline()
fight(spindel, player_1)

wait()

storyline()
fight(diskmaskin,player_1)

wait()

print("Ånej vad är det stora läskiga monstret där framme. Det är en boss.")
bossbattle(BossMonster, player_1)

wait()
storyline()
fight(storMonster, player_1)

