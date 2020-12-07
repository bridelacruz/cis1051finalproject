import random

class Player:
    def __init__(self):
        self.hp = 10
        self.maxhp = 10
        self.dmg = 3
        self.name = ""
        self.spaceship = ""
        self.race = ""
        self.ship = 10

        self.marksmanship = 8
        self.knowHow = 8
        self.chutzpah = 8
        self.luck = 8
        self.brawn = 8

    def equipment(self):
        StarBucks = 10
        OmniTool = True
        QuantumSixShooter = True
        RangerSpaceSuit = True 

class Cow:
    def __init__(self):
        self.hp = 15

class Enemy:
    pass


def youDied1():
    print("Nobody ever said the life of a space cowboy was an easy one")
    tryAgain = print(input("Would you like to try again? Yes or no?").lower())

    if tryAgain == "yes":
        game()
    else:
        print("End of demo. Thank you for playing! The game is still in development and will take time until completion. Until then, stay legen-dairy, space cowboy!")

def youDied2():
    print("You've yee'd your last haw")
    tryAgain = print(input("Would you like to try again? Yes or no?").lower())

    if tryAgain == "yes":
        game()
    else:
        print("End of demo. Thank you for playing! The game is still in development and will take time until completion. Until then, stay legen-dairy, space cowboy!")

def youDied3():
    print("See you, space cowboy")
    tryAgain = print(input("Would you like to try again? Yes or no?").lower())

    if tryAgain == "yes":
        game()
    else:
        print("End of demo. Thank you for playing! The game is still in development and will take time until completion. Until then, stay legen-dairy, space cowboy!")


def howDoDie():
    if random.randint(1,3) == 1:
        youDied1()
    if random.randint(1,3) == 2:
        youDied2()
    if random.randint(1,3) == 3:
        youDied3()

def helpFunc():
    print("Your available moves are:")
    print("LOOK")
    print("EXAMINE")
    print("INVENTORY")
    print("SEARCH")
    print("TAKE")
    print("OPEN")
    print("CLOSE")
    print("ASK")
    print("TELL")
    print("SAY")
    print("GIVE")
    print("WAIT")
    print("DRAW")
    print("SHOOT")
    print("HIT")
    print("THROW")
    print("HIDE")
    print("RUN")
    print("MOVE or GO")
    print("WRANGLE")
    print("RIDE")
    print("USE")

player = Player()

def undo():
    pass

def game():
    print("")
    print("")
    print("The Milky Way Galaxy is aptly named for its abundance of megalo-cosmic space cows, and in the year 27,399 AEI (After Earth Imploded), the nuclear milk of megalo-cosmic space cows is a heavily coveted resource. Not only is it an essential component in fuel for interstellar travel, it is also responsible for creating the greatest tasting cakes in the spacetime continuum.")
    print("")
    print("Naturally, for such a valuable commodity, there must be workers that manage the production and protection of the precious cosmic dairy. This is where you come in: you are a space cowboy (the term cowboy is gender-neutral in the 28th millennium) drifting your silver mustang through the open range of the universe, and boldly transporting your herd of cosmic cattle between solar systems. ")
    print("")
    print("You’ve picked up a new herd of space cows in orbit around the planet Ploxicon-9. As you finalize the contract, the rancher promises you 200 Star-Bucks if you can deliver the herd to the planet New New Jersey in an adjacent star system. It is imperative that the cows reach their destination within three standard space-days so that the space cows can be milked in time for the Great Galataki Bake-Off. You gather your supplies and head back to the space station.")
    print("")



    print("             /( ,,,,, )\"")
    print("            _\,;;;;;;;,/_")
    print('         .-""; ;;;;;;;;; ;""-.')
    print("         '.__/`_ / \ _`\__.'")
    print("            | (')| |(') |")
    print("            | .--' '--. |")
    print("            |/ o     o \|")
    print("            |           |")
    print('           / \ _..=.._ / \'') #fix
    print("          /:. '._____.'   \"") #fix
    print("          ;::'    / \     .;")
    print("          |     _|_ _|_  ::|")
    print("        .-|     '==o=='   '|-.")
    print("       /  |  . /       \   |  \"")
    print("      |  | ::|         |   | .|")
    print("      |  (  ')         (.  )::|")
    print("      |: |   |; U U U ;|:: | `|")
    print("      |' |   | \ U U / |'  |  |")


    intro = False
    while intro == False:
        print("\nThe space station is grimy and smells of corroded steel. Rust stains the aging metal walls, and the chatter of alien languages reverberates through the halls. Periodically, the ground shakes as large transport ships take off into the sky. You get in the back of a line of aliens, anxious to catch their flights off-world. The line moves slowly; at the front it appears that the registrar has gotten into an argument with an irritable alien.")
        print("\nWhat would you like to do? Enter a command and a noun. If you need help, type 'help'")
        firstMove = input().lower()

        if firstMove == "look alien":
            print("\nThe tripedal creature has slimy green skin and a long eyestalk protruding from the top of what you assume is a head. It’s spattering at the robotic desk-worker in an unknown language, likely because of a missed flight.")
            intro == True
            break
        elif firstMove == "look registrar":
            print("\nThe registrar at the check-in counter is an outdated protocol robot.")
            intro == True
            break
        elif firstMove == "shoot alien":
            print("\nYou blast a searing hole with your laser pistol through the shouting three-legged alien. It’s single eyestalk turns towards you in surprise, before slumping to the ground. The rest of the people in the line scream and scatter in surprise. You step carefully over the dead body to the check-in counter.")
            intro == True
            break
        elif firstMove == "shoot registrar":
            print("\nYour laser blast ricochets off of the robot’s surprisingly reflective armor. You duck as the incoming laser flies back at you, after which you hear a large crash. “MY LEG!” a voice cries out.")
            intro == True
            break
        elif firstMove == "wait":
            print("\nEventually the line begins to move again, and you arrive in front of the check-in counter.")
            intro == True
            break
        elif firstMove == "look north":
            print("\nTo the north lies the rest of the spaceport. Long corridors lead to private docks as well as loading bays for larger company-owned vessels. To go that way, you’ll need to check in at the front desk first.")
            intro == True
            break
        elif firstMove == "look south":
            print("\nThe entrance to the spaceport is southward. Beyond the glass windows you see heavy mists resting over long stretches of mud-flats and rice fields. Why would anyone build a spaceport here? you wonder.")
            intro == True
            break
        elif firstMove == "help":
            helpFunc()





    print("\nThe check-in robot greets you: *Howdy, biological lifeform! Welcome to Ploxicon-9’s #1 and only spaceport. Before preparing your flight, we must assess your space-travel readiness by asking a few questions.*")

    print("What is your name?")
    player.name = input().lower()

    print("Your marksmanship is", player.marksmanship)
    print("Your know-how is", player.knowHow)
    print("Your chutzpah is",player.chutzpah)
    print("Your luck is", player.luck)
    print("Your brawn is", player.brawn)



    def s():
        speciesChoice = False

        while speciesChoice == False:
            print("\nWhat alien species to you belong to?\n")
            print("Human")
            print("Khovorion")
            print("Xorq")
            print("Galataki")
            print("Bumblerwum")
            species = input().lower()
            if species == "human":
                print("\nHumans are the most widely detested species in the galaxy due to their overwhelming greed and blatant disregard for planetary resources. They tend to be 5 to 6 feet tall, grow superfluous hair on the top of their heads, and have a range of debilitating features including poor eyesight, fragile skin, and vulnerability to many diseases. It is a wonder that they have survived this long. ")
                print("+2 Luck, +1 Chutzpah")
                areHuman = print(input("Are you human? Yes or no? ").lower())
                if areHuman == "yes":
                    speciesChoice = True
                    break
            elif species == "khovorion":
                print("\nKhovorions are tall, intimidating insectoid creatures. They have six appendages, typically walking on four legs and using the upper two as arms. They have chitinous exoskeletons, beady eyes, and long tails with pointed stingers.")
                print("+2 Marksmanship, +1 Brawn")
                areKhovorion = print(input("Are you Khovorion? Yes or no? ").lower())
                if areKhovorion == "yes":
                    speciesChoice = True
                    break
            elif species == "xorq":
                print("\nXorq skin is perfectly camouflaged to blend into rocky environments, such as their mountainous home planet. They average 3 to 4 feet tall, and have rough, hard skin that feels like stone. Their rotund bodies can curl into a boulder-like shape as a defense mechanism and roll into enemies.")
                print("+2 Brawn, +1 Know-How")
                areXorq = print(input("Are you a Xorq? Yes or no? ").lower())
                if areXorq == "yes":
                    speciesChoice = True
                    break
            elif species == "galataki":
                print("\nGalataki are semi-aquatic cephalopods widely renowned for their academic prowess. They have large brains and 12 tentacles which can be interchangeably used as arms and legs. Their home planet boasts some of the most prestigious universities in the galaxy, but they are usually found underwater.")
                print("+2 Know-How, +1 Marksmanship")
                areGalataki = print(input("Are you a Galataki? Yes or no? ").lower())
                if areGalataki == "yes":
                    speciesChoice = True
                    break
            elif species == "bumblerwum":
                print("\nBumblerwum are famous for being one of the most adorable species in the known universe. They typically stand only 2 to 3 feet tall, and appear as colorful balls of fluffy hair. When threatened, though, they can harden their fluffy rainbow-colored hair into sharp spikes which can shoot out at enemies.")
                print("+2 Chutzpah, +1 Know-How")
                areBumblerwum = print(input("Are you a bumblerwum? Yes or no? ").lower())
                if areBumblerwum == "yes":
                    speciesChoice = True
                    break
                    

        if species == "human":
            player.luck += 2
            player.chutzpah += 1
        elif species == "khovorion":
            player.marksmanship += 2
            #input brawn
        elif species == "xorq":
            #input brawn
            player.knowHow += 1
        elif species == "galataki":
            player.knowHow += 2
            player.marksmanship += 1
        elif species == "bumblerwum":
            player.chutzpah += 2
            player.knowHow += 1


    s()
    

    #thebeginning
    print("Do you have a spaceship already docked at the station?")
    dock = input().lower()
    if dock == "y" or dock == "yes":
        player.spaceship = input("\n*Excellent! What is the name of your spaceship?*")
        print("*Ah, yes. We have your ship,", player.spaceship, ",docked in port 6B. You may head there now.*")
    elif dock == "n" or dock == "no":
        print("*Very well. Then you will have to buy a ticket for one of our off-world transports. The standard price of an interstellar transport is 100 Star-Bucks. [...] What do you mean you don’t have that kind of money?* [The End]")
        howDoDie()


    #enter ship
    enterShip = False
    while enterShip == False:
        print("\nHeading down the grimy spaceport hallways, you come to an elevator with 6B painted on the doors in blocky green characters. The lift takes you up to a large room empty save for a number of crates, gas pipes, and your prize ship,")
        pt1 = input().lower()
        if pt1 == "look ship":
            print("\nIt’s a small fighter vessel, with only enough room for essential cow-wrangling equipment and a small living space. Paint is peeling off the sides, revealing rusted metal armor.")
        elif pt1 == "enter ship":
            print("\nAfter getting yourself seated in the cockpit, you power up the engines with a heavy revving, and blast off into the stratosphere.")
            enterShip == True

    #asteroid
    asteroidEncounter = False
    while asteroidEncounter == False:
        print("\nOnce in orbit, you find your herd of space-cows, lazily drifting in zero-gravity. As you count them, you realize that there are only 14 cows, when there should be 15. Checking your scanners, you see a small blip moving dangerously close to an asteroid field.")
        pt2 = input().lower()
        if pt2 == "look space-cows" or pt2 == "look cows" or pt2 == "look herd":
            print("\nSpace-cows are massive creatures more akin to horned whales than cows. They have no hind legs, instead propelling themselves through the void of space with heavy tails. This herd is made up of 10 fully-grown adult calves and 4 calves. One of the mothers appears distressed, as she has lost her calf.")
        elif pt2 == "look asteroid field" or pt2 == "look asteroid":
            print("\nThis asteroid field makes up the ring that surrounds Ploxicon-9. While beautiful from afar, it’s filled with rocks ranging from pebbles to boulders the size of a house.")
        elif pt2 == "go asteroid field" or pt2 == "move asteroid field" or pt2 == "go asteroid" or pt2 == "move asteroid":
            print("\nFlying in the direction of the blip on your scanner, you see a young space-cow calf entering the chaotic fray of rocks.")
            asteroidEncounter == True
            break
        elif pt2 == "go calf" or pt2 == "move calf" or pt2 == "follow calf":
            print("\nAs you tail behind the calf, you deftly navigate between huge chunks of flying space-rocks. You lose sight of the calf only for a moment while weaving through the fray. Suddenly, a massive asteroid looms towards you at an unrelenting speed. Do you:")
            print("Dodge asteroid [know-how]")
            print("Shoot asteroid [marksmanship]")
            goCalf = input().lower()
            if goCalf == "dodge asteroid":
                dodgeAsteroid = random.randint(1,100)
                totalKnowHow = 40 + (player.knowHow*3)
                if dodgeAsteroid <= totalKnowHow:
                    print("You nimbly pilot your ship down below the tumbling asteroid before being hit.")
                else:
                    print("You swerve your ship around the side, but you aren’t quick enough, and the wing of your ship catches on the asteroid. Your ship takes 3 damage.")
            elif goCalf == "shoot asteroid":
                shootAsteroid = random.randint(1,100)
                totalMarksmanship = 40 + (player.marksmanship*3)
                if shootAsteroid <= totalMarksmanship:
                    print("Your missile obliterates the asteroid into tiny chunks which bounce harmlessly of the plated exterior of your vessel.")
                else:
                    print("The blast is enough to mostly destroy the asteroid so that your ship isn’t crushed, but large chunks of debris damage the outer plating of your vessel. Your ship takes 3 damage.")
            asteroidEncounter == True

    #calf
    calfEncounter = False
    while calfEncounter == False:
        print("\nYou spot the calf through the jumble of asteroid pieces heading towards a clearing of relative safety. Putting on your oxygen-helmet and stepping out onto the loading platform, you consider your options. You could use your lasso to wrangle the calf back to you, or you could try to coerce the frightened beast to follow your ship.")
        pt3 = input().lower()
        if pt3 == "look calf":
            print("\nThe poor baby space-cow seems frightened of the chaotic asteroid field. A wrong move could cause it to run away again, or even make it lash out.")
        elif pt3 == "wrangle calf":
            wrangleCalf = random.randint(1,100)
            totalBrawn = 40 + (player.brawn*3)
            if wrangleCalf <= totalBrawn:
                print("You successfully hook the lasso around the calf before it can dash away and hold tight against the shell of your ship. You secure the lasso to the side before reentering the cockpit and activating enough thrust to gently pull the calf outside of the asteroid field.")
            else:
                print("You manage to catch the calf with your lasso, but it panics, pulling you out of your ship with it! You only have moments to react before it drags you out into the entropic fray of rocks.")
            calfEncounter == True
            break
        elif pt3 == "coerce calf":
            coerce = random.randint(1,100)
            totalChutzpah = 40 + (player.chutzpah*3)
            if coerce <= totalChutzpah:
                print("Careful not to frighten the thing, you coo to the calf with open arms to encourage it to approach you. Once within your reach, you gently secure it to the outside of your ship with cables and fly out of the asteroid cluster.")
            else:
                print("The calf does not react to your encouragement. After about a minute of trying to get it to come closer, a rogue asteroid crashes into your ship, scaring the calf away and knocking you out into space.")
            calfEncounter == True
            break
                
    print("You could use your lasso to climb onto the cow and ride it back in the direction of the ship, or you could activate your omni-tool to remotely pilot the ship back to you and pursue the calf.")

    pt4 = input().lower()
    if pt4 == "ride calf":
        rideCalf = random.randint(1,100)
        totalBrawn = 40 + (player.brawn * 3)
        if rideCalf <= totalBrawn:
            print("Using all your might to pull yourself up the lasso as the calf wildly swims through waves of boulders, you eventually clamber onto its back. From there you grab hold of its newly formed horns and steer it back towards your ship and out of the chaos of the asteroid field.")
        else:
            print("You catch the lasso on one of the calf’s small horns, but as it thrashes about, it is impossible to climb back on, and the end of the lasso eventually snaps. You manage to tie a new one long enough to reach your ship and climb inside, but you lose sight of the calf.")

    elif pt4 == "use omnitool" or pt4 == "use omni-tool":
        omnitool = random.randint(1,100)
        totalKnowHow = 40 + (player.knowHow * 3)
        if omnitool <= totalKnowHow:
            print("Floating through space, you pull out your omni-tool and load a remote steering application. You navigate your ship close enough to pull yourself in through the shield doors. Once inside, you quickly recover the escaped calf and guide it outside the asteroid field.")
        else:
            print("Navigating your ship through the entropic fray of asteroids takes time, and by the time you finally enter your ship, the calf is no longer visible.")

    print("End of demo. Thank you for playing! The game is still in development and will take time until completion. Until then, stay legen-dairy, space cowboy!")

game()