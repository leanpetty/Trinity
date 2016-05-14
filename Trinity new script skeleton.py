import time
import random

#M % defs
Mmagic=100
Mpop=random.randint(10000,20000)
Mminors=round(0.1*Mpop)
Mworkforce=Mpop-Mminors
Mwood=100
Mmetals=100
Mfood=100
Mresources=100
Mtaxes=100
Mland=100
Mspaceused=100
Mhousing=100
Mmilitarypower=100

#T % defs
Tfatigue=100
Tpop=random.randint(10000,20000)
Tminors=round(0.1*Tpop)
Tworkforce=Tpop-Tminors
Twood=100
Tmetals=100
Tfood=100
Tresources=100
Ttaxes=100
Tland=100
Tspaceused=100
Thousing=100
Tmilitary=100

#W % defs
Wpop=random.randint(10000,20000)
Wminors=round(0.1*Wpop)
Wworkforce=Wpop-Wminors
Wwood=100
Wmetals=100
Wfood=100
Wresources=100
Wtaxes=100
Wland=100
Wspaceused=100
Whousing=100
Wmilitary=100

#A % defs
Apop=random.randint(10000,20000)
Aminors=round(0.1*Apop)
Aworkforce=Apop-Aminors
Awood=100
Ametals=100
Afood=100
Aresources=100
Ataxes=100
Aland=100
Aspace=100
Ahousing=100
Amilitary=100

#M crisis affects
Mcrisis1=random.randint(45,55)
Mcrisis2=7.7

#T crisis affects
Tcrisis1=random.randint(20,30)
Tcrisis2=random.randint(20,45)

#W crisis affects
Wcrisis1=random.randint(10,25)
Wcrisis2=random.randint(20,45)

#A crisis affect
Acrisis1=random.randint(19,22)

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
w_jahestirr = "Goaer's Recurve"
w_ara = "All-Powerful Rune"
w_esmyau = "Spellbreaker's Greatshield"
w_umisr = "Ominous Warblade of the Unbreakable"
w_trillini = "Hellreaver"
w_lenicara = "Armageddon"
w_goaer = "Triple Pronged Mechanical Sword"

w_commonweapons = [ww_steelsword, ww_claws, ww_bludgeon, ww_scimitar, ww_hammer]
a_commonweapons = [aw_sprucebow, aw_longbow, aw_dioritebow, aw_ivy, aw_breeze]
m_commonweapons = [mw_birchstick, mw_scarecrow, mw_candlestick, mw_elderwand, mw_flameburst]
t_commonweapons = [tw_brassknuckle, tw_javelin, tw_spear, tw_cyclops, tw_scythe]

w_rareweapons = [ww_mallet, ww_mandibles, ww_gladius, ww_halberd, ww_doubleaxe]
a_rareweapons = [aw_sharpshooter, aw_ivory, aw_thunderbolt, aw_trentbow, aw_prizedbow]
m_rareweapons = [mw_earthliving, mw_ironstaff, mw_cane, mw_harp, mw_arcanebolt]
t_rareweapons = [tw_bullseye, tw_diorite, tw_blacksmith, tw_undying, tw_lion]

w_epicweapons = [ww_zweireaper, ww_greatsword, ww_gemcrusher, ww_katana, ww_lunar]
a_epicweapons = [aw_ignis, aw_az, aw_ironstring, aw_flare, aw_cluster]
m_epicweapons = [mw_diablo, mw_voidtwig, mw_ancient, mw_waterbreath, mw_liam]
t_epicweapons = [tw_warriorspear, tw_tidebinder, tw_harwrol, tw_fierte, tw_frog]

legendaryweapons = [w_rubythorn, w_drakefang, w_broccomace, w_frostbite, w_enderfist, w_divide, w_gemini, w_felflame, w_armblade, w_amaranth]

godweapons = [w_jahestirr, w_ara, w_esmyau, w_umisr, w_trillini, w_lenicara, w_goaer]

#your weapons
yourweaponslist = []
    
#other lists
traderexclamationsjoyful = ["Terrific!", "Fantastic", "Splendid!", "Perfect!", "Wonderful!", "Amazing!", "Marvellous!", "Magnificent!", "Superb!", "Splendid!", "Super!", "Great!", "Smashing!", "Phenomenal!", "Sensational!", "Fabulous!", "Fantabulous!"]

def characterchoice():
    cchoiceloop=True
    while cchoiceloop == True:
        global charname
        cnameloop=True
        while cnameloop==True:
            charname=input("What is your name?")
            print("")
            if charname == "":
                print("You have not typed anything, try again.")
                print("")
            else:
                cnameloop=False
            #in this case, 'char' means character, not charmaine
            print("Welcome to the game,", charname)
            print("")
            print("")
        chargenderinput=input("Are you a boy or a girl?")
        print("")
        global chargender
        if chargenderinput.lower() == "boy" or chargenderinput.lower() == "male" or chargenderinput.lower() == "man":
            chargender="boy"
            print("You are a boy.")
            print("")
            input("Press 'enter' to begin the game.")
            cchoiceloop=False
        elif chargenderinput.lower() == "girl" or chargenderinput.lower() == "female" or chargenderinput.lower() == "woman":
            chargender="girl"
            print("You are a girl.")
            print("")
            input("Press 'enter' to begin the game.")
            cchoiceloop=False
        elif chargenderinput.lower() == "i don't know" or chargenderinput.lower() == "i dont know" or chargenderinput.lower() == "idk":
            print("Then we'll decide for you.")
            print("")
            cnameidk=random.randint(0,1)
            if cnameidk == 0:
                chargender="girl"
                print("You are a girl")
                print("")
                input("Press 'enter' to begin the game.")
                cchoiceloop=False
            elif cnameidk == 1:
                chargender="boy"
                print("You are a boy")
                print("")
                input("Press 'enter' to begin the game.")
                cchoiceloop=False
            
        else:
            print("That was not one of the options. Start again.")
            print("")

def introspeech():
    print("")
    print("Welcome to the island of Trinity.")
    input()
    print("This small, unassuming island was actually home to the most amazing people imaginable.")
    input()
    print("These people never left this island. Why would they? It was all they needed.")
    input()
    print("")
    print("But one day, a ship appeared on the horizon, carrying the Barbarians.")
    input()
    print("These Barbarians were war loving creatures, who believed they could subjugate all others to their will.")
    input()
    print("So they attacked the Trinites, killing adults and children alike, and decimating their land for centuries to come.")
    input()
    print("""Just five groups managed to survive this massacre:
the Trents, the Mages, the Archers, the Warriors and the Rogues.""")
    input()
    print("In the face of this danger, they joined arms and pushed back the invading Barbarians to the edge of the island.")
    input()
    print("Most of the groups realised that they did not have the strength to defeat the Barbarians, and stopped their attack there.")
    input()
    print("But the Rogues were not satisfied with this stalemate.")
    input()
    print("They amassed an army and attacked the Barbarians, hoping to destroy them in all out war.")
    input()
    print("Not a single Rogue survived.")
    input()
    print("")
    print("")
    print("After the battle, the four surviving groups made a pact to always be allies, and to help protect each other from the Barbarians.")
    input()
    print("As it turned out, the pact was worthless.")
    input()
    print("The clans turned against each other, through need and mistrust. There were few remaining alliances.")
    input()
    print("The Barbarians have made few raids on Trinity, but they continue to be an menacing presence.")
    input()
    print("And that brings our story up to now.")
    input()
    print("Born to an archer mother and a warrior father, you symbolise a change.")
    input()
    print(""" As a product of one of the few marriages between warring clans, it is widely believed that you can be the ruler who destroys the barbarians, either by defeating them using the resources of your clan, or by uniting all of Trinity to fight back. Like it or not, this is the responsibility you have been given.""")
    input()
    print("Because of this possibility, you were sent away from all four clans, to be taught the ways of leading by a man who speaks with the gods themselves.")
    input()
    print("After years of training, you return, finally ready to become a leader, and all the clans are desperate to have you.")
    input()

def clanchoice():
    #for each choice, define a variable as being the clan choice to be used later in the program - Alex will do this
    print("Which of the clans do you want to lead?")
    print("")
    time.sleep(4)
    global clan
    global clanplural
    ccloop = True
    while ccloop==True:
        ccinput=input("Warriors, Trents, Mages or Archers?")
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
            print("")
            input("That was not one of the available choices. Try again")
    

    print("")
    print("Welcome to the", clanplural, ".")

def initialsalesman():
    #salesman
    print("For the last 3 centuries, it has been customary to give a gift to society upon taking up the position of ruler.")
    input()
    print("Luckily, there is a wondering salesman on the road you are taking.")
    input()
    print("Having heard of you, he will give away one of his four weapons to you for free.")
    input()
    print("You will be at his booth shortly.")
    input()
    print("You have arrived.")
    input()
    print("")
    print("Salesman: Hello! Who are you? More importantly, would you like to buy something?")
    input()
    print("You: Good afternoon, sir. My name is", charname, ", the new head of the", clan, "clan.")
    input()
    print("")
    print("Salesman: Really?")
    input()
    print("Salesman: I mean, hello", charname, "! I didn't recognise you! My most gracious apologies.")
    input()
    print("You: It's all right. Many people haven't seen me yet.")
    input()
    print("Salesman: Oh, all right then. But tell you what, as compensation for not recognising you, take any of my 4 weapons.")
    input()
    print("You: Are you joking?")
    input()
    print("""Salesman: No! I mean it. This is a one time offer!
I'm afraid I dont have much of a selection at the moment though. All I can offer is a simple Blade, a Stick, a Mallet or an old Bow.
Very basic weaponary.""")
    input()

    weaponchoiceloop=True
    while weaponchoiceloop==True:
        firstweapon=input("Which weapon would you like to take?")
        if  firstweapon.lower()=="blade" or firstweapon.lower()=="stick" or firstweapon.lower()=="mallet" or firstweapon.lower()=="bow":
            weaponchoiceloop=False
        else:
            print("That is not an option. Please choose again.")

    print("")
    print("The", firstweapon.lower(), "has been added to your weapons.")
    input()

    print("You: Thank you so much!")
    input()
    print("You: I would stay, but I should really reach the town before sunset.")
    input()

    if chargender == "boy":
        print("Salesman: Of course! A young man like you must have lots to do.")
        input()
    else:
        print("Salesman: Of course! A young lady like you must have lots to do.")
        input()
        print("")
    print("You say goodbye, and head on to the town.")
    input()
    

def joinclan():
    #joinclan
    print("Finally, you've made it to the town of the", clanplural, ". ")
    input()
    print("Though you wish to begin work right away, the town's people are insistent that you eat and rest.")
    input()
    print("On the way to your rooms, you banter with the officials who guide you.")
    input()
    print("But despite the jolly, carefree talk, all the officials seem worried.")
    input()
    print("Unfortunately, by the time you notice, you're too tired to care, and decide to let it wait until tomorrow.")
    input()
    print("")

def intro():
    characterchoice()
    introspeech()
    print("")
    ccloop=True
    if ccloop==True:
        clanchoice()
        print("")
    initialsalesman()
    print("")
    joinclan()

def trentinitialproblem():
    #tip
    print("")

def mageinitialproblem():
    #mip
    print("In the morning you wake up.")
    input()
    print("Before you eat, you ask what the problem is that you noticed the night before.")
    input()
    print("Your servants tell you:")
    input()
    randmageinitialproblem=random.randint(7,9)
    if randmageinitialproblem == 0 or randmageinitialproblem == 1 or randmageinitialproblem == 2 or randmageinitialproblem == 3 or randmageinitialproblem == 4 or randmageinitialproblem == 5 or randmageinitialproblem == 6:
        print("We forgot to sacrifice to Ara, the goddess of magic and love during a nobles wedding.")
        input()
        print("She has cursed us by removing some of the magical powers of the world. This began a week ago.")
        input()
        print("Thank goodness we aren't at war with anyone, or we would be destroyed.")
        input()
        global Mmagic
        Mmagic=Mmagic-Mcrisis1
        print("")
        print("Each person's magical powers have gone down by", Mcrisis1, "%.")
        input()
    elif randmageinitialproblem == 7 or randmageinitialproblem == 8 or randmageinitialproblem == 9:
        print("Lenicara, the god of luck, has decided that luck is no longer in our favour.")
        input()
        print("The last time this happened, thousands of years ago, half our population died.")
        input()
        print("This time, it's nowhere near as bad, but it's still terrible.")
        input()
        print("All of our seventh sons have fallen sick, and need lots of attention or they will die.")
        input()
        global Mworkforce
        OrigMworkforce=Mworkforce
        mip2=Mworkforce//Mcrisis2
        Mworkforce=Mworkforce-mip2
        round(Mworkforce)
        print("")
        print("Your workforce has gone down from", OrigMworkforce, "to", Mworkforce,)
        input()

def warriorinitialproblem():
    #wip
    print("In the morning you wake up.")
    input()
    print("Before you eat, you ask what the problem is that you noticed the night before.")
    input()
    print("Your servants tell you:")
    input()
    randwarriorinitialproblem=random.randint(0,9)
    if randwarriorinitialproblem == 0 or randwarriorinitialproblem == 1 or randwarriorinitialproblem == 2 or randwarriorinitialproblem == 3 or randwarriorinitialproblem == 4 or randwarriorinitialproblem == 5:
        print("The Trents have gone to war with the Archers.")
        input()
        print("The Trents are our only wood supplier and can't supply new wood to us.")
        input()
        print("Thank goodness we aren't at war with anyone, or we would be destroyed.")
        input()
        global Wwood
        Wwood=Wwood-Wcrisis1
        print("")
        print("The clan's wood supply has decreased by", Wcrisis1, "%. You now have", Wwood, "pieces of wood.")
        input()
    elif randwarriorinitialproblem == 6 or randwarriorinitialproblem == 7 or randwarriorinitialproblem == 8 or randwarriorinitialproblem == 9:
        print("The Trents have gone to war with the Archers and as their allies we are obliged to provide them with troops.")
        input()
        global Wmilitary
        OrigWmil=Wmilitary
        Wmilitary=Wmilitary-Wcrisis1
        print("")
        print("Your military size has gone down from", OrigWmil, "to", round (Wmilitary))
        input()

def archerinitialproblem():
    #aip
    print("In the morning you wake up")
    input()
    print("Before you eat, you ask what the problem is you noticed the night before")
    input()
    print("Your servants tell you:")
    input()
    randarcherinitialproblem=random.randint(0,9)
    if randarcherinitialproblem == 0 or randarcherinitialproblem == 1 or randarcherinitialproblem == 2 or randarcherinitialproblem == 3:
        print("'We have gone to war with the Trents.'")
        input()
        print("'However the Trents are outnumbering us and we are losing ground quickly.'")
        input()
        print("'If this keeps up, we will end up losing lots of our territory to the trents.'")
        input()
        global Aland
        Aland=Aland-Acrisis1
        print(" ")
        print("The clan's territory has decreasded by", Acrisis1, "%. You now have", Aland, "acres of land.")
        input()
    elif randarcherinitialproblem == 4 or randarcherinitialproblem == 5 or randarcherinitialproblem == 6 or randarcherinitialproblem == 7 or randarcherinitialproblem == 8 or randarcherinitialproblem == 9:
        print("'The monsoon season has started once again and our rivers have been flooded with muddy water, severely decreasing the fish population.'")
        input()
        print("'The last time this happened nearly half of our population died from starvation.'")
        input()
        print("'We will soon need to make trades with other clans for food if the entire clan were to survive.'")
        input()
        global Afood
        OrigAfood=Afood
        Afood=Afood-Acrisis1
        print(" ")
        print("Your clan's food levels have gone down from", OrigAfood, "to", round(Afood))
    
    #the program for the salesman who visits in everyday life - can be edited for your own needs later, this one is specifically for Mages
    def freetraderM():
        print("Hello my dear friend!")
        input()
        print("What do you want to buy today?")
        input()
        #Note: The spaces here are so that on my computer with my settings, these are centered. I'll work on a way to have that done better for the future
        print("""Options:
                                                                Food                                                       Weapons
    
                                                                                             Materials""")
        freetradein=input("")
        freetradein = freetradein.lower()
        if freetradein == "food":
            print(random.choice(traderexclamationsjoyful),"You will find that my selection of cusine is far above that of anyone else on this island.")
            input()
            print("I'll have them shipped directly to the doorsteps of your citizens - for a fair price, of course.")
            input()
        elif freetradein == "weapons":
            print(random.choice(traderexclamationsjoyful),"I guarantee that utterly destroying your enemies with these weapons will be much more fun than with any others.")
            input()
            print("And don't worry, all the correct sacrifices have been made. Your weapons won't turn on you in battle.")
            input()
        elif freetradein == "materials":
            print(random.choice(traderexclamationsjoyful), "I have a rather wide range of materials here for you to buy from me.")
            input()
            print("They might not be as cheap as those from your other friends, but I come round many times more often!")
            input()
            print("Its only fair you buy from me instead.")
            input()

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
    trentlife()

def magegame():
    mageinitialproblem()
    magelife()

def warriorgame():
    warriorinitialproblem()
    warriorlife()

def archergame():
    archerinitialproblem()
    archerlife()

def clangame():
    if clan=="mage":
        magegame()
    elif clan=="warrior":
        warriorgame()
    elif clan=="archer":
        archergame()
    elif clan=="trent":
        trentgame()

def trinity():
    intro()
    clangame()

trinity()

