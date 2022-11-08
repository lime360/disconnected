# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Player", color="#0088A3")

define funnydude69420 = Character("funnydude69420", color="#A30200")

define page = Character("https://reconnect.net/instructions.html", color="#FFFFFF")

define questhelper = Character("Quest Helper", color="#FFFFFF")

define worker = Character("Web Cafe Worker", color="#cf1180")


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

    questhelper "You are in a Web Cafe, wanting something to eat or drink..."

    worker "Hi, welcome to the Web Cafe, what can i get for you?"

    player "I want..."

    return
