# The script of the game goes in this file.

define m = Character("[name]", color="#41d941")
define monster = Character("???", color="#2b0606")

# The game starts here.

label start:

    show bg placeholder

    python:

        name = renpy.input("What's your name?")

        name = name.strip()
 
    show enemy 1

    monster "..."

    m "gasp"

    return
