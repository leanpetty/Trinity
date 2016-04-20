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

#epic weapons
ww_zweireaper = "Zweireaper"
ww_greatsword = "Elven Greatsword"
ww_gemcrusher = "Gemcrusher"
ww_katana = "Nethersteel Katana"
ww_lunar = "Lunar Relic"

aw_ignis = "Legolas' Ignis"
aw_az = "Az"
aw_ironstring = "Iron String"
aw_flare = "Flare's Crest"
aw_liam = "Liam's Fart"

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

def introspeech():
    time.sleep(5)
    input("Welcome to the island of Trinity.")
    input("This small, unassuming island is actually home to the most amazing peoples imaginable.")
    time.sleep(2)
    input("These people have never left this island. Why would they? It was all they needed?")
    print("")
    input("But one day, a ship turned up on the horison, carrying the Barbarians.")
    input("These Barbarians were lesser creatures, who believed they could subjugate all others to their will.")
    time.sleep(3)
    input("So they attacked the peoples, killing adults and children alike, and decimating their land for centuries to come.")
    input("""Just five groups managed to survive this massacre:
        the Trents, the Mages, the Archers, the Warriors and the Rogues.""")
    input("In the face of this danger, they joined arms and pushed back the invading Barbarians to the edge of the island.")
    input("Most of the groups realised that they did not have the strength to defeat the Barbarians, and stopped their attack there.")
    input("But the Rogues were not satisfied with this stalemate. They amassed an army, encompassing all the Rogues.")
    input("They attacked the Barbarians, hoping to destroy them in all out war.")
    time.sleep(7)
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
    input("After years of training, you are finally ready to become a leader, and all the clans are clamouring to have you.")

def clanchoice():
    #for each choice, define a variable as being the clan choice to be used later in the program - Alex will do this
    print("Which of the clans do you want to join?")
    time.sleep(4)
    ccinput=input("Warriors, Trents, Mages or Archers?")
    if ccinput.lower() == warrior or ccinput.lower() == warriors:
        #warriors
    elif ccinput.lower() == trent or ccinput.lower() == trents:
        #trents
    elif ccinput.lower() == mage or ccinput.lower() == mages:
        #mages
    elif ccinput.lower() == archer or ccinput.lower() == archers:
        #archers

def initialsalesman():
    #salesman

def joinclan():
    #joinclan

def intro():
    introspeech()
    print("")
    time.sleep(2)
    clanchoice()
    print("")
    time.sleep(2)
    salesman()
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
