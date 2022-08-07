# The script of the game goes in this file.

define n = Character("{b}Newspaper Boy{/b}", color="#ffffff")
define uk = Character("{b}???{/b}", color="#ffffff")
define p = Character("{b}[name]{/b}", color="#ffffff")
define m = Character("{b}Matthew{/b}", color="#ffffff")

# The game starts here.
label start:

    stop sound
    stop music fadeout 2.0

label chapter_I:

    # A maneira como se pergunta o nome do jogo tem que ser melhorada
    python:

        name = renpy.input("What's your name?")

        name = name.strip()

    # Int. Cafe. Daytime.
 
    p "Hey Matthew!{w=0.5} I'm glad you called.{w=0.5} Is everything okay?"

    m "Yes,{w=0.2} it's all good!{w=0.5} I actually called because of the chip you're looking for your arcade."

    p "Oh..."
    
    p "I hope you have some good news for me!"

    m "Well.{w=0.2}.{w=0.2}.{w=0.2} It's not going great to be honest."

    m "I can't find it on any site or in second-hand shops."

    m "I've also taken some time to search into the arcade model and it's not been produced since 1971,{w=0.2} which makes this a lot harder than it already is."

    p "What about Greg?{w=0.5} Did he talked to you?"

    m "Greg couldn't also find anyone who owns an arcade like yours."

    p "Are there any replies to our ad?"

    m "No,{w=0.2} still none."

    p "Okay.{w=0.5} No worries!{w=0.5} I know we will find a way to get that chip and repair my arcade."

    p "So,{w=0.2} what's our next step?"

    m "I'm afraid there's no next step."

    p "How so?"

    m "I've been looking everywhere.{w=0.5} I don't know what more to do."

    p "Are you sure?"

    p "Did you try going into that arcade-themed cafe in the mall?{w=0.5} I heard they have some pretty rare arcades."

    m "Yes,{w=0.2} I did!{w=0.5} I tried various malls!{w=0.5} A lot of malls!"

    p "Okay okay,{w=0.2} I believe you!"

    p "I'm going to wait one more week to see if anyone answers to the ad."

    p "If not.{w=0.2}.{w=0.2}.{w=0.2}  well,{w=0.2} I'll give up my arca-"

    m "Wait a second!"

    m "What if.{w=0.2}.{w=0.2}.{w=0.2} No,{w=0.2} that's not a good idea."

    p "What are you thinking about?"

    m "Remember Coppertale Mall?"

    p "Yes.{w=0.2}.{w=0.2}.{w=0.2}  What about it?"

    m "They had an arcade shop with an arcade like yours."

    p "Yeah,{w=0.2} I remember that!{w=0.5} Do you think.{w=0.2}.{w=0.2}.{w=0.2} the arcade might still be there?"

    m "I don't know..."

    m "The mall has been abandoned for over 15 years."

    p "I guess there's no harm in checking.{w=0.5} It's a 10-minute ride from my house."

    m "It's still private property.{w=0.2}.{w=0.2}.{w=0.2} but,{w=0.2} yes,{w=0.2} you could give it a try..."

    m "I would advise you to go at night to not get into any trouble."

    p "Yeah,{w=0.2} you're right.{w=0.5} It won't take long anyways."

    m "Okay,{w=0.2} then!"

    m "Call me afterwards.{w=0.5} I want to know if you got it."

    p "Sure do!"

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

label chapter_II:

    # Int. Coppertale Mal- Mall Entry. Night.

    p "Okay.{w=0.5} This is different than I recalled. How can I get to this arcade again?"

label chapter_II_choice:

    menu:

        "Go foward.":

            jump chapter_II_go_foward

        "Turn left.":

            jump chapter_II_turn_left

label chapter_II_go_foward:

    "You walk foward." 

    "In front of you is an old escalator that leads into an old food court.{w=0.5} To your left,{w=0.2} there's a dark hallway where you can see a shimmering light in the distance."

    menu:

        "Go up the escalator.":

            jump chapter_II_escalator

        "Turn to the dark hallway.":

            jump chapter_II_dark_hallway
    
label chapter_II_escalator:

    "The food court on the first floor is a ghost town.{w=0.5} Closed restaurants,{w=0.2} chairs spread around the plaza and spider webs filling every crack on the walls."

    "Above,{w=0.2} a broken skylight that once filled the whole room with light,{w=0.2} lets in the night breeze.{w=0.5} You look up to see a clear sky full of stars."

    "To your left,{w=0.2} there's a double door.{w=0.5} You open it and follow a long pathway into a large room.{w=0.5} It seems like you've come back to the main entrance."

    jump chapter_II_choice

label chapter_II_dark_hallway:

    "The hallway is longer than you thought,{w=0.2} with clothing shops on either side."

    "While passing near an old photo booth,{w=0.2} you step on a broken glass and the noise startles you."

    # Broken glass sound effect

    "You continue walking,{w=0.2} this time more carefully than before,{w=0.2} until you reach a dead end.{w=0.5} The shimmering light lits up the entrance of a pet shop. There's no way in."
    
    "You end up turning back to the main entrance."

    jump chapter_II_choice

label chapter_II_turn_left:

    "You turn left and see a merry-go-round further back.{w=0.5} A sign with a symbol points to the opposite direction."

    menu:

        "Go to the merry-go-round.":
        
            jump chapter_II_merry_go_round

        "Follow the sign":

            jump chapter_II_sign

label chapter_II_merry_go_round:

    "You walk towards the merry-go-round.{w=0.5} None of the horses are still attached to it. Strange."

    "You look past it and notice the passage is completely blocked by a couple of collapsed beams.{w=0.5} You go back to the main entrance."

    jump chapter_II_choice

label chapter_II_sign:

    "You follow the sign.{w=0.5} One of the stores to your right is lit with candles{w=0.5}. You get a little bit closer and hear to distinct {b}voices{/b} coming from inside."

    p "Shit..."

    p "I better find that chip and get the hell out of here as quickly as I can."

    "You turn back to see more stores lit up as the number of voices keep adding up.{w=0.5} A shiver runs up your spine.{w=0.5} You look to your cellphone and the battery is dead."
    
    "How can this be?{w=0.5} You charged it up right before you left the house."

    "You decide to walk back to the mall's entry without raising an eyebrow."

label chapter_III:

    p "What?"

    p "Is that newspaper stand actually open?!"

    p "This must be one of those underground trendy places that open during the night."

    p "If I stick around and blend in with the people, they won't ever notice I sneaked in."

    # Entra

    p "Let's see one of these!"

    # Clica no jornal

    p "August 3rd, 2022."

    # Front page appears

    p "What the hell?"

    uk "Hey, buddy!{w=0.5} Are you planning to buy that?"

    # Newspaper boy appears

    n "Are you?"

    p "Ah- ahm!"

    return
