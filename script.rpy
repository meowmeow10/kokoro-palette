# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define tc = Character("Test-chan")
define ts = Character("Tsukiko")
define ay = Character("Ayaka")
define sen = Character("Sensei")
define it = Character ("Itsuki")
# Declare variables used. $ indicates Ren'py will treat it like Python 3.11.
$ skipped_class = 0
$ basement_skip = 0




# The game starts here.

label start:
    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene classroom morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Monday - 10 AM - English - School."

    show tsukiko at left
    with fade

    # These display lines of dialogue.
    

    ts "School is so boring..."

    ts "Maybe I should bunk next class..."

    show ayaka at right
    with dissolve

    ay "You sure that's a good idea?"
    ay "You know how Sensei gets with bunkers..."
    ts "I know, but detention is better than hearing Sensei go on about the American revolution for 2 hours."
    ay "Maybe then, but I still don't recommend it."
    ts "What should I do?"

    menu:
        "Skip class":
            jump skip
        "Stay in class":
            jump stay

    label skip: 
        $ skipped_class = 1 # get detention, idiot!
    ts "I'm gonna skip class."
    ay "You're really sure about that?"
    ts "Yeah, again, a half hour detention is better than 2 hours of American revolution."
    ay "I guess, but I'm not joining you."
    # Place bell ring here when audio ready
    ts "Oh, thats the bell. I guess it's recess."
    hide ayaka
    show ayaka at right # Change image here to Ayaka Angry when Astro has finished art.
    ay "You have been here for a year already! How do you guess it's recess??!" with vpunch
# It should jump to scene skipclass from here. If not, ping @meowcat.
    jump skipclass
    label stay:
    $ skipped_class = 0 # set to 0 incase it gets tripped somehow
    ts "I think it's better to stay then get scolded by my Parents for getting a detention."
    ay "Me too."
    ts "And I avoid getting scolded by my Parents."
    ay "They are brutal..."
    # Place bell ring here when audio ready
    ts "Oh, thats the bell. I guess it's recess."
    hide ayaka
    show ayaka at right # Change image to Ayaka Angry when Astro has finished art.
    ay "You have been here for a year already! How do you guess it's recess??!" with vpunch
# It should jump to scene boringhist from here. If not, ping @meowcat.
    jump boringhist
    
    hide classroom morning
    hide tsukiko
    hide ayaka
    label skipclass:
    scene hallway 1 with wipeleft
    show tsukiko with dissolve
    ts "Well, Ayaka went to class with Sensei. I'm hiding from the staff who prey on kids who skip classes."
    ts "I bet Ayaka is bored as hell, listening to Sensei go on about the Americans fighting each other."
    ts "Well, as Midterms are coming up, maybe I could go to the Libary and study..."
    ts "But I might get caught, and get a Detention..."
    ts "Well, there is only half an hour left of class. Maybe I could get away with it!"
    ts "I could also hide in the basement..."
    ts "What should I do?"
    menu:
        "Hide in Basement":
            jump basement
        "Stay upstairs":
            jump lunch
    
    label boringhist:
        hide classroom morning
        hide tsukiko
        hide ayaka
        scene classroom board morning
        "12 PM - World History - School"
        show tsukiko at right # Change image to Tsukiko Bored when Astro has finished art.
        ts "I'm so bored..."
        ts "Maybe I shouda' skipped..."
        show ayaka at left 
        ay "Shh... Do you reckon I could start playing Square Blaster on my phone to pass the time?"
        ts "but what if you get caught?"
        ay "Sensei will take my phone away... and she will find the Yaoi I have as my wallpaper..."
        ts "YOU HAVE YAOI AS YOUR WALLPAPER!?!?" with hpunch
        ay "SHUT UP! If Sensei hears us shouting, we will so get detention!"
        sen "Who is shouting? If you don't listen up, you will fail your Midterms!"
        ay "I forgot about midterms..."
        ts "Just cram at the last minute, like me!"
        hide ayaka
        show ayaka # Change image to Ayaka Angry when Astro has finished art.
        ay "That's not good work ethic!" with hpunch
        ts "Well, I have never failed before!"
        ay "That's true, but it's still not good!"
        ts "Well if it ain't broke, don't fix it!"
        ay "THAT DOES NOT APPLY HERE!" with vpunch
        sen "If I hear anyone shout again, it's detention for ALL of you!"
        ts "Yeah Ayaka, you better shut up!"
        ay "Get out!"
   
        jump lunch

        label basement:
        ts "I guess I'm going to the basement then."
        $ basement_skip = 1
        jump lunch

        # Fixing the syntax issues in the lunch label

label lunch:
    scene outside morning
    "1:30 PM - Lunch - School"
    show tsukiko at right with dissolve
    ts "Huh, I wonder where the others are..."
    show ayaka at left with moveinleft

    # Explicitly declare basement_skip as a global variable
    default basement_skip = 0  # Ensure it is initialized if not already set

    if basement_skip:  # Check the value of basement_skip
        ay "Why do you smell musty?"
        ts "I was in the basement..."
        jump lunch2
    else:
        ay "You smell OK, for once."
        ts "What do you mean by that?" with vpunch
        jump lunch2
    label lunch2:
        ts "Anyway..."
        ts "I was thinking of going to the Libary to study for Midterms at the end of the day."
        ay "Sounds like a good shout."
        show itsuki at center with dissolve
        it "Sorry I'm late!"
        ts "Every day, huh."
        ay "Why are you always late? You litterally have a watch on!"
        it "Uhh..."
        it "The bathroom line was long..."
        ay "Just go after eating... The line will be gone by then."
        ts "Imagine using the school bathrooms and not holdng it like me!"
        it "It's not my fault I have a small bladder!" with vpunch
        ts "more like a small rectum!"
        it "Shut up! Says the kid who skips class!"
        ts "You want me to show you what damage I can do!?"
        it "No, not really."
        ts "Good, because I don't think I could punch your face without your glasses getting embedded in your skull."
        ay "That's a bit dark, don't you think?"
        it "Tell that to the kid who spends about 7 hours a week in the basement."
        ts "Says the kid with 6+ prescription glasses!"
        it "I can't help it!"
        ay "Bro could see mainland china with those eyes!"
        it "Not you too!" with hpunch
        ay "Ok, but if Tsukiko won't shut her mouth, I'm going to force feed her the lunch she has!"
        ts "Not after last time..."
        it "What happened last time?"
        ay "Well, I did it-"
        ts "Scarred me for life, really-"
        ay "And uhh... Well, my skirt-"
        it "I get it, I get it."
        it "I don't want to know what Tsukiko saw." (multiple = 2)
        ts "You really don't." (multiple = 2)
        ay "Anyway, Itsuki, do you want to join us in the Libary for studying after school?"
        it "I won't have time at home, so I guess I should."
        ts "Thats our Itsuki!"
        ay "If you are late, I am going to force feed you YOUR lunch tomorrow" with vpunch
        it "I won't be late!"
        ts "Famous last words!"
        it "Hey! Shut up!"
        # School bell plays here when audio ready.
        ts "Oh, thats the bell. I guess we have to go back to class."
        it "If I catch you skipping again, I will tell Sensei!"
        ts "You wouldn't be able to walk again if you did!"
        it "Yeah maybe not..."
        ay "Guys! Move it, or we will all be late!"

        label class2:
        




    # This ends the game.
    return




    
    # This ends the game.

    return
