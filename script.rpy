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
$ force_feed = 0




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
    ts "Well, Ayaka-chan went to class with Sensei. I'm hiding from the staff who prey on kids who skip classes."
    ts "I bet Ayaka-chan is bored as hell, listening to Sensei go on about the Americans fighting each other."
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
        it "I don't want to know what Tsukiko-chan saw."
        ts "You really don't."
        ay "Anyway, Itsuki-kun, do you want to join us in the Libary for studying after school?"
        it "I won't have time at home, so I guess I should."
        ts "Thats our Itsuki-kun!"
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
        scene classroom sunset
        "2:30 PM - Mathematics - School"
        show tsukiko at left with dissolve
        ts "Ugh, I hate math..."
        ts "When in later life am I going to need to know how to find a volume of a cylinder?"
        ts "I mean, I guess if I want to be a plumber, but I don't want to be a plumber!"
        ts "I want to be cafe owner!"
        ts "I mean, I guess I could be a cafe owner and a plumber, but that would be a bit weird."
        ts "Welcome to Tsukiko's Cafe! Can I get you started on coffee or a toilet flush?"
        ts "What would I even serve in that cafe? Omlette Rice and Drain Cleaner?"
        ts "Sushi and a Plunger?"
        show itsuki at right with moveinright
        it "What are you waffling on about?"
        ts "Huh!"
        ts "Oh, nothing..."
        it "So, whats a Omlette Rice and Drain Cleaner special today?"
        ts "Hey! Don't insult my bored brain!"
        it "Anyway, Sensei is going to start shouting at you if you don't pay attention."
        ts "What are we doing again?"
        it "Calulating volumes. Now, pay attention!"
        ts "But, Itsuki-senpai... When am I actually gonna need this in later life?"
        it "Don't call me that!"
        ts "But senpai-"
        it "I will throw you out the the nearest window if you call me that again!"
        ts "Sorry, Itsuki-kun..."
        it "Just pay attention!"
        ts "Fine..."
    label libary1:
        scene libary with dissolve
        "3:30 PM - Libary - School"
        show tsukiko at left with dissolve
        show ayaka at center with dissolve
        ts "Well, here we are."
        ay "Itsuki-kun is late like always."
        ts "Does that mean you are going to force feed him his lunch tomorrow?"
        ay "Of course!"
        ts "You had better wear trousers!"
        ay "Don't even go there!" with hpunch
        ts "Alright, I get it."
        show itsuki at right with moveinright
        ts "Oh, look who finally decided to show up!"
        it "Hey, I needed a piss!"
        ts "You should look at Bladder Expansion Surgery!"
        it "I don't want doctors poking around that area!"
        ts "Not that there is anything to poke around anyway!"
        it "Don't you even-"
        ay "Can you guys stop talking about that?"
        ay "It's really weird, and this is a public space!"
        ay "If you want to talk about that, go to the basement or something."
        ay "Itsuki-kun..."
        it "Yes?"
        ay "How much water do you drink a day?"
        it "About 2-3 litres, I guess."
        ts "That's a lot of water"
        ts "I drink one of those 500ml bottles a day."
        it "That's not enough!"
        ts "But, there is a fine line between drinking enough and drinking too much!"
        ay "Can you guys just shut up and study!"
        ts "Sorry, Ayaka-chan..."
        it "She started it!"
        ay "I don't care who started it! Just shut up and study!" with vpunch
        it "I get the point."
        ay "Also, I'm force feeding you your lunch tomorrow."
        it "W-why?"
        ay "Because you were late!"
        "And so, the three of them studied until sundown, when Ayaka-chan realized the time."
        ay "Oh no! It's 5:30! The school closes at 6! We had better get going!"
        hide ayaka with moveoutright
        hide tsukiko with moveoutleft
        hide itsuki with moveoutright
    label tsukikoroom1:
        scene apartment night
        "6:00 PM - Tsukiko's Room - Tsukiko's House"
        show tsukiko at center with dissolve
        ts "Well, that was a day..."
        ts "And there is still 4 more days of this week left..."
        ts "Tomorrow will be funny, though."
        ts "There is no way that Ayaka-chan will let him off the hook. She will feed him."
        ts "And since we can use phones at break, I am so gonna record it!"
        # phone buzz sound here when audio ready.
        ts "Oh, it's Itsuki-kun."
        "Can you please convince Ayaka-chan to not feed me? Some guy will record it and post it on Z or something. I can't afford to become the class clown!"
        ts "Huh."
        "But you already are the class clown!"
        ts "heh."
        # phone buzz sound here when audio ready.
        "DON'T EVEN GO THERE YOU %#@#@!"
        ts "Wow, someone is feeling feisty today!"
        ts "But, should I convice Ayaka-chan to not feed him?"
        ts "Should I message her and tell her not to do it?"
        menu:
            "I wanna see him get fed!":
                $ force_feed = 1
                ts "I so can't miss out on this!"
                
                jump tsukikoroom2
            "I should tell her not to do it." :
                $ force_feed = 0 # make sure this is set to 0 incase it gets tripped somehow
                ts "I guess I should tell her not to do it."
                ts "After all, I don't want to see him become an outcast."
                "Hey, Ayaka-chan! Please don't feed Itsuki-kun tomorrow!"
                "He will become a social outcast if you do!"

                jump tsukikoroom2
    label tsukikoroom2:
        ts "Well I had better go make instant ramen for dinner."
        ts "Most kids who go to study end up eating microwave meals or such, since they miss dinner."
        ts "Hopefully, Ayaka-chan doesn't lose track of time again tomorrow. Then I can have real food!"
        ts "To the kitchen!"
    label kitchen1:
        scene kitchen 1
        show tsukiko at center with dissolve
        ts "Huh, I wonder if we have run out..."
        ts "I hope not, because I can't be bothered to go to the store."
        ts "I could order something, but I could also wait until tomorrow."
        ts "Ayaka-chan would also get mad at me if I didn't eat, though."
        ts "Nah, I will just eat something tomorrow."
        ts "I'm sure it will be fine."
    label day2start:
        scene classroom board morning
        "Tuesday - 10AM - Science - School"
        show tsukiko at left with dissolve
        ts "Ok, it's got interesting now!"
        


                       






        






    
    # This ends the game.

    return
