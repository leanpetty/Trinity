import time
import random

global krikor

global Mresources
global Mhappy
global Mpop
global Mmilitary
global Mmagic

global Tresources
global Thappy
global Tpop
global Tmilitary

global Wresources
global Whappy
global Wpop
global Wmilitary

global Aresources
global Ahappy
global Apop
global Amilitary

krikor=40000
Jsacriprice=85
Asacriprice=60
Esacriprice=70
Usacriprice=35
Tsacriprice=55
Lsacriprice=65
Gsacriprice=100

global pricefood
global woodprice 
global coalprice
global ironprice
global stoneprice
global epicweaponluck

pricefood=random.randint(20,30)
woodprice=random.randint(250,500)
coalprice=random.randint(500,750)
ironprice=random.randint(500,1000)
stoneprice=random.randint(100,500)
epicweaponluck=random.randint(1,50)

#M % defs
Mmagic=100
Mpop=random.randint(10000,20000)
Mminors=round(0.1*Mpop)
Mhappy=100
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
Thappy=100
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
Whappy=100
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
Ahappy=100
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

#common weapons
ww_steelsword = "Steel Sword"
ww_claws = "Claws" 
ww_bludgeon = "Bludgeon"
ww_scimitar = "Scimitar"
ww_hammer = "Hammer"
ww_sabre = "Sabre"
ww_ida = "Ida Sword"
ww_bolo = "Bolo Sword"
ww_hook = "Hook"
ww_mallet = "Granite Mallet"
ww_strongwood = "Strongwood Club"
ww_longknife = "Long Knife"
ww_dagger = "Dagger"
ww_katana = "Katana Sword"
ww_bonesword = "Bone Sword"

aw_sprucebow = "Spruce Bow"
aw_longbow = "Oak Longbow"
aw_dioritebow = "Refined Diorite Bow"
aw_ivy = "Ivy"
aw_breeze = "Breeze"
aw_sharpshooter = "Sharpshooter's Arch"
aw_crossbow = "Crossbow"
aw_pocketbow = "Pocket Bow"
aw_recurve = "Recurve Bow"
aw_hellburner = "Hellburner"
aw_skullbreaker = "Skullbreaker"
aw_tridentarrow = "Trident Arrow"
aw_meet = "Meeter"
aw_knife = "Knife"
aw_barrager = "Barrager"

mw_birchstick = "Birch Stick"
mw_scarecrow = "Scarecrow's Staff"
mw_candlestick = "Candlestick"
mw_grotti = "Grotti"
mw_flameburst = "Flameburst" #casted spell
mw_thunderlord = "Thunderlord"
mw_mercy = "Merciful Killer"
mw_icestorm = "Icestorm" #casted spell
mw_enchantsword = "Enchanted Sword"
mw_void = "Void Staff"
mw_silverlance = "Silver Lance"
mw_runicbook = "Book of Runes"
mw_skystaff = "Staff of the Sky"
mw_strength = "Strength" #casted spell
mw_tearbringer = "Tear Bringer"

tw_brassknuckle = "Brass Knuckles"
tw_javelin = "Javelin"
tw_spear = "Warrior-Forged Spear"
tw_cyclops = "Cyclops' Javelin"
tw_scythe = "Scythe"
tw_lance = "Metal Lance"
tw_bluepike = "Blue Pike"
tw_tribute = "Tribute to Fallen Foes"
tw_trident = "Antique Trident"
tw_bloodspear = "Blood-Spear"
tw_harpoon = "Harpoon"
tw_forkspear = "Forked Spear"
tw_heavymace = "Heavy Mace"
tw_deathseeker = "Deathseeker"
tw_staff = "Staff"

#rare weapons
ww_butterfly = "Butterfly Sword"
ww_mandibles = "Mandibles"
ww_gladius = "Golden Gladius"
ww_halberd = "Halberd"
ww_doubleaxe = "Double-Sided Axe"

aw_threebow = "Three Arrow Bow"
aw_ivory = "Petrified Ivory Bow"
aw_thunderbolt = "Thunderbolt"
aw_trentbow = "Infused Trent Bow"
aw_prizedbow = "Trinity's Prized Bow"

mw_earthliving = "Earthliving Staff"
mw_ironstaff = "Iron Tipped Staff"
mw_cane = "Wood Cane"
mw_harp = "Petrified Harp"
mw_arcanebolt = "Arcane Bolt" #casted spell

tw_bullseye = "Bullseye!"
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
w_jahestirr = "Goaer's Gift"
w_ara = "All-Powerful Rune"
w_esmyau = "Spellbreaker's Greatshield"
w_umisr = "Ominous Warblade of the Unbreakable"
w_trillini = "Hellreaver"
w_lenicara = "Armageddon"
w_goaer = "Triple Pronged Mechanical Sword"

w_commonweapons = [ww_steelsword, ww_claws, ww_bludgeon, ww_scimitar, ww_hammer, ww_sabre, ww_ida, ww_bolo, ww_hook, ww_mallet, ww_strongwood, ww_longknife, ww_dagger, ww_katana, ww_bonesword]
a_commonweapons = [aw_sprucebow, aw_longbow, aw_dioritebow, aw_ivy, aw_breeze, aw_sharpshooter, aw_crossbow, aw_pocketbow, aw_recurve, aw_hellburner, aw_skullbreaker, aw_tridentarrow, aw_meet, aw_knife, aw_barrager]
m_commonweapons = [mw_birchstick, mw_scarecrow, mw_candlestick, mw_grotti, mw_flameburst, mw_thunderlord, mw_mercy, mw_icestorm, mw_enchantsword, mw_void, mw_silverlance, mw_runicbook, mw_skystaff, mw_strength, mw_tearbringer]
t_commonweapons = [tw_brassknuckle, tw_javelin, tw_spear, tw_cyclops, tw_scythe, tw_lance, tw_bluepike, tw_tribute, tw_trident, tw_bloodspear, tw_harpoon, tw_forkspear, tw_heavymace, tw_deathseeker, tw_staff]

w_rareweapons = [ww_butterfly, ww_mandibles, ww_gladius, ww_halberd, ww_doubleaxe]
a_rareweapons = [aw_ivory, aw_threebow, aw_trentbow, aw_prizedbow]
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

def presets():
    print("To change the presets, you must first complete the game.")
    presetcode=input("If you have completed the game, enter your 10-digit code here.")
    if presetcode==1123581321:
        print("You can now change the presets.")
        #change this when game is complete
        print("Unfortunately, the game hasn't been completed yet, so we know that if you are here, Its because you cheated.")
        print("But you can have a second chance.")
        input()
        print("And a sneak peak of what will be here.")
        print("Once you complete the game, you can change the presets, giving you a massive amount of people, popularity or others.")
        input()
        print("Or you could give yourself really low points, making the game more difficult.")
        print("But as the game isnt finished, this feature isnt yet ready. When the game is complete, this will be too.")
        input()
        print("But now...")
        input("Press enter to begin the game.")
    else:
        input("Incorrect. Press enter to begin the game normally.")


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
        else:
            print("That was not an option, start again.")
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
    clanchoice()
    print("")
    initialsalesman()
    print("")
    joinclan()


def trentinitialproblem():
    global Tpop
    #tip
    print("In the morning you wake up.")
    input()
    print("Before you eat, you ask what the problem is that you noticed the night before.")
    input()
    print("Your servants tell you:")
    input()
    Tcrisis=random.randint(1,2)
    if Tcrisis==1:
        print("'Yesterday, we recieved word that a raging forest fire has burned", Tcrisis1, "Trents to death'")
        Tpop=Tpop-Tcrisis1
        print("You now have a population of", Tpop, ".")
    elif Tcrisis==2:
        print ("'Yesterday, we recieved word that a rabid swarm of insects near our southern border have killed", Tcrisis2, "Trents'")
        Tpop=Tpop-Tcrisis2
        print("You now have a population of", Tpop, ".")
        
    print("You are a little rattled by the terrible things that just happened, but you settle down into your first week of the job.")


def mageinitialproblem():
    global Mmagic
    global Mworkforce
    #mip
    print("In the morning you wake up.")
    input()
    print("Before you eat, you ask what the problem is that you noticed the night before.")
    input()
    print("Your servants tell you:")
    input()
    randmageinitialproblem=random.randint(0,9)
    if randmageinitialproblem == 0 or randmageinitialproblem == 1 or randmageinitialproblem == 2 or randmageinitialproblem == 3 or randmageinitialproblem == 4 or randmageinitialproblem == 5 or randmageinitialproblem == 6:
        print("We forgot to sacrifice to Ara, the goddess of magic and love during a nobles wedding.")
        input()
        print("She has cursed us by removing some of the magical powers of the world. This began a week ago.")
        input()
        print("Thank goodness we aren't at war with anyone, or we would be destroyed.")
        input()
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
        OrigMworkforce=Mworkforce
        mip2=Mworkforce//Mcrisis2
        Mworkforce=Mworkforce-mip2
        round(Mworkforce)
        print("")
        print("Your workforce has gone down from", OrigMworkforce, "to", Mworkforce,)
        input()
        
    print("You are a little rattled by the terrible things that just happened, but you settle down into your first week of the job.")


def warriorinitialproblem():
    global Wwood
    global Wmilitary
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
        Wwood=Wwood-Wcrisis1
        print("")
        print("The clan's wood supply has decreased by", Wcrisis1, "%. You now have", Wwood, "pieces of wood.")
        input()
    elif randwarriorinitialproblem == 6 or randwarriorinitialproblem == 7 or randwarriorinitialproblem == 8 or randwarriorinitialproblem == 9:
        print("The Trents have gone to war with the Archers and as their allies we are obliged to provide them with troops.")
        input()
        OrigWmilitary=Wmilitary
        Wmilitary=Wmilitary-Wcrisis1
        Wmilitary=round(Wmilitary)
        print("")
        print("Your military size has gone down from", OrigWmilitary, "to", Wmilitary)
        input()
        
    print("You are a little rattled by the terrible things that just happened, but you settle down into your first week of the job.")


def archerinitialproblem():
    #aip
    global Aland
    global Afood
    print("In the morning you wake up.")
    input()
    print("Before you eat, you ask what the problem is that you noticed the night before.")
    input()
    print("Your servants tell you:")
    input()
    randarcherinitialproblem=random.randint(0,9)
    if randarcherinitialproblem == 0 or randarcherinitialproblem == 1 or randarcherinitialproblem == 2 or randarcherinitialproblem == 3:
        print("'We have gone to war with the Trents.'")
        input()
        print("'However the Trents are outnumbering us and we are losing ground quickly.'")
        input()
        print("'If this keeps up, we will end up losing lots of our territory to the Trents.'")
        input()
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
        OrigAfood=Afood
        Afood=Afood-Acrisis1
        print(" ")
        print("Your clan's food levels have gone down from", OrigAfood, "to", round(Afood))

    print("You are a little rattled by the terrible things that just happened, but you settle down into your first week of the job.")


def freetraderT():
    print("")
    pricefood=random.randint(20,30)
    woodprice=random.randint(250,500)
    coalprice=random.randint(500,750)
    ironprice=random.randint(500,1000)
    stoneprice=random.randint(100,500)
    epicweaponluck=random.randint(1,50)
    print("Hello my dear friend!")
    input()
    input("Today I have the following:")
    input("Food")
    input("Weapons")
    input("Materials")
    input("")
    freetradein=input("What would you like to buy? If you don't wish to purchase anything type none.")
    freetradein = freetradein.lower()
    if freetradein == "food":
        print(random.choice(traderexclamationsjoyful),"You will find that my selection of cusine is far above that of anyone else on this island.")
        input()
        print("I'll have them shipped directly to the doorsteps of your citizens - for a fair price, of course.")
        input()
        foodtradeloop = True
        while foodtradeloop == True:
            group_of_food = {"Steak", "Cooked Porkchop", "Jacket Potato", "Cooked Fish", "Bread", "Cooked Chicken"}
            num_to_select = 3
            list_of_random_food = random.sample(group_of_food, num_to_select)
            first_random_food = list_of_random_food[0]
            second_random_food = list_of_random_food[1]
            third_random_food = list_of_random_food[2]
            print("Today's selection is", first_random_food,",",second_random_food, "as well as", third_random_food,".")
            input()
            typedfood=str(input("What would you like to purchase? Please note that I am case sensitive."))
            if typedfood in {first_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {second_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {third_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            else:
                print("")
                input("I'm sorry. Unfortunately that is not a valid option. Please try again.")

    elif freetradein == "weapons":
        print(random.choice(traderexclamationsjoyful),"I guarantee that utterly destroying your enemies with these weapons will be much more fun than with any others.")
        input()
        print("And don't worry, all the correct sacrifices have been made. Your weapons won't turn on you in battle.")
        input()
        weapontradeloop = True
        while weapontradeloop == True:

            group_of_common_tweapons = {brassknuckle, javelin, spear, cyclops, scythe, lance, bluepike, tribute, trident, bloodspear, harpoon, tw_forkspear, heavymace, deathseeker, staff}
            num_to_select = 6
            list_of_random_common_tweapons = random.sample(group_of_common_tweapons, num_to_select)
            first_random_common_tweapon = list_of_random_common_tweapons[0]
            second_random_common_tweapon = list_of_random_common_tweapons[1]
            third_random_common_tweapon = list_of_random_common_tweapons[2]
            fourth_random_common_tweapon = list_of_random_common_tweapons[3]
            fifth_random_common_tweapon = list_of_random_common_tweapons[4]
            sixth_random_common_tweapon = list_of_random_common_tweapons[5]

            group_of_rare_tweapons = {"Bullseye", "Diorite", "Blacksmith", "Undying", "Lion"}
            num_to_select = 2
            list_of_random_rare_tweapons = random.sample(group_of_rare_tweapons, num_to_select)
            first_random_rare_wweapon = list_of_random_rare_tweapons[0]
            second_random_rare_wweapon = list_of_random_rare_tweapons[1]

            print("Lucky for you, I have quite the selection right now. For common weapons, I can offer a", first_random_common_tweapon,", a", second_random_common_tweapon,", a", third_random_common_tweapon,", a", fourth_random_common_tweapon,", a", fifth_random_common_tweapon," and a", sixth_random_common_tweapon,".")
            input()
            print("As for rare weapons, a", first_random_rare_tweapon," and a", second_random_rare_tweapon,".")
            input()
            weapontradeloop = False
            
            group_of_epic_tweapons ={"Warrior Infused Javevlin", "Tidebender's Spear", "Harwol", "Fierte", "Golden Frog Poison"}
            num_to_select = 1
            list_of_random_epic_tweapons = random.sample(group_of_epic_tweapons, num_to_select)
            random_epic_aweapon = list_of_random_epic_tweapons[0]
            if epicweaponluck == 7:
                print("Oh my. What is this...looks like you're in luck today! It seems as if I have an epic weapon in stock - the", random_epic_tweapon,"!")
            else:
                print("")

            typedweapon=str(input("Which weapon would you like to purchase? Please note that I am case sensitive."))
            if typedweapon in {first_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {second_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {third_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {fourth_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {fifth_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {sixth_random_common_tweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {first_random_rare_tweapon}:
                print("Excellent. That will be", price2,"krikor.")
                weapontradeloop = False
                krikor=krikor-price2
                print("You now have", krikor, "krikor.")
            elif typedweapon in {second_random_rare_tweapon}:
                print("Excellent. That will be", price2,"krikor.")
                weapontradeloop = False
                krikor=krikor-price2
                print("You now have", krikor, "krikor.")
            elif typedweapon in {random_epic_weapon}:
                print("Excellent. That will be", price3,"krikor.")
                weapontradeloop = False
                krikor=krikor-price3
                print("You now have", krikor, "krikor.")
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")

    elif freetradein == "materials":
        print(random.choice(traderexclamationsjoyful), "I have a rather wide range of materials here for you to buy from me.")
        input()
        print("They might not be as cheap as those from your other friends, but I come round many times more often!")
        input()
        print("Its only fair you buy from me instead.")
        input()
        print("I have a selection of Wood, Coal, Iron and Stone.")
        input()
        materialtradeloop = True
        while materialtradeloop == True:
            typedmaterial=str(input("What would you like to purchase?"))
            if typedmaterial == "Wood" or typedmaterial == "wood":
                print("Excellent. That will", woodprice,"be krikor.")
                materialtradeloop = False
            elif typedmaterial == "Coal" or typedmaterial == "coal":
                print("Excellent. That will be", coalprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Iron" or typedmaterial == "iron":
                print("Excellent. That will be", ironprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Stone" or typedmaterial == "stone":
                print("Excellent. That will be", stoneprice,"krikor.")
                materialtradeloop = False
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")
            

    elif freetradein=="none":
        print("That's unfortunate. I hope we could do businesss sometime else.")
        input()

    else:
        print("An error has occurered. Please try again.")
        input()


def freetraderM():
    print("")
    pricefood=random.randint(20,30)
    woodprice=random.randint(250,500)
    coalprice=random.randint(500,750)
    ironprice=random.randint(500,1000)
    stoneprice=random.randint(100,500)
    epicweaponluck=random.randint(1,50)
    print("Hello my dear friend!")
    input()
    input("Today I have the following:")
    input("Food")
    input("Weapons")
    input("Materials")
    input("")
    freetradein=input("What would you like to buy? If you don't wish to purchase anything type none.")
    freetradein = freetradein.lower()
    if freetradein == "food":
        print(random.choice(traderexclamationsjoyful),"You will find that my selection of cusine is far above that of anyone else on this island.")
        input()
        print("I'll have them shipped directly to the doorsteps of your citizens - for a fair price, of course.")
        input()
        foodtradeloop = True
        while foodtradeloop == True:
            group_of_food = {"Steak", "Cooked Porkchop", "Jacket Potato", "Cooked Fish", "Bread", "Cooked Chicken"}
            num_to_select = 3
            list_of_random_food = random.sample(group_of_food, num_to_select)
            first_random_food = list_of_random_food[0]
            second_random_food = list_of_random_food[1]
            third_random_food = list_of_random_food[2]
            print("Today's selection is", first_random_food,",",second_random_food, "as well as", third_random_food,".")
            input()
            typedfood=str(input("What would you like to purchase? Please note that I am case sensitive."))
            if typedfood in {first_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {second_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {third_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            else:
                print("")
                input("I'm sorry. Unfortunately that is not a valid option. Please try again.")

    elif freetradein == "weapons":
        print(random.choice(traderexclamationsjoyful),"I guarantee that utterly destroying your enemies with these weapons will be much more fun than with any others.")
        input()
        print("And don't worry, all the correct sacrifices have been made. Your weapons won't turn on you in battle.")
        input()
        weapontradeloop = True
        while weapontradeloop == True:
            group_of_common_mweapons = {"Birch Stick", "Scarecrow", "Candlestick", "Elderwand", "Flameburst", "Thunderlord", "Merciful Killer", "Icestorm", "Enchanted Sword", "Void Staff", "Silver Lance", "Book of Runes", "Staff of the Sky", "Strength", "Tear Bringer"}
            num_to_select = 6
            list_of_random_common_mweapons = random.sample(group_of_common_mweapons, num_to_select)
            first_random_common_mweapon = list_of_random_common_mweapons[0]
            second_random_common_mweapon = list_of_random_common_mweapons[1]
            third_random_common_mweapon = list_of_random_common_mweapons[2]
            fourth_random_common_mweapon = list_of_random_common_mweapons[3]
            fifth_random_common_mweapon = list_of_random_common_mweapons[4]
            sixth_random_common_mweapon = list_of_random_common_mweapons[5]

            group_of_rare_mweapons = {"Earthliving", "Iron Tipped Staff", "Wood Cane", "Petrified Harp", "Arcane Bolt"}
            num_to_select = 2
            list_of_random_rare_mweapons = random.sample(group_of_rare_mweapons, num_to_select)
            first_random_rare_mweapon = list_of_random_rare_mweapons[0]
            second_random_rare_mweapon = list_of_random_rare_mweapons[1]

            print("Lucky for you, I have quite the selection right now. For common weapons, I can offer a", first_random_common_mweapon,", a", second_random_common_mweapon,", a", third_random_common_mweapon,", a", fourth_random_common_mweapon,", a", fifth_random_common_mweapon," and a", sixth_random_common_mweapon,".")
            input()
            print("As for rare weapons, a", first_random_rare_mweapon," and a", second_random_rare_mweapon,".")
            input()
            weapontradeloop = True
            
            group_of_epic_mweapons ={"Diablo", "Void Twig", "Ancient Wand", "Water Breath", "Liam Fart"}
            num_to_select = 1
            list_of_random_epic_mweapons = random.sample(group_of_epic_mweapons, num_to_select)
            random_epic_mweapon = list_of_random_epic_mweapons[0]
            if epicweaponluck == 7:
                print("Oh my. What is this...looks like you're in luck today! It seems as if I have an epic weapon in stock - the", random_epic_mweapon,"!")
            else:
                print("")

            typedweapon=str(input("Which weapon would you like to purchase? Please note that I am case sensitive."))
            if typedweapon in {first_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {second_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {third_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {fourth_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {fifth_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {sixth_random_common_mweapon}:
                print("Excellent. That will be", price1,"krikor.")
                weapontradeloop = False
                krikor=krikor-price1
                print("You now have", krikor, "krikor.")
            elif typedweapon in {first_random_rare_mweapon}:
                print("Excellent. That will be", price2,"krikor.")
                weapontradeloop = False
                krikor=krikor-price2
                print("You now have", krikor, "krikor.")
            elif typedweapon in {second_random_rare_mweapon}:
                print("Excellent. That will be", price2,"krikor.")
                weapontradeloop = False
                krikor=krikor-price2
                print("You now have", krikor, "krikor.")
            elif typedweapon in {random_epic_mweapon}:
                print("Excellent. That will be", price3,"krikor.")
                weapontradeloop = False
                krikor=krikor-price3
                print("You now have", krikor, "krikor.")
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")

    elif freetradein == "materials":
        print(random.choice(traderexclamationsjoyful), "I have a rather wide range of materials here for you to buy from me.")
        input()
        print("They might not be as cheap as those from your other friends, but I come round many times more often!")
        input()
        print("Its only fair you buy from me instead.")
        input()
        print("I have a selection of Wood, Coal, Iron and Stone.")
        input()
        materialtradeloop = True
        while materialtradeloop == True:
            typedmaterial=str(input("What would you like to purchase?"))
            if typedmaterial == "Wood" or typedmaterial == "wood":
                print("Excellent. That will", woodprice,"be krikor.")
                materialtradeloop = False
            elif typedmaterial == "Coal" or typedmaterial == "coal":
                print("Excellent. That will be", coalprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Iron" or typedmaterial == "iron":
                print("Excellent. That will be", ironprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Stone" or typedmaterial == "stone":
                print("Excellent. That will be", stoneprice,"krikor.")
                materialtradeloop = False
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")
            

    elif freetradein=="none":
        print("That's unfortunate. I hope we could do businesss sometime else.")
        input()

    else:
        print("An error has occurered. Please try again.")
        input()

def freetraderW():
    pricefood=random.randint(20,30)
    woodprice=random.randint(250,500)
    coalprice=random.randint(500,750)
    ironprice=random.randint(500,1000)
    stoneprice=random.randint(100,500)
    epicweaponluck=random.randint(0,50)
     print("Hello my dear friend!")
    input()
    input("Today I have the following:")
    input("Food")
    input("Weapons")
    input("Materials")
    input("")
    freetradein=input("What would you like to buy? If you don't wish to purchase anything type none.")
    freetradein = freetradein.lower()
    if freetradein == "food":
        print(random.choice(traderexclamationsjoyful),"You will find that my selection of cusine is far above that of anyone else on this island.")
        input()
        print("I'll have them shipped directly to the doorsteps of your citizens - for a fair price, of course.")
        input()
        foodtradeloop = True
        while foodtradeloop == True:
            group_of_food = {"Steak", "Cooked Porkchop", "Jacket Potato", "Cooked Fish", "Bread", "Cooked Chicken"}
            num_to_select = 3
            list_of_random_food = random.sample(group_of_food, num_to_select)
            first_random_food = list_of_random_food[0]
            second_random_food = list_of_random_food[1]
            third_random_food = list_of_random_food[2]
            
            print("Today's selection is", first_random_food,",",second_random_food, "as well as", third_random_food,".")
            input()
            typedfood=str(input("What food would you like to procure?"))
            if typedfood.lower() in {first_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood.lower() in {second_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood.lower() in {third_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            else:
                print("")
                input("I'm sorry. Unfortunately that is not a valid option. Please try again.")

    elif freetradein == "weapons":
        print(random.choice(traderexclamationsjoyful),"I guarantee that utterly destroying your enemies with these weapons will be much more fun than with any others.")
        input()
        print("And don't worry, all the correct sacrifices have been made. Your weapons won't turn on you in battle.")
        input()
        weapontradeloop = True
        while weapontradeloop == True:
            group_of_common_wweapons = {"Steel Sword", "Claws", "Bludgeon", "Scimitar", "Hammer", "Sabre", "Ida Sword", "Bolo Sword", "Hook", "Granite Mallet", "Strongwood Club", "Long Knife", "Dagger", "Katana Sword", "Bone Sword"}
            num_to_select = 6
            list_of_random_common_wweapons = random.sample(group_of_common_wweapons, num_to_select)
            first_random_common_wweapon = list_of_random_common_wweapons[0]
            second_random_common_wweapon = list_of_random_common_wweapons[1]
            third_random_common_wweapon = list_of_random_common_wweapons[2]
            fourth_random_common_wweapon = list_of_random_common_wweapons[3]
            fifth_random_common_wweapon = list_of_random_common_wweapons[4]
            sixth_random_common_wweapon = list_of_random_common_wweapons[5]
            group_of_rare_wweapons = {"Butterfly Sword", "Mandibles", "Gladius", "Halberd", "Doubleaxe"}
            num_to_select = 2
            list_of_random_rare_wweapons = random.sample(group_of_rare_wweapons, num_to_select)
            first_random_rare_wweapon = list_of_random_rare_wweapons[0]
            second_random_rare_wweapon = list_of_random_rare_wweapons[1]
            print("Lucky for you, I have quite the selection right now. For common weapons, I can offer a", first_random_common_wweapon,", a", second_random_common_wweapon,", a", third_random_common_wweapon,", a", fourth_random_common_wweapon,", a", fifth_random_common_wweapon," and a", sixth_random_common_wweapon,".")
            input()
            print("As for rare weapons, a", first_random_rare_wweapon," and a", second_random_rare_wweapon," are in stock.")
            input()
            weapontradeloop = False
            group_of_epic_wweapons ={"Zweireaper", "Greatsword", "Gemcrusher", "Katana", "Lunar Relic"}
            num_to_select = 1
            list_of_random_epic_wweapons = random.sample(group_of_epic_wweapons, num_to_select)
            random_epic_aweapon = list_of_random_epic_wweapons[0]
            if epicweaponluck == 7:
                print("Oh my. What is this...looks like you're in luck today! It seems as if I have an epic weapon in stock - the", random_epic_wweapon,"!")
                epicweaponluck=8
            else:
                print("")
                typedweapon=str(input("Which weapon would you like to purchase?"))
                if typedweapon.lower() in {first_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {second_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {third_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {fourth_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {fifth_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {sixth_random_common_wweapon}:
                    print("Excellent. That will be", price1,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price1
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {first_random_rare_wweapon}:
                    print("Excellent. That will be", price2,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price2
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {second_random_rare_wweapon}:
                    print("Excellent. That will be", price2,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price2
                    print("You now have", krikor, "krikor.")
                elif typedweapon.lower() in {random_epic_wweapon}:
                    print("Excellent. That will be", price3,"krikor.")
                    weapontradeloop = False
                    krikor=krikor-price3
                    print("You now have", krikor, "krikor.")
                else:
                    print("")
                    print("I'm sorry but that is not a valid option. Please try again.")

    elif freetradein == "materials":
        print(random.choice(traderexclamationsjoyful), "I have a rather wide range of materials here for you to buy from me.")
        input()
        print("They might not be as cheap as those from your other friends, but I come round many times more often!")
        input()
        print("Its only fair you buy from me instead.")
        input()
        print("I have a selection of Wood, Coal, Iron and Stone.")
        input()
        materialtradeloop = True
        while materialtradeloop == True:
            typedmaterial=str(input("What would you like to purchase?"))
            if typedmaterial == "Wood" or typedmaterial == "wood":
                print("Excellent. That will", woodprice,"be krikor.")
                materialtradeloop = False
            elif typedmaterial == "Coal" or typedmaterial == "coal":
                print("Excellent. That will be", coalprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Iron" or typedmaterial == "iron":
                print("Excellent. That will be", ironprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Stone" or typedmaterial == "stone":
                print("Excellent. That will be", stoneprice,"krikor.")
                materialtradeloop = False
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")
    elif freetradein=="none":
        print("That's unfortunate. I hope we could do businesss sometime else.")
        input()
    else:
        print("An error has occurered. Please try again.")
        input()
    
def freetraderA():
    print("")
    print("Hello my dear friend!")
    input()
    input("Today I have the following:")
    input("Food")
    input("Weapons")
    input("Materials")
    input("")
    freetradein=input("What would you like to buy? If you don't wish to purchase anything type none.")
    freetradein = freetradein.lower()
    if freetradein == "food":
        print(random.choice(traderexclamationsjoyful),"You will find that my selection of cusine is far above that of anyone else on this island.")
        input()
        print("I'll have them shipped directly to the doorsteps of your citizens - for a fair price, of course.")
        input()
        foodtradeloop = True
        while foodtradeloop == True:
            group_of_food = {"Steak", "Cooked Porkchop", "Jacket Potato", "Cooked Fish", "Bread", "Cooked Chicken"}
            num_to_select = 3
            list_of_random_food = random.sample(group_of_food, num_to_select)
            first_random_food = list_of_random_food[0]
            second_random_food = list_of_random_food[1]
            third_random_food = list_of_random_food[2]
            print("Today's selection is", first_random_food,",",second_random_food, "as well as", third_random_food,".")
            input()
            typedfood=str(input("What would you like to purchase? Please note that I am case sensitive."))
            if typedfood in {first_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {second_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            elif typedfood in {third_random_food}:
                print("Excellent! That'll be", pricefood,"krikor.")
                foodtradeloop=False
            else:
                print("")
                input("I'm sorry. Unfortunately that is not a valid option. Please try again.")

    elif freetradein == "weapons":
        print(random.choice(traderexclamationsjoyful),"I guarantee that utterly destroying your enemies with these weapons will be much more fun than with any others.")
        input()
        print("And don't worry, all the correct sacrifices have been made. Your weapons won't turn on you in battle.")
        input()
        weapontradeloop = True
        while weapontradeloop == True:

            group_of_common_aweapons = {"Spruce Bow", "Oak Longbow", "Refined Diorite Bow", "Ivy", "Breeze", "Liam"} #remove liam and add the 10 more weapons
            num_to_select = 6
            list_of_random_common_aweapons = random.sample(group_of_common_aweapons, num_to_select)
            first_random_common_aweapon = list_of_random_common_aweapons[0]
            second_random_common_aweapon = list_of_random_common_aweapons[1]
            third_random_common_aweapon = list_of_random_common_aweapons[2]
            fourth_random_common_aweapon = list_of_random_common_aweapons[3]
            fifth_random_common_aweapon = list_of_random_common_aweapons[4]
            sixth_random_common_aweapon = list_of_random_common_aweapons[5]

            group_of_rare_aweapons = {"Sharpshooter's Arch", "Petrified Ivory Bow", "Thunderbolt", "Trentbow", "Prizedbow"}
            num_to_select = 2
            list_of_random_rare_aweapons = random.sample(group_of_rare_aweapons, num_to_select)
            first_random_rare_aweapon = list_of_random_rare_aweapons[0]
            second_random_rare_aweapon = list_of_random_rare_aweapons[1]

            print("Lucky for you, I have quite the selection right now. For common weapons, I can offer a", first_random_common_aweapon,", a", second_random_common_aweapon,", a", third_random_common_aweapon,", a", fourth_random_common_aweapon,", a", fifth_random_common_aweapon," and a", sixth_random_common_aweapon,".")
            input()
            print("As for rare weapons, a", first_random_rare_aweapon," and a", second_random_rare_aweapon,".")
            input()
            weapontradeloop = True
            
            group_of_epic_aweapons ={"Sharpshooter's Ignis", "Az", "Iron String", "Flare's Crest", "Clustershock"}
            num_to_select = 1
            list_of_random_epic_aweapons = random.sample(group_of_epic_aweapons, num_to_select)
            random_epic_aweapon = list_of_random_epic_aweapons[0]
            if epicweaponluck == 7:
                print("Oh my. What is this...looks like you're in luck today! It seems as if I have an epic weapon in stock - the", random_epic_aweapon,"!")
            else:
                print("")

            typedweapon=str(input("Which weapon would you like to purchase? Please note that I am case sensitive."))
            if typedweapon in {first_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {second_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {third_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {fourth_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {fifth_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {sixth_random_common_aweapon}:
                print("Excellent. That will be", price1,"krikor.")
                krikor=krikor-price1
                weapontradeloop = False
            elif typedweapon in {first_random_rare_aweapon}:
                print("Excellent. That will be", price2,"krikor.")
                krikor=krikor-price2
                weapontradeloop = False
            elif typedweapon in {second_random_rare_aweapon}:
                print("Excellent. That will be", price2,"krikor.")
                krikor=krikor-price2
                weapontradeloop = False
            elif typedweapon in {random_epic_aweapon}:
                print("Excellent. That will be", price3,"krikor.")
                krikor=krikor-price3
                weapontradeloop = False
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")

    elif freetradein == "materials":
        print(random.choice(traderexclamationsjoyful), "I have a rather wide range of materials here for you to buy from me.")
        input()
        print("They might not be as cheap as those from your other friends, but I come round many times more often!")
        input()
        print("Its only fair you buy from me instead.")
        input()
        print("I have a selection of Wood, Coal, Iron and Stone.")
        input()
        materialtradeloop = True
        while materialtradeloop == True:
            typedmaterial=str(input("What would you like to purchase?"))
            if typedmaterial == "Wood" or typedmaterial == "wood":
                print("Excellent. That will", woodprice,"be krikor.")
                materialtradeloop = False
            elif typedmaterial == "Coal" or typedmaterial == "coal":
                print("Excellent. That will be", coalprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Iron" or typedmaterial == "iron":
                print("Excellent. That will be", ironprice,"krikor.")
                materialtradeloop = False
            elif typedmaterial == "Stone" or typedmaterial == "stone":
                print("Excellent. That will be", stoneprice,"krikor.")
                materialtradeloop = False
            else:
                print("")
                print("I'm sorry but that is not a valid option. Please try again.")
            

    elif freetradein=="none":
        print("That's unfortunate. I hope we could do businesss sometime else.")
        input()

    else:
        print("An error has occurered. Please try again.")
        input()

def everydaylifeT():
    print("")
    global Tpop
    global Tresources
    global Thappy
    global Tmilitary
    global Tmagic
    global krikor
    event1=random.randint(0,9)
    event2=random.randint (0,9)
    event3=random.randint(0,9)
    event4=random.randint (0,9)
    event5=random.randint(0,1)
    event6=random.randint (0,9)
    event7=random.randint (0,19)
    event8=random.randint (0,19)
    event9=random.randint(0,9)
    event10=random.randint (0,19)
    event11=random.randint(0,19)
    event12=random.randint (0,9)
    Jahestirrsacrifice1=False
    Jahestirrsacrifice2=False
    Jahestirrsacrifice3=False
    Jahestirrsacrifice4=False
    Jahestirrsacrifice5=False
    Arasacrifice1=False
    Arasacrifice2=False
    Arasacrifice3=False
    Arasacrifice4=False
    Arasacrifice5=False
    Esmyausacrifice1=False
    Esmyausacrifice2=False
    Esmyausacrifice3=False
    Esmyausacrifice4=False
    Esmyausacrifice5=False
    Umisirsacrifice1=False
    Umisirsacrifice2=False
    Umisirsacrifice3=False
    Umisirsacrifice4=False
    Umisirsacrifice5=False
    Trillinisacrifice1=False
    Trillinisacrifice2=False
    Trillinisacrifice3=False
    Trillinisacrifice4=False
    Trillinisacrifice5=False
    Lenicarasacrifice1=False
    Lenicarasacrifice2=False
    Lenicarasacrifice3=False
    Lenicarasacrifice4=False
    Lenicarasacrifice5=False
    Goaersacrifice1=False
    Goaersacrifice2=False
    Goaersacrifice3=False
    Goaersacrifice4=False
    Goaersacrifice5=False
    if event1==0 or event1==1 or event1==2 or event1==3 or event1==4 or event1==5:
        input("You must sacrifice to Jahestirr this week, god of the harvest.")
        Jahestirrsacrifice1=True
    else:
        input
    if event2==0 or event2==1 or event2==2 or event2==3:
        input("You must sacrifice to Ara this week, goddess of magic and love.")
        Arasacrifice1=True
    else:
        input
    if event3==0 or event3==1:
        input("You must sacrifice to Esmyau this week, goddess of peace.")
        Esmyausacrifice1=True
    else:
        input
    if event4==0:
        input("You must sacrifice to Umisir this week, god of happiness.")
        Umisirsacrifice1=True
    else:
        input
    if event5==0 or event5==1:
        input("You must sacrifice to Trillini this week, king of the Gods.")
        Trillinisacrifice1=True
    else:
        input
    if event6==0 or event6==1 or event6==2:
        input("You must sacrifice to Lenicara and Goaer this week, gods of luck and war.")
        Lenicarasacrifice1=True
        Goaersacrifice1=True
    else:
        input
    if event7==0:
        #CHANGE POP NATE FOR EACH CLAN
        Tpop=round(Tpop*0.96)
        print("There was a bad flood this week. You have lost 4% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event8==0:
        Tpop=round(Tpop*0.92)
        #CHANGE POP NATE FOR EACH CLAN
        print("There was a big fire this week. You have lost 8% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event9==0:
        input("There was a drought this week.")
    elif event9==1:
        input("There was good rainfall this week. You must sacrifice to Lenicara.")
        Lenicarasacrifice2=True
    else:
        input
    if event10==0 or event10==1 or event10==2:
        input("There was a bad harvest this week.")
    elif event10==3 or event10==4 or event10==5 or event10==6:
        input("There was a good harvest this week. You must sacrifice to Jahestirr.")
        Jahestirrsacrifice2=True
    else:
        input
    if event11==0 or event11==1 or event11==2:
        input("There was a wedding this week. You must sacrifice to Ara.")
        Arasacrifice2=True
    else:
        input
    if event12==0 or event12==1 or event12==2 or event12==3 or event12==4 or event12==5 or event12==6 or event12==7:
        input("The free trader has come to visit. ")
        freetraderT()
    else:
        input

    choicesacrificeJ=input("Do you want to sacrifice to Jahestirr? Yes or no?")
    if choicesacrificeJ.lower()=="yes" or choicesacrificeJ.lower()=="y":
        print("You shall sacrifice to Jahestirr.")
        choicesacrificeJamount=int(input("How many times would you like to sacrifice to Jahestirr?"))
        if choicesacrificeJamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeJamount==0:
            print("You changed your mind and decided not to sacrifice to Jahestirr.")
            input()
        elif choicesacrificeJamount==1:
            print("You gave one sacrifice to Jahestirr.")
            Jahestirrsacrifice1=False
            input()
            print("The sacrifice to Jahestirr cost you", Jsacriprice*1, "Krikor." )
            krikor=krikor-(Jsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==2:
            print("You gave two sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*2, "Krikor." )
            krikor=krikor-(Jsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==3:
            print("You gave three sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*3, "Krikor." )
            krikor=krikor-(Jsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==4:
            print("You gave four sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*4, "Krikor." )
            krikor=krikor-(Jsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==5:
            print("You gave five sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*5, "Krikor." )
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount>5:
            print("Jahestirr doesnt want that many sacrifices, so instead, you just gave him 5.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Jahestirr.")
        input()

    choicesacrificeA=input("Do you want to sacrifice to Ara? Yes or no?")
    if choicesacrificeA.lower()=="yes" or choicesacrificeA.lower()=="y":
        print("You shall sacrifice to Ara.")
        choicesacrificeAamount=int(input("How many times would you like to sacrifice to Ara?"))
        if choicesacrificeAamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeAamount==0:
            print("You changed your mind and decided not to sacrifice to Ara.")
            input()
        elif choicesacrificeAamount==1:
            print("You gave one sacrifice to Ara.")
            Arasacrifice1=False
            input()
            print("The sacrifice to Ara cost you", Asacriprice*1, "Krikor." )
            krikor=krikor-(Asacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==2:
            print("You gave two sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*2, "Krikor." )
            krikor=krikor-(Asacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==3:
            print("You gave three sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*3, "Krikor." )
            krikor=krikor-(Asacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==4:
            print("You gave four sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*4, "Krikor." )
            krikor=krikor-(Asacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==5:
            print("You gave five sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount>5:
            print("Ara doesnt want that many sacrifices, so instead, you just gave her 5.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Ara.")
        input()

    choicesacrificeE=input("Do you want to sacrifice to Esmyau? Yes or no?")
    if choicesacrificeE.lower()=="yes" or choicesacrificeE.lower()=="y":
        print("You shall sacrifice to Esmyau.")
        choicesacrificeEamount=int(input("How many times would you like to sacrifice to Esmyau?"))
        if choicesacrificeEamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeEamount==0:
            print("You changed your mind and decided not to sacrifice to Esmyau.")
            input()
        elif choicesacrificeEamount==1:
            print("You gave one sacrifice to Esmyau.")
            Esmyausacrifice1=False
            input()
            print("The sacrifice to Esmyau cost you", Esacriprice*1, "Krikor." )
            krikor=krikor-(Esacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==2:
            print("You gave two sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*2, "Krikor." )
            krikor=krikor-(Esacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==3:
            print("You gave three sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*3, "Krikor." )
            krikor=krikor-(Esacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==4:
            print("You gave four sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*4, "Krikor." )
            krikor=krikor-(Esacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==5:
            print("You gave five sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount>5:
            print("Esmyau doesnt want that many sacrifices, so instead, you just gave him 5.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Esmyau.")
        input()

    choicesacrificeU=input("Do you want to sacrifice to Umisir? Yes or no?")
    if choicesacrificeU.lower()=="yes" or choicesacrificeU.lower()=="y":
        print("You shall sacrifice to Umisir.")
        choicesacrificeUamount=int(input("How many times would you like to sacrifice to Umisir?"))
        if choicesacrificeUamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeUamount==0:
            print("You changed your mind and decided not to sacrifice to Umisir.")
            input()
        elif choicesacrificeUamount==1:
            print("You gave one sacrifice to Umisir.")
            Umisirsacrifice1=False
            input()
            print("The sacrifice to Umisir cost you", Usacriprice*1, "Krikor." )
            krikor=krikor-(Usacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==2:
            print("You gave two sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*2, "Krikor." )
            krikor=krikor-(Usacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==3:
            print("You gave three sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*3, "Krikor." )
            krikor=krikor-(Usacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==4:
            print("You gave four sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*4, "Krikor." )
            krikor=krikor-(Usacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==5:
            print("You gave five sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount>5:
            print("Umisir doesnt want that many sacrifices, so instead, you just gave him 5.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Umisir.")
        input()

    choicesacrificeT=input("Do you want to sacrifice to Trillini? Yes or no?")
    if choicesacrificeT.lower()=="yes" or choicesacrificeT.lower()=="y":
        print("You shall sacrifice to Trillini.")
        choicesacrificeTamount=int(input("How many times would you like to sacrifice to Trillini?"))
        if choicesacrificeTamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeTamount==0:
            print("You changed your mind and decided not to sacrifice to Trillini.")
            input()
        elif choicesacrificeTamount==1:
            print("You gave one sacrifice to Trillini.")
            input()
            print("The sacrifice to Trillini cost you", Tsacriprice*1, "Krikor." )
            Trillinisacrifice1=False
            krikor=krikor-(Tsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==2:
            print("You gave two sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*2, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            krikor=krikor-(Tsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==3:
            print("You gave three sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*3, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            krikor=krikor-(Tsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==4:
            print("You gave four sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*4, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            krikor=krikor-(Tsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==5:
            print("You gave five sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount>5:
            print("Trillini doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Trillini.")
        input()

    choicesacrificeL=input("Do you want to sacrifice to Lenicara? Yes or no?")
    if choicesacrificeL.lower()=="yes" or choicesacrificeL.lower()=="y":
        print("You shall sacrifice to Lenicara.")
        choicesacrificeLamount=int(input("How many times would you like to sacrifice to Lenicara?"))
        if choicesacrificeLamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeLamount==0:
            print("You changed your mind and decided not to sacrifice to Lenicara.")
            input()
        elif choicesacrificeLamount==1:
            print("You gave one sacrifice to Lenicara.")
            input()
            print("The sacrifice to Lenicara cost you", Lsacriprice*1, "Krikor." )
            Lenicarasacrifice1=False
            krikor=krikor-(Lsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==2:
            print("You gave two sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*2, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            krikor=krikor-(Lsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==3:
            print("You gave three sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*3, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            krikor=krikor-(Lsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==4:
            print("You gave four sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*4, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            krikor=krikor-(Lsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==5:
            print("You gave five sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount>5:
            print("Lenicara doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Lenicara.")
        input()

    choicesacrificeG=input("Do you want to sacrifice to Goaer? Yes or no?")
    if choicesacrificeG.lower()=="yes" or choicesacrificeG.lower()=="y":
        print("You shall sacrifice to Goaer.")
        choicesacrificeGamount=int(input("How many times would you like to sacrifice to Goaer?"))
        if choicesacrificeGamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeGamount==0:
            print("You changed your mind and decided not to sacrifice to Goaer.")
            input()
        elif choicesacrificeGamount==1:
            print("You gave one sacrifice to Goaer.")
            input()
            print("The sacrifice to Goaer cost you", Gsacriprice*1, "Krikor." )
            Goaersacrifice1=False
            krikor=krikor-(Gsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==2:
            print("You gave two sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*2, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            krikor=krikor-(Gsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==3:
            print("You gave three sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*3, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            krikor=krikor-(Gsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==4:
            print("You gave four sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*4, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            krikor=krikor-(Gsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==5:
            print("You gave five sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount>5:
            print("Goaer doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Goaer.")
        input()

    if Jahestirrsacrifice1==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Tresources=Tresources-10
        Thappy=Thappy-3
    if Jahestirrsacrifice2==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Tresources=Tresources-10
        Thappy=Thappy-3
    if Jahestirrsacrifice3==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Tresources=Tresources-10
        Thappy=Thappy-3
    if Jahestirrsacrifice4==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Tresources=Tresources-10
        Thappy=Thappy-3
    if Jahestirrsacrifice5==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Tresources=Tresources-10
        Thappy=Thappy-3
    if Arasacrifice1==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Thappy=Thappy-20
        Tmagic=Tmagic-15
    if Arasacrifice2==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Thappy=Thappy-20
        Tmagic=Tmagic-15
    if Arasacrifice3==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Thappy=Thappy-20
        Tmagic=Tmagic-15
    if Arasacrifice4==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Thappy=Thappy-20
        Tmagic=Tmagic-15
    if Arasacrifice5==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Thappy=Thappy-20
        Tmagic=Tmagic-15
    if Esmyausacrifice1==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Tpop=Tpop-1
        Thappy=Thappy-10
    if Esmyausacrifice2==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Tpop=Tpop-1
        Thappy=Thappy-10
    if Esmyausacrifice3==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Tpop=Tpop-1
        Thappy=Thappy-10
    if Esmyausacrifice4==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Tpop=Tpop-1
        Thappy=Thappy-10
    if Esmyausacrifice5==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Tpop=Tpop-1
        Thappy=Thappy-10
    if Umisirsacrifice1==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Thappy=Thappy-60
    if Umisirsacrifice2==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Thappy=Thappy-60
    if Umisirsacrifice3==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Thappy=Thappy-60
    if Umisirsacrifice4==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Thappy=Thappy-60
    if Umisirsacrifice5==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Thappy=Thappy-60
    if Trillinisacrifice1==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Tpop=Tpop-random.randint(100,150)
    if Trillinisacrifice2==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Tpop=Tpop-random.randint(100,150)
    if Trillinisacrifice3==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Tpop=Tpop-random.randint(100,150)
    if Trillinisacrifice4==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Tpop=Tpop-random.randint(100,150)
    if Trillinisacrifice5==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Tpop=Tpop-random.randint(100,150)
    if Lenicarasacrifice1==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Tpop=Tpop-10
        Thappy=Thappy-10
    if Lenicarasacrifice2==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Tpop=Tpop-10
        Thappy=Thappy-10
    if Lenicarasacrifice3==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Tpop=Tpop-10
        Thappy=Thappy-10
    if Lenicarasacrifice4==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Tpop=Tpop-10
        Thappy=Thappy-10
    if Lenicarasacrifice5==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Tpop=Tpop-10
        Thappy=Thappy-10
    if Goaersacrifice1==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Tmilitary=Tmilitary-4
    if Goaersacrifice2==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Tmilitary=Tmilitary-4
    if Goaersacrifice3==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Tmilitary=Tmilitary-4
    if Goaersacrifice4==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Tmilitary=Tmilitary-4
    if Goaersacrifice5==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Tmilitary=Tmilitary-4
    print("")
    print("")

def everydaylifeM():
    global Mpop
    global Mresources
    global Mhappy
    global Mmilitary
    global Mmagic
    global krikor
    event1=random.randint(0,9)
    event2=random.randint (0,9)
    event3=random.randint(0,9)
    event4=random.randint (0,9)
    event5=random.randint(0,1)
    event6=random.randint (0,9)
    event7=random.randint (0,19)
    event8=random.randint (0,19)
    event9=random.randint(0,9)
    event10=random.randint (0,19)
    event11=random.randint(0,19)
    event12=random.randint (0,9)
    Jahestirrsacrifice1=False
    Jahestirrsacrifice2=False
    Jahestirrsacrifice3=False
    Jahestirrsacrifice4=False
    Jahestirrsacrifice5=False
    Arasacrifice1=False
    Arasacrifice2=False
    Arasacrifice3=False
    Arasacrifice4=False
    Arasacrifice5=False
    Esmyausacrifice1=False
    Esmyausacrifice2=False
    Esmyausacrifice3=False
    Esmyausacrifice4=False
    Esmyausacrifice5=False
    Umisirsacrifice1=False
    Umisirsacrifice2=False
    Umisirsacrifice3=False
    Umisirsacrifice4=False
    Umisirsacrifice5=False
    Trillinisacrifice1=False
    Trillinisacrifice2=False
    Trillinisacrifice3=False
    Trillinisacrifice4=False
    Trillinisacrifice5=False
    Lenicarasacrifice1=False
    Lenicarasacrifice2=False
    Lenicarasacrifice3=False
    Lenicarasacrifice4=False
    Lenicarasacrifice5=False
    Goaersacrifice1=False
    Goaersacrifice2=False
    Goaersacrifice3=False
    Goaersacrifice4=False
    Goaersacrifice5=False
    if event1==0 or event1==1 or event1==2 or event1==3 or event1==4 or event1==5:
        input("You must sacrifice to Jahestirr this week, god of the harvest.")
        Jahestirrsacrifice1=True
    else:
        input
    if event2==0 or event2==1 or event2==2 or event2==3:
        input("You must sacrifice to Ara this week, goddess of magic and love.")
        Arasacrifice1=True
    else:
        input
    if event3==0 or event3==1:
        input("You must sacrifice to Esmyau this week, goddess of peace.")
        Esmyausacrifice1=True
    else:
        input
    if event4==0:
        input("You must sacrifice to Umisir this week, god of happiness.")
        Umisirsacrifice1=True
    else:
        input
    if event5==0 or event5==1:
        input("You must sacrifice to Trillini this week, king of the Gods.")
        Trillinisacrifice1=True
    else:
        input
    if event6==0 or event6==1 or event6==2:
        input("You must sacrifice to Lenicara and Goaer this week, gods of luck and war.")
        Lenicarasacrifice1=True
        Goaersacrifice1=True
    else:
        input
    if event7==0:
        #CHANGE POP NAME FOR EACH CLAN
        Mpop=round(Mpop*0.96)
        print("There was a bad flood this week. You have lost 4% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event8==0:
        Mpop=round(Mpop*0.92)
        #CHANGE POP NAME FOR EACH CLAN
        print("There was a big fire this week. You have lost 8% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event9==0:
        input("There was a drought this week.")
    elif event9==1:
        input("There was good rainfall this week. You must sacrifice to Lenicara.")
        Lenicarasacrifice2=True
    else:
        input
    if event10==0 or event10==1 or event10==2:
        input("There was a bad harvest this week.")
    elif event10==3 or event10==4 or event10==5 or event10==6:
        input("There was a good harvest this week. You must sacrifice to Jahestirr.")
        Jahestirrsacrifice2=True
    else:
        input
    if event11==0 or event11==1 or event11==2:
        input("There was a wedding this week. You must sacrifice to Ara.")
        Arasacrifice2=True
    else:
        input
    if event12==0 or event12==1 or event12==2 or event12==3 or event12==4 or event12==5 or event12==6 or event12==7:
        input("The free trader has come to visit. ")
        freetraderM()
    else:
        input

    choicesacrificeJ=input("Do you want to sacrifice to Jahestirr? Yes or no?")
    if choicesacrificeJ.lower()=="yes" or choicesacrificeJ.lower()=="y":
        print("You shall sacrifice to Jahestirr.")
        choicesacrificeJamount=int(input("How many times would you like to sacrifice to Jahestirr?"))
        if choicesacrificeJamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeJamount==0:
            print("You changed your mind and decided not to sacrifice to Jahestirr.")
            input()
        elif choicesacrificeJamount==1:
            print("You gave one sacrifice to Jahestirr.")
            Jahestirrsacrifice1=False
            input()
            print("The sacrifice to Jahestirr cost you", Jsacriprice*1, "Krikor." )
            krikor=krikor-(Jsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==2:
            print("You gave two sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*2, "Krikor." )
            krikor=krikor-(Jsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==3:
            print("You gave three sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*3, "Krikor." )
            krikor=krikor-(Jsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==4:
            print("You gave four sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*4, "Krikor." )
            krikor=krikor-(Jsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==5:
            print("You gave five sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*5, "Krikor." )
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount>5:
            print("Jahestirr doesnt want that many sacrifices, so instead, you just gave him 5.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Jahestirr.")
        input()

    choicesacrificeA=input("Do you want to sacrifice to Ara? Yes or no?")
    if choicesacrificeA.lower()=="yes" or choicesacrificeA.lower()=="y":
        print("You shall sacrifice to Ara.")
        choicesacrificeAamount=int(input("How many times would you like to sacrifice to Ara?"))
        if choicesacrificeAamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeAamount==0:
            print("You changed your mind and decided not to sacrifice to Ara.")
            input()
        elif choicesacrificeAamount==1:
            print("You gave one sacrifice to Ara.")
            Arasacrifice1=False
            input()
            print("The sacrifice to Ara cost you", Asacriprice*1, "Krikor." )
            krikor=krikor-(Asacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==2:
            print("You gave two sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*2, "Krikor." )
            krikor=krikor-(Asacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==3:
            print("You gave three sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*3, "Krikor." )
            krikor=krikor-(Asacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==4:
            print("You gave four sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False

            Arasacrifice3=False
            Arasacrifice4=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*4, "Krikor." )
            krikor=krikor-(Asacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==5:
            print("You gave five sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount>5:
            print("Ara doesnt want that many sacrifices, so instead, you just gave her 5.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Ara.")
        input()

    choicesacrificeE=input("Do you want to sacrifice to Esmyau? Yes or no?")
    if choicesacrificeE.lower()=="yes" or choicesacrificeE.lower()=="y":
        print("You shall sacrifice to Esmyau.")
        choicesacrificeEamount=int(input("How many times would you like to sacrifice to Esmyau?"))
        if choicesacrificeEamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeEamount==0:
            print("You changed your mind and decided not to sacrifice to Esmyau.")
            input()
        elif choicesacrificeEamount==1:
            print("You gave one sacrifice to Esmyau.")
            Esmyausacrifice1=False
            input()
            print("The sacrifice to Esmyau cost you", Esacriprice*1, "Krikor." )
            krikor=krikor-(Esacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==2:
            print("You gave two sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*2, "Krikor." )
            krikor=krikor-(Esacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==3:
            print("You gave three sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*3, "Krikor." )
            krikor=krikor-(Esacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==4:
            print("You gave four sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*4, "Krikor." )
            krikor=krikor-(Esacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==5:
            print("You gave five sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount>5:
            print("Esmyau doesnt want that many sacrifices, so instead, you just gave him 5.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Esmyau.")
        input()

    choicesacrificeU=input("Do you want to sacrifice to Umisir? Yes or no?")
    if choicesacrificeU.lower()=="yes" or choicesacrificeU.lower()=="y":
        print("You shall sacrifice to Umisir.")
        choicesacrificeUamount=int(input("How many times would you like to sacrifice to Umisir?"))
        if choicesacrificeUamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeUamount==0:
            print("You changed your mind and decided not to sacrifice to Umisir.")
            input()
        elif choicesacrificeUamount==1:
            print("You gave one sacrifice to Umisir.")
            Umisirsacrifice1=False
            input()
            print("The sacrifice to Umisir cost you", Usacriprice*1, "Krikor." )
            krikor=krikor-(Usacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==2:
            print("You gave two sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*2, "Krikor." )
            krikor=krikor-(Usacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==3:
            print("You gave three sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*3, "Krikor." )
            krikor=krikor-(Usacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==4:
            print("You gave four sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*4, "Krikor." )
            krikor=krikor-(Usacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==5:
            print("You gave five sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount>5:
            print("Umisir doesnt want that many sacrifices, so instead, you just gave him 5.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Umisir.")
        input()

    choicesacrificeT=input("Do you want to sacrifice to Trillini? Yes or no?")
    if choicesacrificeT.lower()=="yes" or choicesacrificeT.lower()=="y":
        print("You shall sacrifice to Trillini.")
        choicesacrificeTamount=int(input("How many times would you like to sacrifice to Trillini?"))
        if choicesacrificeTamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeTamount==0:
            print("You changed your mind and decided not to sacrifice to Trillini.")
            input()
        elif choicesacrificeTamount==1:
            print("You gave one sacrifice to Trillini.")
            input()
            print("The sacrifice to Trillini cost you", Tsacriprice*1, "Krikor." )
            Trillinisacrifice1=False
            krikor=krikor-(Tsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==2:
            print("You gave two sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*2, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            krikor=krikor-(Tsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==3:
            print("You gave three sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*3, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            krikor=krikor-(Tsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==4:
            print("You gave four sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*4, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            krikor=krikor-(Tsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==5:
            print("You gave five sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount>5:
            print("Trillini doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Trillini.")
        input()

    choicesacrificeL=input("Do you want to sacrifice to Lenicara? Yes or no?")
    if choicesacrificeL.lower()=="yes" or choicesacrificeL.lower()=="y":
        print("You shall sacrifice to Lenicara.")
        choicesacrificeLamount=int(input("How many times would you like to sacrifice to Lenicara?"))
        if choicesacrificeLamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeLamount==0:
            print("You changed your mind and decided not to sacrifice to Lenicara.")
            input()
        elif choicesacrificeLamount==1:
            print("You gave one sacrifice to Lenicara.")
            input()
            print("The sacrifice to Lenicara cost you", Lsacriprice*1, "Krikor." )
            Lenicarasacrifice1=False
            krikor=krikor-(Lsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==2:
            print("You gave two sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*2, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            krikor=krikor-(Lsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==3:
            print("You gave three sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*3, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            krikor=krikor-(Lsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==4:
            print("You gave four sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*4, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            krikor=krikor-(Lsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==5:
            print("You gave five sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount>5:
            print("Lenicara doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Lenicara.")
        input()

    choicesacrificeG=input("Do you want to sacrifice to Goaer? Yes or no?")
    if choicesacrificeG.lower()=="yes" or choicesacrificeG.lower()=="y":
        print("You shall sacrifice to Goaer.")
        choicesacrificeGamount=int(input("How many times would you like to sacrifice to Goaer?"))
        if choicesacrificeGamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeGamount==0:
            print("You changed your mind and decided not to sacrifice to Goaer.")
            input()
        elif choicesacrificeGamount==1:
            print("You gave one sacrifice to Goaer.")
            input()
            print("The sacrifice to Goaer cost you", Gsacriprice*1, "Krikor." )
            Goaersacrifice1=False
            krikor=krikor-(Gsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==2:
            print("You gave two sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*2, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            krikor=krikor-(Gsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==3:
            print("You gave three sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*3, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            krikor=krikor-(Gsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==4:
            print("You gave four sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*4, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            krikor=krikor-(Gsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==5:
            print("You gave five sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount>5:
            print("Goaer doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Goaer.")
        input()

    if Jahestirrsacrifice1==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Mresources=Mresources-10
        Mhappy=Mhappy-3
    if Jahestirrsacrifice2==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Mresources=Mresources-10
        Mhappy=Mhappy-3
    if Jahestirrsacrifice3==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Mresources=Mresources-10
        Mhappy=Mhappy-3
    if Jahestirrsacrifice4==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Mresources=Mresources-10
        Mhappy=Mhappy-3
    if Jahestirrsacrifice5==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Mresources=Mresources-10
        Mhappy=Mhappy-3
    if Arasacrifice1==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Mhappy=Mhappy-20
        Mmagic=Mmagic-15
    if Arasacrifice2==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Mhappy=Mhappy-20
        Mmagic=Mmagic-15
    if Arasacrifice3==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Mhappy=Mhappy-20
        Mmagic=Mmagic-15
    if Arasacrifice4==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Mhappy=Mhappy-20
        Mmagic=Mmagic-15
    if Arasacrifice5==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy and takes some of your magic.")
        Mhappy=Mhappy-20
        Mmagic=Mmagic-15
    if Esmyausacrifice1==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Mpop=Mpop-1
        Mhappy=Mhappy-10
    if Esmyausacrifice2==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Mpop=Mpop-1
        Mhappy=Mhappy-10
    if Esmyausacrifice3==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Mpop=Mpop-1
        Mhappy=Mhappy-10
    if Esmyausacrifice4==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Mpop=Mpop-1
        Mhappy=Mhappy-10
    if Esmyausacrifice5==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Mpop=Mpop-1
        Mhappy=Mhappy-10
    if Umisirsacrifice1==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Mhappy=Mhappy-60
    if Umisirsacrifice2==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Mhappy=Mhappy-60
    if Umisirsacrifice3==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Mhappy=Mhappy-60
    if Umisirsacrifice4==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Mhappy=Mhappy-60
    if Umisirsacrifice5==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Mhappy=Mhappy-60
    if Trillinisacrifice1==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Mpop=Mpop-random.randint(100,150)
    if Trillinisacrifice2==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Mpop=Mpop-random.randint(100,150)
    if Trillinisacrifice3==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Mpop=Mpop-random.randint(100,150)
    if Trillinisacrifice4==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Mpop=Mpop-random.randint(100,150)
    if Trillinisacrifice5==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Mpop=Mpop-random.randint(100,150)
    if Lenicarasacrifice1==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Mpop=Mpop-10
        Mhappy=Mhappy-10
    if Lenicarasacrifice2==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Mpop=Mpop-10
        Mhappy=Mhappy-10
    if Lenicarasacrifice3==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Mpop=Mpop-10
        Mhappy=Mhappy-10
    if Lenicarasacrifice4==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Mpop=Mpop-10
        Mhappy=Mhappy-10
    if Lenicarasacrifice5==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Mpop=Mpop-10
        Mhappy=Mhappy-10
    if Goaersacrifice1==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Mmilitary=Mmilitary-4
    if Goaersacrifice2==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Mmilitary=Mmilitary-4
    if Goaersacrifice3==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Mmilitary=Mmilitary-4
    if Goaersacrifice4==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Mmilitary=Mmilitary-4
    if Goaersacrifice5==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Mmilitary=Mmilitary-4
    print("")
    print("")


def everydaylifeW():
    global Wpop
    global Wresources
    global Whappy
    global Wmilitary
    global krikor
    event1=random.randint(0,9)
    event2=random.randint (0,9)
    event3=random.randint(0,9)
    event4=random.randint (0,9)
    event5=random.randint(0,1)
    event6=random.randint (0,9)
    event7=random.randint (0,19)
    event8=random.randint (0,19)
    event9=random.randint(0,9)
    event10=random.randint (0,19)
    event11=random.randint(0,19)
    event12=random.randint (0,9)
    Jahestirrsacrifice1=False
    Jahestirrsacrifice2=False
    Jahestirrsacrifice3=False
    Jahestirrsacrifice4=False
    Jahestirrsacrifice5=False
    Arasacrifice1=False
    Arasacrifice2=False
    Arasacrifice3=False
    Arasacrifice4=False
    Arasacrifice5=False
    Esmyausacrifice1=False
    Esmyausacrifice2=False
    Esmyausacrifice3=False
    Esmyausacrifice4=False
    Esmyausacrifice5=False
    Umisirsacrifice1=False
    Umisirsacrifice2=False
    Umisirsacrifice3=False
    Umisirsacrifice4=False
    Umisirsacrifice5=False
    Trillinisacrifice1=False
    Trillinisacrifice2=False
    Trillinisacrifice3=False
    Trillinisacrifice4=False
    Trillinisacrifice5=False
    Lenicarasacrifice1=False
    Lenicarasacrifice2=False
    Lenicarasacrifice3=False
    Lenicarasacrifice4=False
    Lenicarasacrifice5=False
    Goaersacrifice1=False
    Goaersacrifice2=False
    Goaersacrifice3=False
    Goaersacrifice4=False
    Goaersacrifice5=False
    
    if event1==0 or event1==1 or event1==2 or event1==3 or event1==4 or event1==5:
        input("You must sacrifice to Jahestirr this week, god of the harvest.")
        Jahestirrsacrifice1=True
    else:
        input
    if event2==0 or event2==1 or event2==2 or event2==3:
        input("You must sacrifice to Ara this week, goddess of magic and love.")
        Arasacrifice1=True
    else:
        input
    if event3==0 or event3==1:
        input("You must sacrifice to Esmyau this week, goddess of peace.")
        Esmyausacrifice1=True
    else:
        input
    if event4==0:
        input("You must sacrifice to Umisir this week, god of happiness.")
        Umisirsacrifice1=True
    else:
        input
    if event5==0 or event5==1:
        input("You must sacrifice to Trillini this week, king of the Gods.")
        Trillinisacrifice1=True
    else:
        input
    if event6==0 or event6==1 or event6==2:
        input("You must sacrifice to Lenicara and Goaer this week, gods of luck and war.")
        Lenicarasacrifice1=True
        Goaersacrifice1=True
    else:
        input
    if event7==0:
        #CHANGE POP NAME FOR EACH CLAN
        Wpop=round(Wpop*0.96)
        print("There was a bad flood this week. You have lost 4% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event8==0:
        Wpop=round(Wpop*0.92)
        #CHANGE POP NAME FOR EACH CLAN
        print("There was a big fire this week. You have lost 8% of your population. Your current population is", Wpop, ".")
    else:
        input
    if event9==0:
        input("There was a drought this week.")
    elif event9==1:
        input("There was good rainfall this week. You must sacrifice to Lenicara.")
        Lenicarasacrifice2=True
    else:
        input
    if event10==0 or event10==1 or event10==2:
        input("There was a bad harvest this week.")
    elif event10==3 or event10==4 or event10==5 or event10==6:
        input("There was a good harvest this week. You must sacrifice to Jahestirr.")
        Jahestirrsacrifice2=True
    else:
        input
    if event11==0 or event11==1 or event11==2:
        input("There was a wedding this week. You must sacrifice to Ara.")
        Arasacrifice2=True
    else:
        input
    if event12==0 or event12==1 or event12==2 or event12==3 or event12==4 or event12==5 or event12==6 or event12==7:
        input("The free trader has come to visit. ")
        freetraderW()
    else:
        input

    choicesacrificeJ=input("Do you want to sacrifice to Jahestirr? Yes or no?")
    if choicesacrificeJ.lower()=="yes" or choicesacrificeJ.lower()=="y":
        print("You shall sacrifice to Jahestirr.")
        choicesacrificeJamount=int(input("How many times would you like to sacrifice to Jahestirr?"))
        if choicesacrificeJamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeJamount==0:
            print("You changed your mind and decided not to sacrifice to Jahestirr.")
            input()
        elif choicesacrificeJamount==1:
            print("You gave one sacrifice to Jahestirr.")
            Jahestirrsacrifice1=False
            input()
            print("The sacrifice to Jahestirr cost you", Jsacriprice*1, "Krikor." )
            krikor=krikor-(Jsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==2:
            print("You gave two sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*2, "Krikor." )
            krikor=krikor-(Jsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==3:
            print("You gave three sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*3, "Krikor." )
            krikor=krikor-(Jsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==4:
            print("You gave four sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*4, "Krikor." )
            krikor=krikor-(Jsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==5:
            print("You gave five sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*5, "Krikor." )
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount>5:
            print("Jahestirr doesnt want that many sacrifices, so instead, you just gave him 5.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Jahestirr.")
        input()
        
    choicesacrificeA=input("Do you want to sacrifice to Ara? Yes or no?")
    if choicesacrificeA.lower()=="yes" or choicesacrificeA.lower()=="y":
        print("You shall sacrifice to Ara.")
        choicesacrificeAamount=int(input("How many times would you like to sacrifice to Ara?"))
        if choicesacrificeAamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeAamount==0:
            print("You changed your mind and decided not to sacrifice to Ara.")
            input()
        elif choicesacrificeAamount==1:
            print("You gave one sacrifice to Ara.")
            Arasacrifice1=False
            input()
            print("The sacrifice to Ara cost you", Asacriprice*1, "Krikor." )
            krikor=krikor-(Asacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==2:
            print("You gave two sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*2, "Krikor." )
            krikor=krikor-(Asacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==3:
            print("You gave three sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*3, "Krikor." )
            krikor=krikor-(Asacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==4:
            print("You gave four sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*4, "Krikor." )
            krikor=krikor-(Asacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==5:
            print("You gave five sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount>5:
            print("Ara doesnt want that many sacrifices, so instead, you just gave her 5.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Ara.")
        input()

    choicesacrificeE=input("Do you want to sacrifice to Esmyau? Yes or no?")
    if choicesacrificeE.lower()=="yes" or choicesacrificeE.lower()=="y":
        print("You shall sacrifice to Esmyau.")
        choicesacrificeEamount=int(input("How many times would you like to sacrifice to Esmyau?"))
        if choicesacrificeEamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeEamount==0:
            print("You changed your mind and decided not to sacrifice to Esmyau.")
            input()
        elif choicesacrificeEamount==1:
            print("You gave one sacrifice to Esmyau.")
            Esmyausacrifice1=False
            input()
            print("The sacrifice to Esmyau cost you", Esacriprice*1, "Krikor." )
            krikor=krikor-(Esacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==2:
            print("You gave two sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*2, "Krikor." )
            krikor=krikor-(Esacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==3:
            print("You gave three sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*3, "Krikor." )
            krikor=krikor-(Esacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==4:
            print("You gave four sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*4, "Krikor." )
            krikor=krikor-(Esacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==5:
            print("You gave five sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount>5:
            print("Esmyau doesnt want that many sacrifices, so instead, you just gave him 5.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Esmyau.")
        input()

    choicesacrificeU=input("Do you want to sacrifice to Umisir? Yes or no?")
    if choicesacrificeU.lower()=="yes" or choicesacrificeU.lower()=="y":
        print("You shall sacrifice to Umisir.")
        choicesacrificeUamount=int(input("How many times would you like to sacrifice to Umisir?"))
        if choicesacrificeUamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeUamount==0:
            print("You changed your mind and decided not to sacrifice to Umisir.")
            input()
        elif choicesacrificeUamount==1:
            print("You gave one sacrifice to Umisir.")
            Umisirsacrifice1=False
            input()
            print("The sacrifice to Umisir cost you", Usacriprice*1, "Krikor." )
            krikor=krikor-(Usacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==2:
            print("You gave two sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*2, "Krikor." )
            krikor=krikor-(Usacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==3:
            print("You gave three sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*3, "Krikor." )
            krikor=krikor-(Usacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==4:
            print("You gave four sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*4, "Krikor." )
            krikor=krikor-(Usacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==5:
            print("You gave five sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount>5:
            print("Umisir doesnt want that many sacrifices, so instead, you just gave him 5.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Umisir.")
        input()

    choicesacrificeT=input("Do you want to sacrifice to Trillini? Yes or no?")
    if choicesacrificeT.lower()=="yes" or choicesacrificeT.lower()=="y":
        print("You shall sacrifice to Trillini.")
        choicesacrificeTamount=int(input("How many times would you like to sacrifice to Trillini?"))
        if choicesacrificeTamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeTamount==0:
            print("You changed your mind and decided not to sacrifice to Trillini.")
            input()
        elif choicesacrificeTamount==1:
            print("You gave one sacrifice to Trillini.")
            input()
            print("The sacrifice to Trillini cost you", Tsacriprice*1, "Krikor." )
            Trillinisacrifice1=False
            krikor=krikor-(Tsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==2:
            print("You gave two sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*2, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            krikor=krikor-(Tsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==3:
            print("You gave three sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*3, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            krikor=krikor-(Tsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==4:
            print("You gave four sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*4, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            krikor=krikor-(Tsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==5:
            print("You gave five sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount>5:
            print("Trillini doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Trillini.")
        input()

    choicesacrificeL=input("Do you want to sacrifice to Lenicara? Yes or no?")
    if choicesacrificeL.lower()=="yes" or choicesacrificeL.lower()=="y":
        print("You shall sacrifice to Lenicara.")
        choicesacrificeLamount=int(input("How many times would you like to sacrifice to Lenicara?"))
        if choicesacrificeLamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeLamount==0:
            print("You changed your mind and decided not to sacrifice to Lenicara.")
            input()
        elif choicesacrificeLamount==1:
            print("You gave one sacrifice to Lenicara.")
            input()
            print("The sacrifice to Lenicara cost you", Lsacriprice*1, "Krikor." )
            Lenicarasacrifice1=False
            krikor=krikor-(Lsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==2:
            print("You gave two sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*2, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            krikor=krikor-(Lsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==3:
            print("You gave three sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*3, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            krikor=krikor-(Lsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==4:
            print("You gave four sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*4, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            krikor=krikor-(Lsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==5:
            print("You gave five sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount>5:
            print("Lenicara doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Lenicara.")
        input()

    choicesacrificeG=input("Do you want to sacrifice to Goaer? Yes or no?")
    if choicesacrificeG.lower()=="yes" or choicesacrificeG.lower()=="y":
        print("You shall sacrifice to Goaer.")
        choicesacrificeGamount=int(input("How many times would you like to sacrifice to Goaer?"))
        if choicesacrificeGamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeGamount==0:
            print("You changed your mind and decided not to sacrifice to Goaer.")
            input()
        elif choicesacrificeGamount==1:
            print("You gave one sacrifice to Goaer.")
            input()
            print("The sacrifice to Goaer cost you", Gsacriprice*1, "Krikor." )
            Goaersacrifice1=False
            krikor=krikor-(Gsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==2:
            print("You gave two sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*2, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            krikor=krikor-(Gsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==3:
            print("You gave three sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*3, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            krikor=krikor-(Gsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==4:
            print("You gave four sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*4, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            krikor=krikor-(Gsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==5:
            print("You gave five sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount>5:
            print("Goaer doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Goaer.")
        input()

    if Jahestirrsacrifice1==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Wresources=Wresources-10
        Whappy=Whappy-3
    if Jahestirrsacrifice2==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Wresources=Wresources-10
        Whappy=Whappy-3
    if Jahestirrsacrifice3==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Wresources=Wresources-10
        Whappy=Whappy-3
    if Jahestirrsacrifice4==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Wresources=Wresources-10
        Whappy=Whappy-3
    if Jahestirrsacrifice5==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Wresources=Wresources-10
        Whappy=Whappy-3
    if Arasacrifice1==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Whappy=Whappy-20
    if Arasacrifice2==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Whappy=Whappy-20
    if Arasacrifice3==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Whappy=Whappy-20
    if Arasacrifice4==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Whappy=Whappy-20
    if Arasacrifice5==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Whappy=Whappy-20
    if Esmyausacrifice1==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Wpop=Wpop-1
        Whappy=Whappy-10
    if Esmyausacrifice2==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Wpop=Wpop-1
        Whappy=Whappy-10
    if Esmyausacrifice3==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Wpop=Wpop-1
        Whappy=Whappy-10
    if Esmyausacrifice4==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Wpop=Wpop-1
        Whappy=Whappy-10
    if Esmyausacrifice5==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Wpop=Wpop-1
        Whappy=Whappy-10
    if Umisirsacrifice1==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Whappy=Whappy-60
    if Umisirsacrifice2==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Whappy=Whappy-60
    if Umisirsacrifice3==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Whappy=Whappy-60
    if Umisirsacrifice4==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Whappy=Whappy-60
    if Umisirsacrifice5==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Whappy=Whappy-60
    if Trillinisacrifice1==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Wpop=Wpop-random.randint(100,150)
    if Trillinisacrifice2==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Wpop=Wpop-random.randint(100,150)
    if Trillinisacrifice3==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Wpop=Wpop-random.randint(100,150)
    if Trillinisacrifice4==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Wpop=Wpop-random.randint(100,150)
    if Trillinisacrifice5==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Wpop=Wpop-random.randint(100,150)
    if Lenicarasacrifice1==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Wpop=Wpop-10
        Whappy=Whappy-10
    if Lenicarasacrifice2==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Wpop=Wpop-10
        Whappy=Whappy-10
    if Lenicarasacrifice3==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Wpop=Wpop-10
        Whappy=Whappy-10
    if Lenicarasacrifice4==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Wpop=Wpop-10
        Whappy=Whappy-10
    if Lenicarasacrifice5==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Wpop=Wpop-10
        Whappy=Whappy-10
    if Goaersacrifice1==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Wmilitary=Wmilitary-4
    if Goaersacrifice2==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Wmilitary=Wmilitary-4
    if Goaersacrifice3==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Wmilitary=Wmilitary-4
    if Goaersacrifice4==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Wmilitary=Wmilitary-4
    if Goaersacrifice5==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Wmilitary=Wmilitary-4
    print("")
    print("")


def everydaylifeA():
    global Apop
    global Aresources
    global Ahappy
    global Amilitary
    global krikor
    
    event1=random.randint(0,9)
    event2=random.randint (0,9)
    event3=random.randint(0,9)
    event4=random.randint (0,9)
    event5=random.randint(0,1)
    event6=random.randint (0,9)
    event7=random.randint (0,19)
    event8=random.randint (0,19)
    event9=random.randint(0,9)
    event10=random.randint (0,19)
    event11=random.randint(0,19)
    event12=random.randint (0,9)
    
    Jahestirrsacrifice1=False
    Jahestirrsacrifice2=False
    Jahestirrsacrifice3=False
    Jahestirrsacrifice4=False
    Jahestirrsacrifice5=False
    Arasacrifice1=False
    Arasacrifice2=False
    Arasacrifice3=False
    Arasacrifice4=False
    Arasacrifice5=False
    Esmyausacrifice1=False
    Esmyausacrifice2=False
    Esmyausacrifice3=False
    Esmyausacrifice4=False
    Esmyausacrifice5=False
    Umisirsacrifice1=False
    Umisirsacrifice2=False
    Umisirsacrifice3=False
    Umisirsacrifice4=False
    Umisirsacrifice5=False
    Trillinisacrifice1=False
    Trillinisacrifice2=False
    Trillinisacrifice3=False
    Trillinisacrifice4=False
    Trillinisacrifice5=False
    Lenicarasacrifice1=False
    Lenicarasacrifice2=False
    Lenicarasacrifice3=False
    Lenicarasacrifice4=False
    Lenicarasacrifice5=False
    Goaersacrifice1=False
    Goaersacrifice2=False
    Goaersacrifice3=False
    Goaersacrifice4=False
    Goaersacrifice5=False
    
    if event1==0 or event1==1 or event1==2 or event1==3 or event1==4 or event1==5:
        input("You must sacrifice to Jahestirr this week, god of the harvest.")
        Jahestirrsacrifice1=True
    else:
        input
    if event2==0 or event2==1 or event2==2 or event2==3:
        input("You must sacrifice to Ara this week, goddess of magic and love.")
        Arasacrifice1=True
    else:
        input
    if event3==0 or event3==1:
        input("You must sacrifice to Esmyau this week, goddess of peace.")
        Esmyausacrifice1=True
    else:
        input
    if event4==0:
        input("You must sacrifice to Umisir this week, god of happiness.")
        Umisirsacrifice1=True
    else:
        input
    if event5==0 or event5==1:
        input("You must sacrifice to Trillini this week, king of the Gods.")
        Trillinisacrifice1=True
    else:
        input
    if event6==0 or event6==1 or event6==2:
        input("You must sacrifice to Lenicara and Goaer this week, gods of luck and war.")
        Lenicarasacrifice1=True
        Goaersacrifice1=True
    else:
        input
    if event7==0:
        Apop=round(Apop*0.96)
        print("There was a bad flood this week. You have lost 4% of your population. Your current population is", Apop, ".")
    else:
        input
    if event8==0:
        Apop=round(Apop*0.92)
        print("There was a big fire this week. You have lost 8% of your population. Your current population is", Apop, ".")
    else:
        input
    if event9==0:
        input("There was a drought this week.")
    elif event9==1:
        input("There was good rainfall this week. You must sacrifice to Lenicara.")
        Lenicarasacrifice2=True
    else:
        input
    if event10==0 or event10==1 or event10==2:
        input("There was a bad harvest this week.")
    elif event10==3 or event10==4 or event10==5 or event10==6:
        input("There was a good harvest this week. You must sacrifice to Jahestirr.")
        Jahestirrsacrifice2=True
    else:
        input
    if event11==0 or event11==1 or event11==2:
        input("There was a wedding this week. You must sacrifice to Ara.")
        Arasacrifice2=True
    else:
        input
    if event12==0 or event12==1 or event12==2 or event12==3 or event12==4 or event12==5 or event12==6 or event12==7:
        input("The free trader has come to visit. ")
        freetraderA()
    else:
        input

    choicesacrificeJ=input("Do you want to sacrifice to Jahestirr? Yes or no?")
    if choicesacrificeJ.lower()=="yes" or choicesacrificeJ.lower()=="y":
        print("You shall sacrifice to Jahestirr.")
        choicesacrificeJamount=int(input("How many times would you like to sacrifice to Jahestirr?"))
        if choicesacrificeJamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeJamount==0:
            print("You changed your mind and decided not to sacrifice to Jahestirr.")
            input()
        elif choicesacrificeJamount==1:
            print("You gave one sacrifice to Jahestirr.")
            Jahestirrsacrifice1=False
            input()
            print("The sacrifice to Jahestirr cost you", Jsacriprice*1, "Krikor." )
            krikor=krikor-(Jsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==2:
            print("You gave two sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*2, "Krikor." )
            krikor=krikor-(Jsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==3:
            print("You gave three sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*3, "Krikor." )
            krikor=krikor-(Jsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==4:
            print("You gave four sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*4, "Krikor." )
            krikor=krikor-(Jsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount==5:
            print("You gave five sacrifices to Jahestirr.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            print("The sacrifices to Jahestirr cost you", Jsacriprice*5, "Krikor." )
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeJamount>5:
            print("Jahestirr doesnt want that many sacrifices, so instead, you just gave him 5.")
            Jahestirrsacrifice1=False
            Jahestirrsacrifice2=False
            Jahestirrsacrifice3=False
            Jahestirrsacrifice4=False
            Jahestirrsacrifice5=False
            input()
            krikor=krikor-(Jsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Jahestirr.")
        input()

    choicesacrificeA=input("Do you want to sacrifice to Ara? Yes or no?")
    if choicesacrificeA.lower()=="yes" or choicesacrificeA.lower()=="y":
        print("You shall sacrifice to Ara.")
        choicesacrificeAamount=int(input("How many times would you like to sacrifice to Ara?"))
        if choicesacrificeAamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeAamount==0:
            print("You changed your mind and decided not to sacrifice to Ara.")
            input()
        elif choicesacrificeAamount==1:
            print("You gave one sacrifice to Ara.")
            Arasacrifice1=False
            input()
            print("The sacrifice to Ara cost you", Asacriprice*1, "Krikor." )
            krikor=krikor-(Asacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==2:
            print("You gave two sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*2, "Krikor." )
            krikor=krikor-(Asacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==3:
            print("You gave three sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*3, "Krikor." )
            krikor=krikor-(Asacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==4:
            print("You gave four sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*4, "Krikor." )
            krikor=krikor-(Asacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount==5:
            print("You gave five sacrifices to Ara.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeAamount>5:
            print("Ara doesnt want that many sacrifices, so instead, you just gave her 5.")
            Arasacrifice1=False
            Arasacrifice2=False
            Arasacrifice3=False
            Arasacrifice4=False
            Arasacrifice5=False
            input()
            print("The sacrifices to Ara cost you", Asacriprice*5, "Krikor." )
            krikor=krikor-(Asacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Ara.")
        input()

    choicesacrificeE=input("Do you want to sacrifice to Esmyau? Yes or no?")
    if choicesacrificeE.lower()=="yes" or choicesacrificeE.lower()=="y":
        print("You shall sacrifice to Esmyau.")
        choicesacrificeEamount=int(input("How many times would you like to sacrifice to Esmyau?"))
        if choicesacrificeEamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeEamount==0:
            print("You changed your mind and decided not to sacrifice to Esmyau.")
            input()
        elif choicesacrificeEamount==1:
            print("You gave one sacrifice to Esmyau.")
            Esmyausacrifice1=False
            input()
            print("The sacrifice to Esmyau cost you", Esacriprice*1, "Krikor." )
            krikor=krikor-(Esacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==2:
            print("You gave two sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*2, "Krikor." )
            krikor=krikor-(Esacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==3:
            print("You gave three sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*3, "Krikor." )
            krikor=krikor-(Esacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==4:
            print("You gave four sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*4, "Krikor." )
            krikor=krikor-(Esacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount==5:
            print("You gave five sacrifices to Esmyau.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeEamount>5:
            print("Esmyau doesnt want that many sacrifices, so instead, you just gave him 5.")
            Esmyausacrifice1=False
            Esmyausacrifice2=False
            Esmyausacrifice3=False
            Esmyausacrifice4=False
            Esmyausacrifice5=False
            input()
            print("The sacrifices to Esmyau cost you", Esacriprice*5, "Krikor." )
            krikor=krikor-(Esacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Esmyau.")
        input()

    choicesacrificeU=input("Do you want to sacrifice to Umisir? Yes or no?")
    if choicesacrificeU.lower()=="yes" or choicesacrificeU.lower()=="y":
        print("You shall sacrifice to Umisir.")
        choicesacrificeUamount=int(input("How many times would you like to sacrifice to Umisir?"))
        if choicesacrificeUamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeUamount==0:
            print("You changed your mind and decided not to sacrifice to Umisir.")
            input()
        elif choicesacrificeUamount==1:
            print("You gave one sacrifice to Umisir.")
            Umisirsacrifice1=False
            input()
            print("The sacrifice to Umisir cost you", Usacriprice*1, "Krikor." )
            krikor=krikor-(Usacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==2:
            print("You gave two sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*2, "Krikor." )
            krikor=krikor-(Usacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==3:
            print("You gave three sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*3, "Krikor." )
            krikor=krikor-(Usacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==4:
            print("You gave four sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*4, "Krikor." )
            krikor=krikor-(Usacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount==5:
            print("You gave five sacrifices to Umisir.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeUamount>5:
            print("Umisir doesnt want that many sacrifices, so instead, you just gave him 5.")
            Umisirsacrifice1=False
            Umisirsacrifice2=False
            Umisirsacrifice3=False
            Umisirsacrifice4=False
            Umisirsacrifice5=False
            input()
            print("The sacrifices to Umisir cost you", Usacriprice*5, "Krikor." )
            krikor=krikor-(Usacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Umisir.")
        input()
    choicesacrificeT=input("Do you want to sacrifice to Trillini? Yes or no?")
    if choicesacrificeT.lower()=="yes" or choicesacrificeT.lower()=="y":
        print("You shall sacrifice to Trillini.")
        choicesacrificeTamount=int(input("How many times would you like to sacrifice to Trillini?"))
        if choicesacrificeTamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeTamount==0:
            print("You changed your mind and decided not to sacrifice to Trillini.")
            input()
        elif choicesacrificeTamount==1:
            print("You gave one sacrifice to Trillini.")
            input()
            print("The sacrifice to Trillini cost you", Tsacriprice*1, "Krikor." )
            Trillinisacrifice1=False
            krikor=krikor-(Tsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==2:
            print("You gave two sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*2, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            krikor=krikor-(Tsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==3:
            print("You gave three sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*3, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            krikor=krikor-(Tsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==4:
            print("You gave four sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*4, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            krikor=krikor-(Tsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount==5:
            print("You gave five sacrifices to Trillini.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeTamount>5:
            print("Trillini doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Trillini cost you", Tsacriprice*5, "Krikor." )
            Trillinisacrifice1=False
            Trillinisacrifice2=False
            Trillinisacrifice3=False
            Trillinisacrifice4=False
            Trillinisacrifice5=False
            krikor=krikor-(Tsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Trillini.")
        input()

    choicesacrificeL=input("Do you want to sacrifice to Lenicara? Yes or no?")
    if choicesacrificeL.lower()=="yes" or choicesacrificeL.lower()=="y":
        print("You shall sacrifice to Lenicara.")
        choicesacrificeLamount=int(input("How many times would you like to sacrifice to Lenicara?"))
        if choicesacrificeLamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeLamount==0:
            print("You changed your mind and decided not to sacrifice to Lenicara.")
            input()
        elif choicesacrificeLamount==1:
            print("You gave one sacrifice to Lenicara.")
            input()
            print("The sacrifice to Lenicara cost you", Lsacriprice*1, "Krikor." )
            Lenicarasacrifice1=False
            krikor=krikor-(Lsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==2:
            print("You gave two sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*2, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            krikor=krikor-(Lsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==3:
            print("You gave three sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*3, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            krikor=krikor-(Lsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==4:
            print("You gave four sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*4, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            krikor=krikor-(Lsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount==5:
            print("You gave five sacrifices to Lenicara.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeLamount>5:
            print("Lenicara doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Lenicara cost you", Lsacriprice*5, "Krikor." )
            Lenicarasacrifice1=False
            Lenicarasacrifice2=False
            Lenicarasacrifice3=False
            Lenicarasacrifice4=False
            Lenicarasacrifice5=False
            krikor=krikor-(Lsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Lenicara.")
        input()

    choicesacrificeG=input("Do you want to sacrifice to Goaer? Yes or no?")
    if choicesacrificeG.lower()=="yes" or choicesacrificeG.lower()=="y":
        print("You shall sacrifice to Goaer.")
        choicesacrificeGamount=int(input("How many times would you like to sacrifice to Goaer?"))
        if choicesacrificeGamount<0:
            print("You cannot give negative sacrifices. Thats just common sense. You dont sacrifice anything.")
            input()
        elif choicesacrificeGamount==0:
            print("You changed your mind and decided not to sacrifice to Goaer.")
            input()
        elif choicesacrificeGamount==1:
            print("You gave one sacrifice to Goaer.")
            input()
            print("The sacrifice to Goaer cost you", Gsacriprice*1, "Krikor." )
            Goaersacrifice1=False
            krikor=krikor-(Gsacriprice*1)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==2:
            print("You gave two sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*2, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            krikor=krikor-(Gsacriprice*2)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==3:
            print("You gave three sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*3, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            krikor=krikor-(Gsacriprice*3)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==4:
            print("You gave four sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*4, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            krikor=krikor-(Gsacriprice*4)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount==5:
            print("You gave five sacrifices to Goaer.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
        elif choicesacrificeGamount>5:
            print("Goaer doesnt want that many sacrifices, so instead, you just gave him 5.")
            input()
            print("The sacrifices to Goaer cost you", Gsacriprice*5, "Krikor." )
            Goaersacrifice1=False
            Goaersacrifice2=False
            Goaersacrifice3=False
            Goaersacrifice4=False
            Goaersacrifice5=False
            krikor=krikor-(Gsacriprice*5)
            input()
            print("You now have", krikor, "Krikor.")
            input()
    else:
        print("You shall not sacrifice to Goaer.")
        input()

    if Jahestirrsacrifice1==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Aresources=Aresources-10
        Ahappy=Ahappy-3
    if Jahestirrsacrifice2==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Aresources=Aresources-10
        Ahappy=Ahappy-3
    if Jahestirrsacrifice3==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Aresources=Aresources-10
        Ahappy=Ahappy-3
    if Jahestirrsacrifice4==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Aresources=Aresources-10
        Ahappy=Ahappy-3
    if Jahestirrsacrifice5==True:
        input("You forgot to sacrifice to Jahestirr. You have a terrible harvest.")
        Aresources=Aresources-10
        Ahappy=Ahappy-3
    if Arasacrifice1==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Ahappy=Ahappy-20
    if Arasacrifice2==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Ahappy=Ahappy-20
    if Arasacrifice3==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Ahappy=Ahappy-20
    if Arasacrifice4==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Ahappy=Ahappy-20
    if Arasacrifice5==True:
        input("You forgot to sacrifice to Ara. She magically makes you unhappy.")
        Ahappy=Ahappy-20
    if Esmyausacrifice1==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Apop=Apop-1
        Ahappy=Ahappy-10
    if Esmyausacrifice2==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Apop=Apop-1
        Ahappy=Ahappy-10
    if Esmyausacrifice3==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Apop=Apop-1
        Ahappy=Ahappy-10
    if Esmyausacrifice4==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Apop=Apop-1
        Ahappy=Ahappy-10
    if Esmyausacrifice5==True:
        input("You forgot to sacrifice to Esmyau. There is a brawl in the local pub and a man dies.")
        Apop=Apop-1
        Ahappy=Ahappy-10
    if Umisirsacrifice1==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Ahappy=Ahappy-60
    if Umisirsacrifice2==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Ahappy=Ahappy-60
    if Umisirsacrifice3==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Ahappy=Ahappy-60
    if Umisirsacrifice4==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Ahappy=Ahappy-60
    if Umisirsacrifice5==True:
        input("You forgot to sacrifice to Umisir. A wave of sadness spreads through your clan.")
        Ahappy=Ahappy-60
    if Trillinisacrifice1==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Apop=Apop-random.randint(100,150)
    if Trillinisacrifice2==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Apop=Apop-random.randint(100,150)
    if Trillinisacrifice3==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Apop=Apop-random.randint(100,150)
    if Trillinisacrifice4==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Apop=Apop-random.randint(100,150)
    if Trillinisacrifice5==True:
        input("You have angered the lord of the gods. He decimates your population, killing hundreds.")
        Apop=Apop-random.randint(100,150)
    if Lenicarasacrifice1==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Apop=Apop-10
        Ahappy=Ahappy-10
    if Lenicarasacrifice2==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Apop=Apop-10
        Ahappy=Ahappy-10
    if Lenicarasacrifice3==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Apop=Apop-10
        Ahappy=Ahappy-10
    if Lenicarasacrifice4==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Apop=Apop-10
        Ahappy=Ahappy-10
    if Lenicarasacrifice5==True:
        input("You forgot to sacrifice to Lenicara. Your raid on a nearby village fails.")
        Apop=Apop-10
        Ahappy=Ahappy-10
    if Goaersacrifice1==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Amilitary=Amilitary-4
    if Goaersacrifice2==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Amilitary=Amilitary-4
    if Goaersacrifice3==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Amilitary=Amilitary-4
    if Goaersacrifice4==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Amilitary=Amilitary-4
    if Goaersacrifice5==True:
        input("You forgot to sacrifice to Goaer. You are attacked by a nearby village but you fend them off.")
        Amilitary=Amilitary-4
        print("")
        print("")


def majorchoiceT():
    print("")
    Tmajorchoice=random.randint(1,3)
    print("On your way to breakfast you notace people gathered around the castle gates, screaming and crying.")
    input()
    print("As you enter the banquit hall your advisor come to you with very depressing news.")
    input()
    print('He tells you that "We have recieved word from the Warriors that the Archer clan have waged war on them.')
    print("We also recieved word from scouts on the boarders that Archer groups have been atacking our people and using their wooden flesh to make stronger bow.")
    print("What do you want to do, you can either a. send a small army to atack the small gangs of archers (chance of Trents dying) b. tell the people near the border to come into the castle for safety (must pay lots for food and transportaion of civilians. 1000 - 2000 Krikor to be precise) or c. do nothing what so ever (will make your population very angry).")
    Tmajorchoiceinput=input()
    if Tmajorchoiceinput == 'a':
        if Tmajorchoice == 1:
            civiliansdied=random.randint(200,500)
            troopssent=random.randint(600,800)
            died=troopssent+civiliansdied
            Tpop=Tpop-died
            print("A large group of Archers breached the boarder as your troops went to atack")
            print("All the Archers retreated, but not untill they killed many civilians and all your troops")
            input()
            print("They killed "+died+" Trents.")
            print("You now have a population of "+Tpop+".")
        else:
            troopssent=random.randint(400,500)
            print("You send "+troopssent+" troops and kill all the archers that invaded")
            input()
            troopsdied=random.randint(100,300)
            print(""+troopsdied+"Trents died in the procces")
            Tpop=Tpop-troopsdied
            input()
            print("You now have a population of "+Tpop+"")
                  
    if Tmajorchoiceinput == 'b':
        Tcrisispay=random.randint(1000,2000)
        krikor=krikor-Tcrisispay
        print("You tell the civilians neer the boarder to come to the castle for safety")
        input()              
        print("You must pay "+Tcrisispay+" Krikor")
        print("You now have "+krikor+" Krikor")
          
    if Tmajorchoiceinput == 'c':
              print("You tell your advisors to do absolutely nothing asuring them that it will be for the best")
              input()
              print("Later that day an angry mob starts protesting")
              input()
              mobanger=random.randint(40-50)
              Thappy=Thappy-mobanger
              print("You have angered your population severely")
              print("Your population is now "+Thappy+"% happy")

def archermagecomp():
    #reliant on ethan
    print("")
    print("You recieve news from the clan elders that it is time for the annual Projectile tournament.")
    input("")
    print("Do you decide to host the tournament? It is said that if you do win the tournament you will gain lots of riches, but if you lose, you will gain nothing.")
    input("")
    print("The amount of money you win or lose depends on how much you decide to bet.")
    archerparticipate=input("Would you like to participate?")

    projectile_event_loop = True
    while projectile_event_loop == True:
        
        if archerparticipate.lower()=="yes":
            archer_bet = raw_input("You have decided to enter the event. How much would you like to bet? 1000, 5000 or 10000 krikor? You currently have" ,krikor, "krikor.")
            if archer_bet == 1000:
                print("You have decided to bet 1000 krikor for the event.")  
                krikor=krikor-1000
                print("You now have", krikor, "krikor.")
                input()
                print("The tournament will take place in a week and you will recieve the results then.")
                projectile_event_loop = False

            elif archer_bet == 5000:
                print("You have decided to bet 5000 krikor for the event.")
                krikor=krikor-5000
                print("You now have", krikor, "krikor.")
                input()
                print("The tournament will take place in a week and you will recieve the results then.")
                projectile_event_loop = False

            elif archer_bet == 10000:
                print("You have decided to bet 10000 krikor for the event.")
                krikor=krikor-10000
                print("You now have", krikor, "krikor.")
                projectile_event_loop = False

            else:
                print("That is not a valid bet. Please try again")

    else:
        input("You have decided not to participate. There has been no change to your krikor.")

    tournamentwinA=random.randint(0,2)
    everydaylifeA()
    input("A week has passed.")
    if tournamentwinA == 1:
        print("The results of the Projectile Tournament have arrived from the mages!")
        input()
        print("The results are... in third place...")
        input("The trents!")
        print("In second place we have...")
        input("The mages!")
        print("And in first place...")
        input("The archers!")
        print("Congratulations on winning this years Projectile Tournament!")
        input()
        archer_bet=archer_bet + 10000
        print("You have gained" , archer_bet, "krikor as a gift from the other clans for winning!")
        krikor=krikor+archer_bet
        Apop=Apop+5
        Aresources=Aresources+50
        print("You currently have a poulation of", Apop, ", ", Aresources, " resources and", krikor, "krikor.")

    else:
        print("The results of the Projectile Tournament have arrived from the mages!")
        input()
        print("The results are... in third place...")
        input("The trents!")
        print("In second place we have...")
        input("The archers!")
        print("And in first place...")
        input("The mages!")
        print("Unfortunately since you have lost the tournament, you haven't gained any krikor, resources or troops.")
        input()
        print("There have been no changes to your population, resources or krikor.")

    
def majorchoiceM():
    global Mhappy
    print("Your clan has been invited to compete in one of the rare competitions in Trinity.")
    input()
    print("This particular competition is hosted by your friends, the archers, and is an archery contest.")
    input()
    print("With skills in ranged combat that all mages possess, archery shouldn't be too different, and most people can use bows.")
    input()
    print("The contest takes place next week and the winner gets a prize provided by the loser, and is followed by an open market day.")
    input()
    joincompM=input("Do you want to join the competition? Yes or No?")
    if joincompM == "yes" or joincompM == "y":
        print("Excellent! Your friends await your competition. Your people are happy to take part.")
        joinedcompM=True
        Mhappy=Mhappy+10
        everydaylifeM()
    else:
        print("A message will be sent to the archers to tell them you decline. This makes your people unhappy.")
        joinedcompM=False
        Mhappy=Mhappy-7
        everydaylifeM()
        
    if joinedcompM==True:
        print("The time for the competition has arrived.")
        archermagecomp()
        input("A week has passed.")
    else:
        input("A week has passed.")

def majorchoiceW():
    print("A traveller visited yesterday and, due to the fact that you sheltered him, he taught you how to mine deeper in order to get more minerals.")
    input("")
    print("By digging deeper you may become richer and gain more resources however some people may die of exhaustion.")
    input("")
    minedeeper=input("Do you want to mine deeper?")
    if minedeeper.lower()=="yes" or minedeeper.lower()=="y":
        input("You have decided to mine deeper. You have gained 1000 krikor, 60 resources and lost 6 men.")
        krikor=krikor+1000
        Wpop=Wpop-6
        Wresources=Wresources+60
        print("You currently have a poulation of", Wpop, ", ", Wresources, " resources and", krikor, "krikor.")
        input("")
    else:
        input("You have decided not to mine deeper. Your people are angry that you didnt take the opportunity, and become unhappy.")
        Whappy=Whappy-5
        
def majorchoiceA():
    print("You recieve news from the clan elders that it is time for the annual Projectile tournament.")
    input("")
    print("Do you decide to host the tournament? It is said that if you do win the tournament you will gain lots of riches, but if you lose, you will gain nothing.")
    input("")
    print("The amount of money you win or lose depends on how much you decide to bet.")
    archerparticipate=input("Would you like to participate?")

    projectile_event_loop = True
    while projectile_event_loop == True:
        
        if archerparticipate.lower()=="yes":
            archer_bet = raw_input("You have decided to enter the event. How much would you like to bet? 1000, 5000 or 10000 krikor? You currently have" ,krikor, "krikor.")
            if archer_bet == 1000:
                print("You have decided to bet 1000 krikor for the event.")  
                krikor=krikor-1000
                print("You now have", krikor, "krikor.")
                input()
                print("The tournament will take place in a week and you will recieve the results then.")
                projectile_event_loop = False

            elif archer_bet == 5000:
                print("You have decided to bet 5000 krikor for the event.")
                krikor=krikor-5000
                print("You now have", krikor, "krikor.")
                input()
                print("The tournament will take place in a week and you will recieve the results then.")
                projectile_event_loop = False

            elif archer_bet == 10000:
                print("You have decided to bet 10000 krikor for the event.")
                krikor=krikor-10000
                print("You now have", krikor, "krikor.")
                projectile_event_loop = False

            else:
                print("That is not a valid bet. Please try again")

    else:
        input("You have decided not to participate. There has been no change to your krikor.")
        
    if archerparticipate.lower()==yes:
        input("A week has passed.")
        print("The time for the competition has arrived.")
        archermagecomp()
        tournamentwinA=random.randint(0,2)
        everydaylifeA()
        tournamentwinA=random.randint(0,2)
        everydaylifeA()
        input("A week has passed.")
        if tournamentwinA == 1:
            print("The results of the Projectile Tournament have arrived from the mages!")
            input()
            print("In second place we have...")
            input("The mages!")
            print("And in first place...")
            input("The archers!")
            print("Congratulations on winning this years Projectile Tournament!")
            input()
            archer_bet=archer_bet*1.5
            print("You have gained" , archer_bet, "krikor as a gift from the other clans for winning!")
            krikor=krikor+archer_bet
            Apop=Apop+5
            Aresources=Aresources+50
            print("You currently have a poulation of", Apop, ", ", Aresources, " resources and", krikor, "krikor.")

        else:
            print("The results of the Projectile Tournament have arrived from the mages!")
            input()
            print("In second place we have...")
            input("The archers!")
            print("And in first place...")
            input("The mages!")
            print("Unfortunately since you have lost the tournament, you haven't gained any krikor, resources or troops.")
            input()
            print("There have been no changes to your population, resources or krikor.")
        
    else:
        input("A week has passed.")
        
def randchoice():
    global krikor
    global Thappy
    global Mhappy
    global Whappy
    global Ahappy
    global Tpop
    global Mpop
    global Wpop
    global Apop
            
    ocurance=random.randint(0,3)
    print("Before the normal week begins, something unusual happens.")
    if ocurance==0:
        print("""A clan oficial's daughter is to be wed.
He asks you to help coordinate the wedding.
Doing so will cause you to help with the cost of the wedding, but will make your population happy.
Do you want to help or decline?""")
        wedocur=input()
        if wedocur=='help':
            wedocurprice=random.randint(200,500)
            wedocurhappy=random.randint(5,10)
            if clan == trent:
                Thappy=Thappy+wedocurhapy
            if clan == mage:
                Mhappy=Mhappy+wedocurhapy
            if clan == warrior:
                Whappy=Whappy+wedocurhapy
            if clan == archer:
                Ahappy=Ahappy+wedocurhapy
            krikor=krikor-wedocurprice
            print("You help pay for the weding and orgainze a large parade.")
            print("You pay "+wedocurprice+" krikor. You now have "+krikor+" krikor and a happiness of "+Thappy+".")
            
        if wedocur=='decline':
            wedocurhapy=random.randint(5,10)
            if clan == trent:
                Thappy=Thappy-wedocurhapy
            if clan == mage:
                Mhappy=Mhappy-wedocurhapy
            if clan == warrior:
                Whappy=Whappy-wedocurhapy
            if clan == archer:
                Ahappy=Ahappy-wedocurhapy
            print("You decline the request saying that you are to busy. your population now has a happiness of "+Thappy+".")

    if ocurance==1:
        barbariantroop=random.randint(20,30)
        print("A small group of "+barbariantrooop+""" Barbarians have come into your borders.
Do you want to a. let them be and hope that they move along or b. send a small force to take care of them?""")

    if ocurance==2:
        cariagegood=random.randint(0,4)
        print("""Your lookout comes to you with news at the border.
He says that a man, either a messenger or a thief, in a cariage has been spotted heading towards the capital.
He asks if he should let it proceed or if he should shoot it.""")
        cariageaprochcap=input("Choose 'proceed' or 'attack'.")
        if cariageaprochcap=='proceed':
            if cariagegood==1:
                atacktole=random.randint(40,50)
                if clan == trent:
                    Tpop=Tpop-atacktole
                    print("""The carriage comes closer to the walls. As it aproaches several men step out and rain burning arrows down on the towns folk.
After a small skermish the raiders are killed and the bodies are counted.""")
                    print("You now have a population of "+Tpop+"")
                if clan == mage:
                    Mpop=Mpop-atacktole
                    print("""The carriage comes closer to the walls. As it aproaches several men step out and rain burning arrows down on the towns folk.
After a small skermish the raiders are killed and the bodies are counted.""")
                    print("You now have a population of "+Mpop+"")
                if clan == warrior:
                    Wpop=Wpop-atacktole
                    print("""The carriage comes closer to the walls. As it aproaches several men step out and rain burning arrows down on the towns folk.
After a small skermish the raiders are killed and the bodies are counted.""")
                    print("You now have a population of "+Wpop+"")
                if clan == archer:
                    Apop=Apop-atacktole
                    print("""The carriage comes closer to the walls. As it aproaches several men step out and rain burning arrows down on the towns folk.
After a small skermish the raiders are killed and the bodies are counted.""")
                    print("You now have a population of "+Apop+"")               
            else:
                gift=random.randint(100,300)
                krikor=krikor+gift
                print("They come with a crate of krikor as a gift to your people")
                print("You now have "+krikor+" krikor")

        if cariageaprochcap=='attack':
            print("The lookout goes off to get your guards, who shoot the carriage.")
            if cariagegood==1 or cariagegood==2:
                penence=random.randint(1000,1800)
                krikor=krikor-penence
                print("""Later, a scout returns to you with news of the cariage.
He says that it was actually an invitation to a wedding from the wariors.""")
                print("You must pay the warrior clan "+penence+" krikor to make up for this crime.")
                print("You now have "+krikor+" krikor.")
            else:
                lootcariage=random.randint(40,100)
                krikor=krikor+lootcariage
                print("""Later that day a scout returns to you with news of the cariage.
He says that it was infact a cariage with several barbarians hidden in barrels in the back.
The scout says that the cariage tipped over killing the barbarians.
He also presents you with a small chest of gold from the carriage.""")
                print("You now have "+krikor+" Krikor")
    if ocurance==3:               
        marriageproposalfrom=random.randint(0,1)
        if clan==trent:
            if marriageproposalfrom==0:
                print("You have been sent a message from the Warrior clan.")
            else:
                print("You have been sent a message from the Mage clan.")
        elif clan==mage:
            if marriageproposalfrom==0:
                print("You have been sent a message from the Trent clan.")
            else:
                print("You have been sent a message from the Archer clan.")
        elif clan==warrior:
            if marriageproposalfrom==0:
                print("You have been sent a message from the Trent clan.")
            else:
                print("You have been sent a rare message from the Mage clan.")
        elif clan==archer:
            print("You have been sent a message from the Mage clan.")
        input()
            
        if chargender=="boy":
            print("Their leader has a young daughter they would like you to marry. If you do, you will have to pay a dowry to the leader.")
            print("The dowry is 5,000 krikor, but a wife would be sure to double your clan's happiness.")
            input()
            marriageacceptance=input("Would you like to marry her? Yes or no?")
            if marriageacceptance.lower()=="yes" or marriageacceptance.lower()=="y":
                print("Your wedding takes place immediately. You are now married.")
                krikor=krikor-5000
                if clan == trent:
                    Thappy=Thappy*2
                    print("You now have", krikor, "krikor and a happiness of", Thappy, ".")
                if clan == mage:
                    Mhappy=Mhappy*2
                    print("You now have", krikor, "krikor and a happiness of", Mhappy, ".")
                if clan == warrior:
                    Whappy=Whappy*2
                    print("You now have", krikor, "krikor and a happiness of", Whappy, ".")
                if clan == archer:
                    Ahappy=Ahappy*2
                    print("You now have", krikor, "krikor and a happiness of", Ahappy, ".")
            else:
                print("You don't get married, and since the public never knew about this proposal, your happiness stays the same.")                       

        elif chargender=="girl":
            print("Their leader has a young son they would like you to marry. If you do, you will have to pay a dowry to the leader.")
            print("The dowry is 5,000 krikor, but a husband would be sure to double your clan's happiness.")
            input()
            marriageacceptance=input("Would you like to marry her?")
            if marriageacceptance.lower()=="yes" or marriageacceptance.lower()=="y" or marriageacceptance.lower()=="yeah":
                print("Your wedding takes place immediately. You are now married.")
                krikor=krikor-5000
                if clan ==trent:
                    Thappy=Thappy*2
                    print("You now have", krikor, "krikor and a happiness of", Thappy, ".")
                if clan ==mage:
                    Mhappy=Mhappy*2
                    print("You now have", krikor, "krikor and a happiness of", Mhappy, ".")
                if clan == warrior:
                    Whappy=Whappy*2
                    print("You now have", krikor, "krikor and a happiness of", Whappy, ".")
                if clan == archer:
                    Ahappy=Ahappy*2
                    print("You now have", krikor, "krikor and a happiness of", Ahappy, ".")
            else:
                print("You don't get married, and since the public never knew about this proposal, your happiness stays the same.")

def clanstats():
    if clan=="warrior":
        input("Your current stats are:")
        print("Population =",Wpop)
        print("Number of minors =",Wminors)
        print("Clan happiness =",Whappy)
        print("Number of workers  =",Wworkforce)
        print("Wood =",Wwood)
        print("Metals =",Wmetals)
        print("Food =",Wfood)
        print("General resources =",Wresources)
        print("Tax rates =",Wtaxes)
        print("Land =",Wland)
        print("Space used =",Wspaceused)
        print("Housing =",Whousing)
        print("Military forces =",Wmilitary)
        input("")
    elif clan=="trent":
        input("Your current stats are:")
        print("Population =",Tpop)
        print("Number of minors =",Tminors)
        print("Clan happiness =",Thappy)
        print("Number of workers  =",Tworkforce)
        print("Wood =",Twood)
        print("Metals =",Tmetals)
        print("Food =",Tfood)
        print("General resources =",Tresources)
        print("Tax rates =",Ttaxes)
        print("Land =",Tland)
        print("Space used =",Tspaceused)
        print("Housing =",Thousing)
        print("Military forces =",Tmilitary)
        print("Clan fatigue =",Tfatigue)
        input("")
    elif clan=="mage":
        input("Your current stats are:")
        print("Population =",Mpop)
        print("Number of minors =",Mminors)
        print("Clan happiness =",Mhappy)
        print("Number of workers  =",Mworkforce)
        print("Wood =",Mwood)
        print("Metals =",Mmetals)
        print("Food =",Mfood)
        print("General resources =",Mresources)
        print("Tax rates =",Mtaxes)
        print("Land =",Mland)
        print("Space used =",Mspaceused)
        print("Housing =",Mhousing)
        print("Clan Magic =",Mmagic)
        print("Military forces =",Mmilitarypower)
        input("")
    elif clan=="archer":
        input("Your current stats are:")
        print("Population =",Apop)
        print("Number of minors =",Aminors)
        print("Clan happiness =",Ahappy)
        print("Number of workers  =",Aworkforce)
        print("Wood =",Awood)
        print("Metals =",Ametals)
        print("Food =",Afood)
        print("General resources =",Aresources)
        print("Tax rates =",Ataxes)
        print("Land =",Aland)
        print("Housing =",Ahousing)
        print("Military forces =",Amilitary)
        input("")

def trentgame():
    trentinitialproblem()
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    clanstats()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    majorchoiceT()
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    clanstats()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    randchoice()
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    clanstats()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    input("A week has passed.")
    everydaylifeT()
    clanstats()


def magegame():
    mageinitialproblem()
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    clanstats()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    majorchoiceM()
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    clanstats()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    randchoice()
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()
    clanstats()
    input("A week has passed.")
    everydaylifeM()
    input("A week has passed.")
    everydaylifeM()


def warriorgame():
    warriorinitialproblem()
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    clanstats()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    majorchoiceW()
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    clanstats()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    randchoice()
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    clanstats()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    input("A week has passed.")
    everydaylifeW()
    clanstats()

def archergame():
    archerinitialproblem()
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    clanstats()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    majorchoiceA()
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    clanstats()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    randchoice()
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    clanstats()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    input("A week has passed.")
    everydaylifeA()
    clanstats()


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


def rules():
    print("")


def openinggame():
    print("You have entered the game of Trinity")
    input()
    startgame=input("Do you wish to begin the game, learn the rules and how to play, or change the presets? Type 'begin', 'rules' or 'presets'.")
    if startgame=="begin":
        trinity()
    elif startgame=="rules":
        rules()
        trinity()
    elif startgaame=="presets":
        presets()
        trinity()
openinggame()
