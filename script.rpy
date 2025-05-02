# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("test-chan")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default. 

    scene bg room

    # This shows a character sprite. A placeholder is used if no file is found.

    show testchan

    # These display lines of dialogue.

    e "python!"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
