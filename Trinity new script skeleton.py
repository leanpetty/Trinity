import time
import random

#M % defs
Mmagic=100
Mpop=random.randint(10000,20000)
Mminors=100
Mworkforce=100
Mwood=100
Mmetals=100
Mresources=100
Mtaxes=100
Mland=100
Mspaceused=100
Mhousing=100
Mmilitary power=100

#T % defs
Tfatigue=100
Tpop=random.randint(10000,20000)
Tminors=100
Tworkforce=100
Twood=100
Tmetals=100
Tresources=100
Ttaxes=100
Tland=100
Tspaceused=100
Thousing=100
Tmilitary=100

#W % defs
Wpop=random.randint(10000,20000)
Wminors=100
Wworkforce=100
Wwood=100
Wmetals=100
Wresources=100
Wtaxes=100
Wland=100
Wspaceused=100
Whousing=100
Wmilitary=100

#A % defs
Apop=random.randint(10000,20000)
Aminors=100
Aworkforce=100
Awood=100
Ametals=100
Aresources=100
Ataxes=100
Aland=100
Aspace=100
Ahousing=100
Amilitary=100

#M crisis affects
Mcrisis1=50
Mcrisis2=7.7

#T crisis affects

#W crisis affects

#A crisis affect

price1=random.randint(50,1000)
price2=random.randint(1000,2000)
price3=random.randint(2000,2500)
price4=random.randint(2500,4000)
price5=random.randint(4000,8000)
price6=random.randint(8000,10000)
price7=random.randint(10000,15000)
price8=random.randint(15000,25000)
price9=random.randint(25000,35000)
price10=random.randint(35000,40000)
price11=random.randint(40000,60000)
price12=random.randint(60000,100000)
price13=random.randint(100000,150000)
price14=random.randint(150000,200000)
price15=random.randint(40000,100000)
pricelenicara=random.randint(1,200000)

ww_steelsword = "Steel Sword"
ww_claws = "Claws" 
ww_bludgeon = "Bludgeon"
ww_scimitar = "Scimitar"
ww_hammer = "Hammer"

aw_sprucebow = "Spruce Bow"
aw_longbow = "Oak Longbow"
aw_dioritebow = "Refined Diorite Bow"
aw_ivy = "Ivy"
aw_breeze = "Breeze"

mw_birchstick = "Birch Stick"
mw_scarecrow = "Scarecrow's Staff"
mw_candlestick = "Candlestick"
mw_elderwand = "The Elder Wand"
mw_flameburst = "Flameburst" #casted spell

tw_brassknuckle = "Brass Knuckles"
tw_javelin = "Javelin"
tw_spear = "Warrior-Forged Spear"
tw_cyclops = "Cyclops' Javelin"
tw_scythe = "Scythe"

#rare weapons
ww_mallet = "Granite Mallet"
ww_mandibles = "Mandibles"
ww_gladius = "Golden Gladius"
ww_halberd = "Halberd"
ww_doubleaxe = "Double-Sided Axe"

aw_sharpshooter = "Sharpshooter's Arch"
aw_ivory = "Petrified Ivory Bow"
aw_thunderbolt = "Thunderbolt"
aw_trentbow = "Infused Trent Bow"
aw_prizedbow = "Trinity's Prized Bow"

mw_earthliving = "Earthliving Staff"
mw_ironstaff = "Iron Tipped Staff"
mw_cane = "Wood Cane"
mw_harp = "Petrified Harp"
mw_arcanebolt = "Arcane Bolt" #casted spell

tw_bullseye = "BULLSEYE!"
tw_diorite = "Impeccable Diorite Spear"
tw_blacksmith = "Blacksmith's Hammer"
tw_undying = "Undying Javelin"
tw_lion = "Coeur de Lion"

#epic weapons
ww_zweireaper = "Zweireaper"
ww_greatsword = "Elven Greatsword"
ww_gemcrusher = "Gemcrusher"
ww_katana = "Nethersteel Katana"
ww_lunar = "Lunar Relic"

aw_ignis = "Sharpshooter's Ignis"
aw_az = "Az"
aw_ironstring = "Iron String"
aw_flare = "Flare's Crest"
aw_cluster = "Clustershock"

mw_diablo = "El Diablo"
mw_voidtwig = "Void Twig"
mw_ancient = "Ancient Wand"
mw_waterbreath = "Water Breath" #casted spells
mw_liam = "Liam's Fart" #casted spell

tw_warriorspear = "Warrior Infused Javelin"
tw_tidebinder = "Tidebender's Spear"
tw_harwrol = "Harwrol"
tw_fierte = "Fiertè"
tw_frog = "Golden Frog Poison"

#legendary weapons
w_rubythorn = "Ruby Thorn"
w_drakefang = "Drake Fang Giantbone"
w_broccomace = "Rune Mace Broccomace"
w_frostbite = "Ice Shard Frostbite"
w_enderfist = "Archon Blade Enderfist"
w_divide = "The Divide"
w_gemini = "Gemini"
w_felflame = "Felflame"
w_armblade = "Armblade"
w_amaranth = "Amaranth"

#god weapons
gw_jahestirr = "Goaer's Recurve"
gw_ara = "All-Powerful Rune"
gw_esmyau = "Spellbreaker's Greatshield"
gw_umisr = "Ominous Warblade of the Unbreakable"
gw_trillini = "Hellreaver"
gw_lenicara = "Armageddon"
gw_goaer = "Triple Pronged Mechanical Sword"

#your weapons
yourweaponslist = []

def characterchoice():
    cchoiceloop=True
    while cchoiceloop == True:
        global charname
        charname=input("What is your name?")
        #in this case, 'char' means character, not charmaine
        time.sleep(1)
        print("Welcome to the game,", charname)
        chargenderinput=input("Are you a boy or a girl?")
        global chargender
        if chargenderinput.lower() == "boy" or chargenderinput.lower() == "male" or chargenderinput.lower() == "man":
            chargender="boy"
            print("You are a boy.")
            input("Press 'enter' to begin the game.")
            cchoiceloop=False
        elif chargenderinput.lower() == "girl" or chargenderinput.lower() == "female" or chargenderinput.lower() == "woman":
            chargender="girl"
            print("You are a girl.")
            input("Press 'enter' to begin the game.")
            cchoiceloop=False
        else:
            print("That was not one of the options. Start again.")

def introspeech():
    time.sleep(2)
    input("Welcome to the island of Trinity.")
    input("This small, unassuming island was actually home to the most amazing peoples imaginable.")
    time.sleep(2)
    input("These people never left this island. Why would they? It was all they needed?")
    print("")
    input("But one day, a ship turned up on the horison, carrying the Barbarians.")
    input("These Barbarians were war loving creatures, who believed they could subjugate all others to their will.")
    time.sleep(3)
    input("So they attacked the peoples, killing adults and children alike, and decimating their land for centuries to come.")
    input("""Just five groups managed to survive this massacre:
        the Trents, the Mages, the Archers, the Warriors and the Rogues.""")
    input("In the face of this danger, they joined arms and pushed back the invading Barbarians to the edge of the island.")
    input("Most of the groups realised that they did not have the strength to defeat the Barbarians, and stopped their attack there.")
    input("But the Rogues were not satisfied with this stalemate. They amassed an army, encompassing all the Rogues.")
    input("They attacked the Barbarians, hoping to destroy them in all out war.")
    time.sleep(4)
    input("Not a single Rogue survived.")
    print("")
    print("")
    time.sleep(2)
    input("After the battle, the four surviving groups made a pact to always be allies, and to help protect each other from the Barbarians.")
    input("As it turned out, the pact was worthless.")
    input("The clans turned against each other, through need and mistrust, keeping few as each others allies.")
    input("The Barbarians have made few raids on Trinity, but they continue to be an antagonistic presence.")
    time.sleep(3)
    input("And that brings our story up to now.")
    input("Born to an archer mother and a warrior father, you symbolise a change.")
    input("""As a product of one of the few marriages between warring clans, it is widely believed that you can be the ruler who brings your clan to victory,
either by yourself, or as all of Trinity united together. Like it or not, this is the responsibility you have been given.""")
    input("Because of this possibility, you were sent away from all four clans, to be taught the ways of leading by a man who speaks with the gods themselves.")
    input("After years of training, you return, finally ready to become a leader, and all the clans are clamouring to have you.")

def clanchoice():
    #for each choice, define a variable as being the clan choice to be used later in the program - Alex will do this
    print("Which of the clans do you want to lead?")
    time.sleep(4)
    ccinput=input("Warriors, Trents, Mages or Archers?")
    global clan
    global clanplural
    if ccinput.lower() == "warrior" or ccinput.lower() == "warriors":
        clan="warrior"
        clanplural="warriors"
        ccloop=False
        
    elif ccinput.lower() == "trent" or ccinput.lower() == "trents":
        clan="trent"
        clanplural="trents"
        ccloop=False
        
    elif ccinput.lower() == "mage" or ccinput.lower() == "mages":
        clan="mage"
        clanplural="mages"
        ccloop=False
        
    elif ccinput.lower() == "archer" or ccinput.lower() == "archers":
        clan="archer"
        clanplural="archers"
        ccloop=False

    else:
        input("That was not one of the available choices. Try again")

    if ccloop==False:
        print("Welcome to the", clanplural, ".")
    else:
        print("")

def initialsalesman():
    #salesman
    print("For the last 3 centuries, it has been customary to give a gift to society upon taking up the position of ruler.")
    time.sleep(2.5)
    input("Luckily, there is a wondering salesman on the road you are taking.")
    input("Having heard of you, he will give away one of his five weapons to you for free.")
    print("You will be at his booth shortly.")
    time.sleep(10)
    print("You have arrived.")
    time.sleep(0.5)
    print("")
    input("Salesman: Hello! Who are you? More importantly, would you like to buy something?")
    print("You: Good afternoon, sir. My name is", charname, ", the new head of the", clan, "clan.")
    input()
    time.sleep(1)
    print("Salesman: Really?")
    time.sleep(0.5)
    print("Salesman: I mean, hello", charname, "! I didn't recognise you! My most gracious apologies.")
    input()
    input("You: It's all right. I didn't have very good publicity in terms of my face.")
    input("Salesman: Oh, all right then. But tell you what, as compensation for not recognising you, take any of my 5 weapons.")
    input("You: Really?")
    input("""Salesman: Yes! Yes, really. This is a one time offer!
I'm afraid I dont have much of a selection though. All I can offer is Blade, Stick, Mallet, Bow
Very basic weaponary.""")
    #add 5 weapons specifically for this start-up sale - Ethan, then do the buying program - Liam
    input("You: Thank you so much!")
    input("You: I would stay, but I should really reach the town before sunset.")
    if chargender == "boy":
        input("Salesman: Of course! A young man like you must have lots to do.")
    else:
        input("Salesman: Of course! A young woman like you must have lots to do.")
    input("You say goodbye, and head on to the town.")
    

def joinclan():
    #joinclan
    input(print("Finally, you've made it to the town of the", clanplural, ". "))
    input("Despite your wish to begin work right away, all you get is a nice meal and a place to sleep.")
    input("But despite the jolly, carefree talk, all the officials seem worried.")
    input("Unfortunately, by the time you notice, you're too tired to care, and decide to let it wait until tomorrow.")

def intro():
    characterchoice()
    introspeech()
    print("")
    time.sleep(2)
    ccloop=True
    if ccloop==True:
        clanchoice()
        print("")
    time.sleep(2)
    initialsalesman()
    print("")
    time.sleep(2)
    joinclan()

def trentinitialproblem():
    #tip
    print("")

def mageinitialproblem():
    #mip
    input("In the morning you wake up.")
    input("Before you eat, you ask what the problem is that you noticed the night before.")
    input("Your servants tell you:")
    randmageinitialproblem=random.randint(7,9)
    if randmageinitialproblem == 0 or randmageinitialproblem == 1 or randmageinitialproblem == 2 or randmageinitialproblem == 3 or randmageinitialproblem == 4 or randmageinitialproblem == 5 or randmageinitialproblem == 6:
        input("'We forgot to sacrifice to Ara, the goddess of magic and love during a nobles wedding.'")
        input("'She has cursed us by removing some of the magical powers of the world. This began a week ago.'")
        input("'Thank goodness we aren't at war with anyone, or we would be destroyed.'")
        global Mmagic
        Mmagic=Mmagic-Mcrisis1
        print("")
        print("Each person's magical powers have gone down by", Mcrisis1, "%.")
        input()
    elif randmageinitialproblem == 7 or randmageinitialproblem == 8 or randmageinitialproblem == 9:
        input("'Lenicara, the god of luck, has decided that luck is no longer in our favour.'")
        input("'The last time this happened, thousands of years ago, half our population died.'")
        input("'This time, it's nowhere near as bad, but it's still terrible.'")
        input("'All of our seventh sons have fallen sick, and need urgent help or they will die.'")
        global Mpop
        OrigMpop=Mpop
        mip2=Mpop//Mcrisis2
        Mpop=Mpop-mip2
        round(Mpop)
        print("")
        print("Your population has gone down from", OrigMpop, "to", Mpop,)

def warriorinitialproblem():
    #wip
    print("")

def archerinitialproblem():
    #aip
    print("")

def trentlife():
    #trentlife
    print("")

def magelife():
    #magelife
    print("")

def warriorlife():
    #warriorlife
    print("")

def archerlife():
    #archerlife
    print("")

def trentgame():
    trentinitialproblem()

def magegame():
    mageinitialproblem()

def warriorgame():
    warriorinitialproblem()

def archergame():
    archerinitialproblem()

def clangame():
    #if/elif from clanchoice()

def trinity():
    intro()
    clangame()
