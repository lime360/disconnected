﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Player", color="#0088A3")

define funnydude69420 = Character("funnydude69420", color="#A30200")

define page = Character("https://reconnect.net/instructions.html", color="#FFFFFF")

define questhelper = Character("Quest Helper", color="#FFFFFF")

define worker = Character("Web Cafe Worker", color="#cf1180")

define seller = Character("Some random guy who sells stuff for free", color="#0151b9")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg placeholder
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    player "I went home after a long school day"

    player "I turned on my laptop, opened up the browser so i can play Flash games, but the browser says..."

    player "PAGE NOT FOUND. PLEASE REFRESH THE PAGE OR TRY TROUBLESHOOTNG THE NETWORK."

    player "That's strange, I connected it to the cable yesterday and it worked normally, maybe i should reconnect it?"

    player "I tried to reconnect 5 times, i refresed the page 30 times, and i even restarted it! Nothing happened..."

    player "Suddenly, i hear an AIM Message Sound, someone under the name funnydude69420 sent me a message..."

    funnydude69420 "Hey! I see that your internet is down."

    player "Wait, how did you know? And how did AIM work even though it requires internet"

    funnydude69420 "That's a secret that i will tell you later during our quest..."

    player "Quest?"

    funnydude69420 "Yes, here is the link: https://reconnect.net"

    player "Thank you."

    jump website

label website:

    player "I opened this link and..."

    player "It worked!"

    player "Now i have to navigate through options"

    player "Where should i click?"

    menu index_html:
        "Read the instructions":
            jump instructions

        "Start the quest":
            jump quest

label instructions:

    page "INSTRUCTIONS"

    page "THESE INSTRUCTIONS ARE MADE FOR PEOPLE WHO ARE PLAYING THIS FOR THE FIRST TIME"

    page "THIS QUEST IS A VISUAL NOVEL THAT TAKES PLACE IN 2005"

    page "THE MAIN GOAL IS TO FIND THE DOWNLOADABLE VIRTUAL DISC CONTAINING A SPECIAL DRIVER"

    page "THIS GAME IS ALSO BASED ON IRL EVENTS THAT HAPPENED TO GAME CREATOR (lime360)"

    page "ENJOY THIS QUEST!"

    page "P.S. SORRY FOR BREAKING THE FOURTH WALL"

    page "REDIRECTING TO INDEX.HTML..."

    jump index_html

label quest:

    questhelper "Welcome to RECONNECTing the interNET (reconnect.net) Quest!"

    questhelper "Your objective is to find a downloadable virtual disk with network drivers update"

    jump cafe

label cafe:

    questhelper "You are in a Web Cafe, wanting something to eat or drink..."

    worker "Hi, welcome to the Web Cafe, what can i get for you?"

    player "I want..."

    menu order:
        "Water":
            player "Water."
        "Cookies and Tea":
            player "My favourite Mint Cookies and Black Tea."
        "This option is for McDonalds Workers":
            jump secret

    worker "OK! Here you go!"

    player "Wait, do i have to pay for this?"

    worker "No, everything is free!"

    player "Okay, thanks!"

    worker "Bye!"

    jump letsgooo

label secret:

    player "1 Big Mac, Large french fries, medium Coke and 9 Chicken Nuggets"

    worker "We're sorry, but we don't have McDonald's in this quest..."

    player "Okay, i'll pick something else..."

    jump order
        
label letsgooo:

    player "I went outside to take a walk."

    funnydude69420 "Hey! I remember you!"

    player "No way..."

    player "It's that guy that messages me in AIM about this quest."

    player "Hi."

    funnydude69420 "Hello."

    funnydude69420 "Thank you for joining this quest, wanna hear more about it?"

    player "Sure!"

    funnydude69420 "Well, i made this quest for people to get back their internet access."

    player "You made it? Really?"

    funnydude69420 "Yeah! And citizens of this world calls me a president!"

    player "That's cool!"

    funnydude69420 "So, as i was saying, you need to get back your internet..."

    player "Yes! I need it so i can play Flash games."

    funnydude69420 "Well, let me show you how to find the key for that."

    funnydude69420 "*typing helper driver*"

    questhelper "As i said earlier. The key is a virtual disk with a driver."

    questhelper "Driver is located in a cave, which is a maze that you need to go through. Luckily you can save data and continue from the place you stuck"

    questhelper "Good luck!"

    player "Alright, lets do this!"

    funnydude69420 "One more thing..."

    player "Which?"

    funnydude69420 "It's easy to get stuck in this cave. Luckily, you have a store where you can get items for an easier expirience!"

    player "Okay..."

    player "Then I went into the shop."

    seller "Hi, what would you like to bring here on this adventure?"

    player "Well..."

    menu what2buy:
        "A map":
                player "I need a map."
        "Nothing":
                jump yousure
    
    seller "Thank you and enjoy your adventures at this cave!"

    jump cave

label yousure:

    seller "Really? Exploring this cave without a special item is not that easy!"

    player "Whatever, I'll just go..."

    seller "Okay then. Bye!"

    jump caveNoLights

label cave:

    scene bg cavemap
    with fade

    questhelper "The map is shown on the screen for an easy play"

    return

label caveNoLights:

    player "Going there with no map was a mistake, i can't find a driver because there were no lights"

    player "I'm stuck here..."

    ".:. Game Over"

    menu retry:
        "Get a map":
            jump what2buy
        "Return to the main menu":
            return
