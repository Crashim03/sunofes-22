# The script of the game goes in this file.

define m = Character("{b}[name]{b}", color="#ffffff")
define monster = Character("{b}???{b}", color="#ffffff")

# The game starts here.

label start:

    show bg shopping

    python:

        name = renpy.input("What's your name?")

        name = name.strip()
 
    show enemy 1

    monster "..."

    m "Texto."

    show enemy 2

    m "{i}gasp{i}"

    return
