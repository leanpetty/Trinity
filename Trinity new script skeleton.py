import time
import random

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

aw_sprucebow = "Spruce Bow"
aw_longbow = "Oak Longbow"
aw_dioritebow = "Refined Diorite Bow"
aw_ivy = "Ivy"
aw_breeze = "Breeze"

mw_
mw_
mw_
mw_
mw_

tw_
tw_
tw_
tw_
tw_

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

mw_
mw_
mw_
mw_
mw_

tw_
tw_
tw_
tw_
tw_

#epic weapons
ww_zweireaper = "Zweireaper"
ww_greatsword = "Elven Greatsword"
ww_gemcrusher = "Gemcrusher"
ww_katana = "Nethersteel Katana"
ww_lunar = "Lunar Relic"

aw_ignis = "Bowman's Ignis"
aw_az = "Az"
aw_ironstring = "Iron String"
aw_flare = "Flare's Crest"
aw_liam = "Liam's Fart"

mw_
mw_
mw_
mw_
mw_

tw_
tw_
tw_
tw_
tw_

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
I'm afraid I dont have much of a selection though. All I can offer is
the..., the..., the..., the... or the... .
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

def mageinitialproblem():
    #mip

def warriorinitialproblem():
    #wip

def archerinitialproblem():
    #aip

def trentlife():
    #trentlife

def magelife():
    #magelife

def warriorlife():
    #warriorlife

def archerlife():
    #archerlife

def trentrand1():
    #random trentlife

def magerand1():
    #random magelife

def warriorrand1():
    #random warriorlife

def archerrand1():
    #random archerlifex

def trentgame():
    trentinitialproblem()
    trentrand1()

def magegame():
    mageinitialproblem()
    magerand1()

def warriorgame():
    warriorinitialproblem()
    warriorrand1()

def archergame():
    archerinitialproblem()
    archerrand1()

def clangame():
    #if/elif from clanchoice()

def trinity():
    intro()
    clangame()
