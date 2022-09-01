screen relationships:
    bar value AnimatedValue(relationship, 6, 1.0):
        xalign 0.05 yalign 0.05
        xmaximum 290
        ymaximum 10
        right_bar "bar/empty.png"
        left_bar "bar/full.png"
        bar_invert False

# Characters
define s = Character("{b}Security Guard{/b}", color="#ffffff")
define n = Character("{b}Newspaper Boy{/b}", color="#ffffff")
define uk = Character("{b}???{/b}", color="#ffffff")
define p = Character("{b}[name]{/b}", color="#ffffff")
define m = Character("{b}Matthew{/b}", color="#ffffff")
define v1 = Character("{b}Voice 1{/b}", color="#ffffff")
define v2 = Character("{b}Voice 2{/b}", color="#ffffff")
define j = Character("{b}Janitor{/b}", color="#ffffff")
define b = Character("{b}Barman{/b}", color="#ffffff")

default relationship = 0

init:
    python:

        def countdown(st, at, length=0.0):

            remaining = length - st
            minutes = (int) (length - st) / 60
            seconds = (int) (length - st) % 60


            if remaining > 10.0:
                return Text("%02d:" % minutes + "%02d" % seconds, color="#fff", size=48), .1
            elif remaining > 0.0:
                return Text("%02d:" % minutes + "%02d" % seconds, color="#f00", size=48), .1
            else:
                renpy.hide_screen("countdown")
                renpy.jump("gameover")

screen countdown(cd_time):
    zorder 2
    frame:
        #xalign 1.0
        xpos 1250
        yalign 0.1
        background None
        add DynamicDisplayable(countdown, length=cd_time)

# The game starts here.
label start:

    # Variables
    $ escalator_tries = 0
    $ dark_hallway_tries = 0
    $ merry_go_round_tries = 0
    $ control_room_tries = 0
    $ asked_drinks = False
    $ lucky_shadow = False
    $ has_keys = False
    $ tricked_news = False
    $ had_conversation = True

    # Relationships
    $ newspaper_boy_rel = 3
    $ barman_rel = 3

    stop sound
    stop music fadeout 3.0

label name:

    # A maneira como se pergunta o nome do jogo tem que ser melhorada
    python:

        name = renpy.input("Name your character:")

        name = name.strip()

    menu:
        "Your name will be [name]. Are you sure?"

        "Yes":

            jump chapter_I

        "No":

            jump name

label chapter_I:

    scene int cafe
    with fade

    window show
 
    p "Hey Matthew!{w=0.5} Glad you called.{w=0.5} Is everything okay?"

    show matthew happy
    with dissolve

    m "Yes,{w=0.2} it's all good!{w=0.5} I actually called because of the {b}chip{/b} you're looking for."


    p "Oh!"
    
    p "I hope you have some good news for me!"

    p "I'm starting to feel like a very unlucky person in general."

    p "I've been looking for one to replace in my {b}arcade{/b} for far too long now."

    m "Well,{w=0.2} I've been searching on several websites and second-hand shops and still nothing."

    m "I even set aside some time to dig into the arcade model itself and I'm afraid to break it to you that it hasn't been produced since 1971."
    
    m "Which makes it a lot harder to find that chip than it already is."

    p "What about Greg?{w=0.5} Did he talk to you?"

    m "Greg also couldn't find anyone who owns an arcade like yours."

    p "Oh,{w=0.2} I see.."

    p "And did we get any replies to our ad?"

    m "No,{w=0.2} still none."

    p "Okay.{w=0.5} No worries!{w=0.5} I just know we will find a way to get that chip and repair my arcade."

    p "So,{w=0.2} what's our next step?"

    m "[name],{w=0.2} I'm afraid there's no next step."

    p "Why do you think that?"

    m "...I've been looking everywhere and I really don't know what else to do."

    m "If you have any suggestions,{w=0.2} I'm all for it."

    p "Ahmm.{w=0.2}.{w=0.2}.{w=0.2} did you try going into that arcade-themed cafe in the mall?{w=0.5} I heard they have some pretty rare arcades."

    show matthew angry

    m "Yes,{w=0.2} I did!{w=0.5} I went to a bunch of malls actually!"

    p "Okay okay,{w=0.2} I believe you!"

    p "I think we should wait a couple more days to see if anyone answers the ad."

    p "If not,{w=0.2} I guess I'll give up my arcade."

    show matthew happy

    m "What if.{w=0.2}.{w=0.2}.{w=0.2} No,{w=0.2} that's not a good idea."

    p "What is it?"

    m "Remember Coppertale Mall?"

    p "Yes.{w=0.2}.{w=0.2}.{w=0.2}  What about it?"

    m "They had an arcade shop with an arcade like yours."

    p "Yeah,{w=0.2} I remember that!{w=0.5} Do you think.{w=0.2}.{w=0.2}.{w=0.2} the arcade might still be there?"

    m "I don't know..."

    m "The mall has been abandoned for over 15 years,{w=0.2} so there's a chance it was left behind..."

    p "I guess there's no harm in checking it out."
    
    p "It's a 10-minute ride from my house.{w=0.5} I'll be in and out."

    m "It's still private property tho.{w=0.2}.{w=0.2}.{w=0.2} but,{w=0.2} yes,{w=0.2} you could give it a try."

    m "I think it might be safer at night when there's no light."

    p "Yeah,{w=0.2} you're right.{w=0.5} I'm not planning taking too long anyways."

    m "Okay,{w=0.2} then!"

    m "Call me afterwards.{w=0.5} I want to know if you got it."

    p "Sure do!"

label chapter_II:


    scene black
    with fade

    window hide

    scene coppertale
    with Dissolve(2.5)

    scene int mall
    with Fade(2,1,1)

    window show

    p "{i}This is way different than I recalled.{w=0.5} A lot bigger too.{w=0.5} I hope I can find a way to the arcade.{/i}"


label chapter_II_choice:

    scene int mall
    with dissolve

    menu:

        "Go foward.":

            scene black
            with fade

            jump chapter_II_go_foward

        "Turn right.":

            scene black
            with fade

            jump chapter_II_turn_right

label chapter_II_go_foward:

    "..You walk foward.{w=0.5} In front of you is an rundown old escalator that leads into an old food court."
    
    "To your left,{w=0.2} there's a dark hallway where you can see a shimmering light in the distance."

    menu:

        "Go up the escalator.":

            $ escalator_tries += 1

            jump chapter_II_escalator

        "Turn to the dark hallway.":

            $ dark_hallway_tries += 1

            jump chapter_II_dark_hallway
    
label chapter_II_escalator:

    "The food court on the first floor is a ghost town.{w=0.5} Closed restaurants,{w=0.2} chairs spread around the plaza and spider webs filling every crack on the walls."

    "Above,{w=0.2} a broken skylight lets through the night breeze.{w=0.5} You look up to see a clear sky full of stars."

    "To your left,{w=0.2} there's a double door.{w=0.5} You open it and follow a long pathway into a large room.{w=0.5} It seems like you've come back to the main entrance."

    if escalator_tries == 1:

        p "How the hell did I come back here?"

    elif escalator_tries == 2:

        p "I am sooooo looost!"

    elif escalator_tries >= 3:

        p "IT IS LITERALLY IMPOSSIBLE that I ended up back here!!"

    jump chapter_II_choice

label chapter_II_dark_hallway:

    "The hallway has clothing shops on both sides and it's longer than you thought."

    "While passing near an old photo booth,{w=0.2} you step on a broken glass and the noise startles you."

    # Broken glass sound effect

    "You continue walking,{w=0.2} this time more carefully than before,{w=0.2} until you reach a dead end.{w=0.5} The shimmering light lits up the entrance of a pet shop.{w=0.5} There's no way in."
    
    if dark_hallway_tries == 1:

        p "It's definitely not this way."

    elif dark_hallway_tries == 2:

        p "This is so confusing."

    elif dark_hallway_tries == 3:

        p "There's no way foward?{w=0.5} AGAIN?!"

    "You end up turning back to the main entrance."

    jump chapter_II_choice

label chapter_II_turn_right:

    "You turn right.{w=0.5} Around the corner there's a newspaper stand and further back you see a merry-go-round.{w=0.5} A sign with a symbol points in the opposite direction."

    menu:

        "Go to the merry-go-round.":
            
            $ merry_go_round_tries += 1

            jump chapter_II_merry_go_round

        "Follow the sign":

            jump chapter_III

label chapter_II_merry_go_round:

    "You walk towards the merry-go-round.{w=0.5} None of the horses are still attached to it.{w=0.5} Strange."

    "You look past it and notice the passage is completely blocked by a couple of collapsed beams.{w=0.5}"

    if merry_go_round_tries == 1:

        p "It's definitely not this way."

    elif merry_go_round_tries == 2:

        p "This is so confusing."

    elif merry_go_round_tries == 3:

        p "There's no way foward?{w=0.5} AGAIN?!"

    "You go back to the main entrance."

    jump chapter_II_choice

label chapter_III:

    "You follow the sign."

    # Int. Mall - Mall (you can see a lit up store). Night.

    "One of the stores to your right is lit with candles.{w=0.5} You get a little bit closer and hear two distinct {b}voices{/b} coming from inside."

    p "{i}People?{w=0.5} What are they doing here?{/i}"

    "You carefully get closer to hear the conversation."

    v1 "Have you heard about the security reinforcement?"

    v2 "Yes,{w=0.2} finally!{w=0.5} We've been waiting for this for what seems to be forever now!"

    v2 "I'm not complaining about the {b}mall security guard{/b}'s work,{w=0.2} but we definitely need more protection!"

    v1 "Agree!{w=0.5} It still feels like yesterday when that abandoned mansion was rehabilitated by {b}humans{/b} and took out 30 of our own."

    v1 "I swear to you,{w=0.2} if I ever sense one I'm not gonna let it slide."

    v2 "Of course,{w=0.2} I think none of us would!{w=0.5} It's either them or us."

    p "{i}Us?{w=0.5} Who's \"us\" if by \"them\" you mean humans?{/i}"

    p "{i}This all sounds very strange.{/i}"

    p "{i}...{/i}"

    p "{i}Oh,{w=0.2} what's this?{/i}"

    window hide

    call screen letter

label chapter_III_letter:

    window show

    p "{i}Okay this is just too weird for me. I think for now I'll just head back home.{/i}"

    "You turn back to see the newspaper stand."

label chapter_IV:

    # Int. Coppertale Mall - Newspaper Stand. Night. 

    p "I think this is the newspaper stand that I passed through a while ago."

    window hide

    call screen newspaper

label chapter_IV_newspaper:
    
    # Front page appears

    window show

    p "August 3rd,{w=0.2} 12 055."

    p "..."

    p "Why are all of these pictures like this?"

    p "What a bizarre newspaper."

    uk "I know right?"

    show newspaper boy
    with dissolve

    p "Ah-"

    p "Wh-?"

    n "It's completely outrageous if you ask me!"

    p "{i}What the hell?!{w=0.5} It looks like one of those things referenced in the letter.{/i}"

    p "{i}Remember: DON'T PANIC.{w=0.5} DON'T PANIC.{w=0.5} DON'T PANIC.{/i}"

    n "Look at this stupid headline: \"The security of Coppertale Mall is being reinforced to protect all vendors and costomers form any outside dangers.\""

    n "What outside dangers?!"

    p "Hmm..."

    n "That's right!"

    n "Nothing!"

    n "Humans are no outside danger whatsoever,{w=0.2} yet we still believe this lie!"

    n "Trust me,{w=0.2} we can drain them faster than they can even say anything!"

    n "I've drained one already and it wasn't such a big deal!{w=0.5} The little guy didn't even have time to react."

    n "What about you?{w=0.5} Have you tried it yourself?"

    hide newspaper boy

    menu:

        "What do you mean by draining?":

            show newspaper boy

            jump chapter_IV_lose_news

        "How can humans not be a threat?":

            show newspaper boy

            jump chapter_IV_gain_news

label chapter_IV_lose_news:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "Errm.{w=0.2}.{w=0.2}.{w=0.2} No.{w=0.5} What do you mean by draining?"

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    n "Oh,{w=0.2} you know.{w=0.2}.{w=0.2}.{w=0.2} consume them."

    hide screen relationships
    with dissolve

    p "{i}Consume?{w=0.5} Just like straight up eating us?{w=0.5} Oh,{w=0.2} man,{w=0.2} don't tell me that letter was right when it talked about my life being at stake.{/i}"

    p "Ah,{w=0.2} I- I see what you mean..."

    n "I sense you're slightly nervous,{w=0.2} pal.{w=0.2}.{w=0.2}.{w=0.2} Are you okay?"

    p "Yeah yeah I'm okay!"

    p "Just had a rough day you know?"

    n "Right..."

    n "Well,{w=0.2} as I was saying,{w=0.2} it's by locking us in that most of us are not aware of our potential."

    n "We are being restrained by ourselves.{w=0.2}.{w=0.2}.{w=0.2} Perpetually afraid and ignorant,{w=0.2} while humans are freely roaming around."

    n "But I'm not gonna succumb to this sort of mindset!"

    n "You'll see,{w=0.2} one of these days,{w=0.2} I'll find a way around that {b}guard in the main entrance{/b} and I'll reach the outside..."

    p "{i}I think he was a bit suspicious about my question and I don't want to find out what being drain actually feels like.{/i}"

    p "{i}Better be more cautious next time.{/i}"

    jump chapter_IV_person

label chapter_IV_gain_news:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "Hmm.{w=0.2}.{w=0.2}.{w=0.2} No.{w=0.5} How can humans not be a threat?{w=0.5} I heard they took out 30 of our own..."

    $ newspaper_boy_rel += 1

    $ relationship = newspaper_boy_rel

    n "What about the incident in the {b}old mansion{/b}?!{w=0.5} I think everyone is making that a bigger fuss than it is."

    hide screen relationships
    with dissolve

    n "Of course there are always gonna be dangers,{w=0.2} especially when they come in packs,{w=0.2} but that doesn't mean that we can't easily take them down."

    p "And how come humans become a threat when they're in packs?"

    n "Think with me,{w=0.2} pal."

    n "Their presence makes us weaker,{w=0.2} makes us fade from existence as we are shadows and they are conscious living beings.{w=0.5} Therefore,{w=0.2} we can't coexist."

    n "However,{w=0.2} I think that only happens when there's a stronger presence.{w=0.5} That's why it's harder for us to notice them if they're alone and need to be careful about any intruders."

    p "{i}Damn it,{w=0.2} I'm so screwed!{/i}"

    p "{i}At least my presence is not strong enough for him to sense I'm a human,{w=0.2} so I don't think he's suspicious about me.{/i}"

    n "We emerge and thrive in abandoned places.{w=0.5} When they start being inhabited again we just cease to exist."

    n "That's what happened in the old mansion,{w=0.2} but then again,{w=0.2} I think we're individually stronger."
    
    n "So we could easily avoid these types of incidents if we're just smart about it instead of reinforcing security."

    n "I've encountered one and I'm perfectly fine.{w=0.2}.{w=0.2}.{w=0.2} But I can't say the same for him.{w=0.5} Ha ha ha ha."

    p "Ha ha ha..."

    p "{i}WHAT DOES HE MEAN HE CAN'T SAY THE SAME FOR HIM?!{w=0.5} DID HE KILL HIM?{/i}"

    p "{i}Oh man,{w=0.2} I should really get out of here as quickly as possible.{w=0.5} In and out,{w=0.2} without raising suspicion.{/i}"

    n "I swear to you,{w=0.2} pal.{w=0.2}.{w=0.2}.{w=0.2} one day I will try to get out of this rathole and be free!{w=0.5} Just like my brother always wanted..."

    n "My brother.{w=0.2}.{w=0.2}.{w=0.2} my poor brother.{w=0.2}.{w=0.2}.{w=0.2} you remind me of him.{w=0.2}.{w=0.2}.{w=0.2} he also was very shy and quiet like you.{w=0.2}.{w=0.2}.{w=0.2} until that DAMN SECURITY GUARD took him out just because he had hopes bigger than ours..."

    n "You'll see.{w=0.2}.{w=0.2}.{w=0.2} that security won't even see what's coming for him!"

label chapter_IV_person:

    "You see a silhouette of a human in the distance."

    p "{i}Is that a person I'm seeing?{w=0.5} Finally,{w=0.2} I might have found a way out of this place!{/i}"

    p "{i}Maybe he's as lost as I am and we can work together to get out of here.{w=0.5} Or,{w=0.2} at least,{w=0.2} we can make some sense of what is going on here!{/i}"

    p "Excuse me,{w=0.2} I really need to go now."

    n "Are you going to buy that newspaper?"

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "Hmm,{w=0.2} I'm sorry.{w=0.5} I don't have any cash on me."

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    n "yeah.{w=0.2}.{w=0.2}.{w=0.2} Right!"

    hide screen relationships
    with dissolve

    hide newspaper boy
    with dissolve

label chapter_V:

    # Int. Mall Entry. Night.

    show janitor happy
    with dissolve

    p "Finally!{w=0.5} A human!"

    j "Hello,{w=0.2} sir,{w=0.2} may I help you with anything?"

    p "Yes!"

    p "Please do you know what's going on here?{w=0.5} What are these shadowy -.{w=0.2}.{w=0.2}.{w=0.2} thingies?{w=0.5} Can they really kill us?!"

    p "I just talked to one and I really think they can!{w=0.5} How can we get out of this mall?"

    j "Oh,{w=0.2} you can get out through the mall entrance.{w=0.5} It's the one right behind you!"

    p "But now there's a security guard blocking the door!"

    j "What security guard?"

    p "The big shadow blocking the entrance!{w=0.5} At least is what they call it,{w=0.2} a guard!"

    j "Oh,{w=0.2} now I see the big fella!{w=0.5} My eyes don't work as they used to,{w=0.2} sir."

    p "So,{w=0.2} you have never seen him until now?!{w=0.5} Have you talked to anyone here?"

    j "Oh,{w=0.2} yes,{w=0.2} all the time!{w=0.5} I've been working here for 25 years now."

    p "So you have been talking to these shadows for the last 15 years,{w=0.2} is that right?"

    j "To these what?"

    p "Shadows?"

    j "I don't know what you're talking about."

    p "{i}Oh my,{w=0.2} this man is senile.{w=0.5} I'm not getting anywhere like this!{/i}"

    p "Don't worry about it,{w=0.2} sir."

    p "I know I can't get out through the main entrance because the security guard won't let me.{w=0.5} I'm just asking for an exit."

    j "Oh the Exit!{w=0.5} You could have asked me that before!"

    j "You take a left after you pass the newspaper stand and the Exit is at the end of the hallway to your right."

    p "Okay,{w=0.2} thank you so much!{w=0.5} I really really appreciate your help!"

    j "What?{w=0.5} Sorry I didn't quite catch that.{w=0.5} May I help you with anything sir?"

    p "No,{w=0.2} don't worry!{w=0.5} Thank you for asking."

    hide janitor happy
    with dissolve

    scene black
    with fade

    p "{i}How can he be here for that long?{w=0.5} And they've never noticed him?!{w=0.5} This is a heck of a situation.{/i}"

    p "{i}These creatures are traces of a long gone human presence,{w=0.2} but they coexist with us because we bring liveliness to places.{/i}"

label chapter_VI:

    # Int. Coppertale Mall - Exit Bar (exterior). Night

    # (A door with a big Exit sign appears)

    p "This has got to be it!{w=0.5} And no security guard to be seen.{w=0.5} Good to know!"

    p "I'm so relieved to finally get out in one piec-"

label chapter_VII:

    # Int. Coppertale Mall - Exit Bar (interior). Night

    show bartender normal
    with dissolve

    b "Welcome to the Exit Bar!{w=0.5} Can I get you anything?"

    p "{i}That freaking janitor.{/i}"

    p "{i}Relax.{w=0.5} Just talk to him.{w=0.5} Casual,{w=0.2} normal,{w=0.2} you're just a regular customer,{w=0.2} [name].{w=0.5} You can talk your way through this.{/i}"

    b "..."

    p "..."

    b "Hello?"

    p "Sorry.{w=0.5} Can you repeat that?"

    b "Oh,{w=0.2} I {b}sensed{/b} you were new here.{w=0.5} We serve beer,{w=0.2} margarita,{w=0.2} whiskey sour,{w=0.2}...?{w=0.5} What are we having today?"

    hide bartender normal

    menu:

        "I'll have a beer.":

            $ asked_drinks = True

            show bartender normal

            jump chapter_VII_beer

        "Do you serve martinis?":

            $ asked_drinks = True

            show bartender normal

            jump chapter_VII_martini

        "I'm good,{w=0.2} thanks.":

            show bartender normal

            jump chapter_VII_nothing

label chapter_VII_beer:

    $ relationship = barman_rel

    show screen relationships

    p "I'll have a beer."

    $ barman_rel += 1

    $ relationship = barman_rel

    b "You are my kind of guy!{w=0.5} The classic never fails!"

    hide screen relationships
    with dissolve

    jump chapter_VII_conversation

label chapter_VII_martini:

    $ relationship = barman_rel

    show screen relationships

    p "Do you serve martinis?"

    $ barman_rel += 1

    $ relationship = barman_rel

    b "Of course I do.{w=0.5} Just one?"

    hide screen relationships
    with dissolve

    p "Yes please."

    jump chapter_VII_conversation

label chapter_VII_nothing:

    $ relationship = barman_rel

    show screen relationships

    p "I'm good,{w=0.2} thanks."

    $ barman_rel -= 1

    $ relationship = barman_rel

    b "Okay.{w=0.2}.{w=0.2}.{w=0.2} so,{w=0.2} are you coming to meet some friends?{w=0.5} Or did you come by mistake?"

    hide screen relationships
    with dissolve

    p "I guess we could say I came by mistake."

    b "Yeah,{w=0.2} I bet you did."

    jump chapter_VII_conversation

label chapter_VII_conversation:

    b "So,{w=0.2} you're new here."

    b "That's very uncommon.{w=0.5} I'm intrigued.{w=0.5} Did you get to meet someone already?"

    p "No,{w=0.2} not really..."

    b "Then,{w=0.2} allow me to introduce myself."

    b "I'm Lucas,{w=0.2} but shadows around here call me by my nickname,{w=0.2} Lucky."
    
    b "I opened this bar 8 years ago and I've been here since then!{w=0.5} Business wasn't always great,{w=0.2} but fortunately things ended up working out for me."

    b "I'm a lucky shadow,{w=0.2} hence the name.{w=0.5} hahaha."

    b "What about you?{w=0.5} What do you do Mr.{w=0.2}.{w=0.2}.{w=0.2} I'm sorry,{w=0.2} what's your name again?"

    hide bartender normal

    menu:

        "I'm [name],{w=0.2} a not so lucky shadow.":

            $ lucky_shadow = True

            show bartender normal

            jump chapter_VII_not_lucky

        "I'm [name],{w=0.2} an ophthalmologist":

            show bartender normal

            jump chapter_VII_ophtal

label chapter_VII_not_lucky:

    $ relationship = barman_rel

    show screen relationships

    p "I haven't said it.{w=0.5} I'm [name].{w=0.5} a not so lucky -.{w=0.2}.{w=0.2}.{w=0.2} shadow."

    $ barman_rel += 1

    $ relationship = barman_rel

    b "ha ha ha,{w=0.2} then let me tell you my secret.{w=0.5} Shadows say I'm lucky,{w=0.2} but in reality I'm just very optimistic."

    hide screen relationships
    with dissolve

    b "It's my motto.{w=0.5} “No matter what situation you're in,{w=0.2} there's always a way to win.” There's always an upside.{w=0.5} And THAT's where you should focus on."

    b "For example:"

    b "During the first couple of years,{w=0.2} after I opened this bar,{w=0.2} I had to sleep on this very floor.{w=0.5} I honestly had no hopes of a better tomorrow,{w=0.2} but I just persevered,{w=0.2} you know?"

    b "Now,{w=0.2} here I am!{w=0.5} Just living the dream!{w=0.5} Hanging out everyday with the drunks!{w=0.5} I always knew this was meant for me!{w=0.5} I always knew I wanted to serve drinks for a living.{w=0.5} haha."

    if asked_drinks:

        b "Speaking of the devil,{w=0.2} here's yours!"

        p "Thank you."

    p "I understand that,{w=0.2} but sometimes I just feel like I tried just about everything.{w=0.2}.{w=0.2}.{w=0.2} not only for me,{w=0.2} but for my son as well."
    
    p "I even find myself {b}where I don't belong{/b} sometimes,{w=0.2} you know?{w=0.5} There's -"

    jump chapter_VII_beers_fall

label chapter_VII_ophtal:

    $ relationship = barman_rel

    show screen relationships

    b "An ophthalmologist?{w=0.5} What is that?"

    p "An eye care specialist."

    b "Eye?"

    p "{i}Damn it!{w=0.5} I fucked up already.{/i}" 
    
    p "It's just a fancy way of saying I help people.{w=0.2}.{w=0.2}.{w=0.2} through.{w=0.2}.{w=0.2}.{w=0.2} their.{w=0.2}.{w=0.2}.{w=0.2} senses..."

    $ barman_rel -= 1

    $ relationship = barman_rel

    b "..."

    hide screen relationships
    with dissolve

    jump chapter_VII_beers_fall

label chapter_VII_beers_fall:

    # noise of beers falling

    b "Oh god damn it!{w=0.5} What a damn mess!"

    b "Look,{w=0.2} sorry if this is asking too much,{w=0.2} but do you think you could go outside and get me the janitor?"

    b "I just have a lot on my plate right now and I think you are the only one here who can still walk in a straight line."
    
    p "Yeah yeah,{w=0.2} no worries."

    hide bartender normal
    with dissolve

    scene black
    with fade

    if lucky_shadow:

        p "{i}Phew!{w=0.5} Well.{w=0.2}.{w=0.2}.{w=0.2} he seems nice!{w=0.5} Still scared.{w=0.2}.{w=0.2}.{w=0.2} for my life!{w=0.5} But I think I'm doing okay.{/i}"

        p "{i}Maybe when I come back I can get him to tell me where I can get out of this hell hole.{/i}"
    
    else:

        p "{i}God freaking dammit!{w=0.5} I was too suspicious!{w=0.5} If it wasn't for those beers dropping,{w=0.2} I would be so screwed!{/i}"

label chapter_VIII:

    # Int. Coppertale Mall - Mall entry. Night

    p "Excuse me,{w=0.2} sir?"

    show janitor happy
    with dissolve

    j "Hello,{w=0.2} sir,{w=0.2} may I help you with anything?"

    p "Hello again."

    j "Oh,{w=0.2} I remember you.{w=0.5} Did you find the bar you were looking for?"

    p "Well,{w=0.2} kind of,{w=0.2} yes.{w=0.5} Speaking of it,{w=0.2} the bartender,{w=0.2} Lucky,{w=0.2} asked for you."

    hide janitor happy
    with dissolve

label chapter_IX:

    # Int. Coppertale Mall - Exit Bar. Night

    p "We're here!"

    show janitor happy at left
    with dissolve

    show bartender normal at right
    with dissolve

    b "Thank you,{w=0.2} [name]."

    b "Hmm.{w=0.2}.{w=0.2}.{w=0.2} I'm sensing something off.{w=0.2}.{w=0.2}.{w=0.2} Do you feel that...like something eerie?{w=0.5} Or is it just me?"

    p "{i}I completely forgot that we can't have a strong presence,{w=0.2} otherwise they'll notice we're humans.{/i}"

    hide bartender normal
    hide janitor happy

    menu:

        "No,{w=0.2} I don't feel anything.":

            show bartender normal at right
            show janitor happy at left

            jump chapter_IX_dont_feel

        "Yes,{w=0.2} I do feel a little something.":

            show bartender normal at right
            show janitor happy at left

            jump chapter_IX_feel

label chapter_IX_dont_feel:

    $ relationship = barman_rel

    show screen relationships

    p "No,{w=0.2} I don't feel anything.{w=0.5} What about you.{w=0.2}.{w=0.2}.{w=0.2} hm.{w=0.2}.{w=0.2}.{w=0.2} Mr.{w=0.2}.{w=0.2}.{w=0.2} Janitor?{w=0.5} Do you feel anything?"

    # suspanse

    j "I do,{w=0.2} actually.{w=0.2}.{w=0.2}.{w=0.2} I sense.{w=0.2}.{w=0.2}.{w=0.2} beer!{w=0.5} I'll go ahead and clean it up."

    $ barman_rel += 1

    $ relationship = barman_rel

    b "Right!{w=0.5} Almost forgot about that.{w=0.5} Thank you again [name] for the help!"

    hide screen relationships
    with dissolve

    b "However I can repay you,{w=0.2} just say the word.{w=0.5} Drinks tonight are on the house!"

    jump chapter_IX_goodbye

label chapter_IX_feel:

    $ relationship = barman_rel

    show screen relationships

    p "Yes,{w=0.2} I do feel a little something.{w=0.5} If you ask me,{w=0.2} I think it's coming from those shadows in the back..."

    j "No,{w=0.2} people always tell me that.{w=0.5} It's probably because they {b}sense{/b} we're two most good-looking individuals around the block."

    p "{i}The fact that this guy hasn't died yet is a complete mystery to me!{/i}"

    b "It's definitely coming from around here and it's making me feel a bit nauseated."

    $ barman_rel -= 1

    $ relationship = barman_rel

    b "Nevertheless,{w=0.2} do you think you could clean up that mess next to the jukebox?"

    hide screen relationships
    with dissolve

    j "Sure will boss!{w=0.5} On it."

    b "Thank you again [name] for the help!{w=0.5} However I can repay you,{w=0.2} just say the word."

label chapter_IX_goodbye:

    hide janitor happy
    with dissolve

    if barman_rel <= 0:

        $ had_conversation = True

        b "Hey,{w=0.2} now that's just the two of us.{w=0.5} I need to tell you a couple of words."

        b "..."

        b "Humans are not welcome here."

        p "...Humans?{w=0.5} I don't know what you mean."

        b "Don't try to fool me."

        b "Just be glad I'm the one finding it out.{w=0.5} Others won't be so forgiving,{w=0.2} so I'd strongly advise you not to give yourself away that easily or you'll never get out of here intact."

        b "I've been able to get old Jimmy “janitor” there off the hook a couple of times now,{w=0.2} but he's not getting any younger,{w=0.2} or smarter."

        b "What I'm saying is: I'm already putting myself at risk here,{w=0.2} but I'm not gonna take a bullet for you."

        b "Don't get me wrong.{w=0.5} You're a nice kid,{w=0.2} but the moment the shadows find out you're a human,{w=0.2} they are definitely gonna take you as a threat."

        b "So just.{w=0.2}.{w=0.2}.{w=0.2} be careful out there!"

    p "Thanks."

    p "Anyways I can't stay here much longer."

    b "Already?{w=0.5} But you just got here."

    p "Yeah I know,{w=0.2} but you COULD help me with something else if you're willing."

    b "What is it."

    p "When I got here,{w=0.2} I was actually looking for an outside exit,{w=0.2} not the Exit Bar.{w=0.5} Do you,{w=0.2} for any reason,{w=0.2} know one?"

    p "I know the main entrance is protected by a guard,{w=0.2} and they are planning to reinforce security."

    b "..."

    b "Well kid.{w=0.2}.{w=0.2}.{w=0.2} not gonna lie to you.{w=0.5} Nobody has gone out there for years now."

    b "And the last person who tried,{w=0.2} got drained by the mall security guard."

    p "Do you know how he tried to get out?"

    b "Yes,{w=0.2} he tried to escape through some vents over the cinema.{w=0.5} I heard they were sealed after the incident."

    b "I wouldn't be surprised if there were more of them..."

    p "Do you think you know where they are?"

    b "I don't.{w=0.5} But I might know who does..."

    p "Who?"

    b "The {b}Newspaper boy{/b} over the newspaper stand.{w=0.5} If somebody knows another route,{w=0.2} he is the most likely to."

    p "Really...?{w=0.5} Okay thanks for the info!"

    b "Kid!"

    b "..."

    b "I really do mean this: BE careful out there."

    hide bartender normal
    with dissolve

label chapter_X:

    # Int. Coppertale Mall - Newspaper Stand. Night.

    p "Hello again."

    show newspaper boy
    with dissolve

    n "Hey."

    n "Are you looking for something specific I can help you with?"

    p "Yes,{w=0.2} actually."

    hide newspaper boy

    menu:

        "Trick the newspaper boy to giving you the information.":

            $ tricked_news = True

            show newspaper boy

            jump chapter_X_trick

        "Agree with Newspaperboy's ideologies in order to give to the information.":

            show newspaper boy

            jump chapter_X_agree

label chapter_X_trick:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "Sorry for leaving so abruptly,{w=0.2} you were in the  middle of the story of your brother..."

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    n "Why do you care?!"

    hide screen relationships
    with dissolve

    p "Well,{w=0.2} you said something about the security guard taking out your brother.{w=0.2}.{w=0.2}.{w=0.2} How did he find out your brother was leaving?"

    n "You see,{w=0.2} my brother was always smart,{w=0.2} but not very cautious.{w=0.2}.{w=0.2}.{w=0.2} The day he planned his escape,{w=0.2} he was followed by the guard until one of the vents."

    p "I see..."

    n "They then proceeded to publicly drain him so the community saw what would happen if anybody else tried to escape."

    n "To this day I still have nightmares about that night..."

    p "And you said you were planning something against that security guard.{w=0.2}.{w=0.2}.{w=0.2} how so?"

    n "That mall entrance security guard was the damn bastard who sentenced my brother."

    n "I WILL make him pay.{w=0.5} But I can only do that when I have a way out of this place where I can get out!"

    p "Do you think there are any other exits?"

    n "The only thing I know for certain is this: there has GOT TO BE another exit.{w=0.5} The vents on this mall are way bigger than they look."

    n "After my brother's escape,{w=0.2} the security around that area got a lot less supervised because they sealed it pretty well,{w=0.2} and discarded any other possible exits through the vents."

    p "And how can you know where the other exits are?"

    n "Now THAT is the big problem I'm still trying to solve.{w=0.5} The vents of the mall are all registered in its blueprints,{w=0.2} which are located in the security guard's control room."

    n "Problem is: The guard is trained to sense from very far away so he can easily feel anyone just by getting near the room."

    n "Plus,{w=0.2} after getting in,{w=0.2} we would still need some time to unlock the safe where the prints are."
    
    n "Which is very impossible due to the fact the security guard doesn't go farther than a 45-60 seconds distance from the room."

    n "So yeah,{w=0.2} that's the biggest challenge to get through.{w=0.5} But as I said: one day I WILL find a way and get the hell out of this rat hole!"

    p "What a hell of a story.{w=0.2}.{w=0.2}.{w=0.2} I sincerely wish you the best of luck finding a way!"

    n "Cheers bud!"

    n "Besides that,{w=0.2} can I help you with anything else?{w=0.5} Maybe you finally brought that cash you needed.{w=0.2}.{w=0.2}.{w=0.2} haha"

    p "No,{w=0.2} thanks anyway though!"

    hide newspaper boy
    with dissolve

    jump chapter_XI

label chapter_X_agree:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "What you said about us not reaching our full potential got me thinking..."

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    n "I knew you weren't brainless like most."

    hide screen relationships
    with dissolve

    p "Yeah,{w=0.2} thank you for enlightening me."

    p "Humans are in fact no danger to us and still we're hiding out here.{w=0.5} It's an absurdity!"

    n "That's what I always say.{w=0.5} Security reinforcement doesn't protect us,{w=0.2} it protects them."

    n "If more shadows would have listened to me,{w=0.2} we would be outside by now.{w=0.2}.{w=0.2}.{w=0.2} free to go wherever we like.{w=0.2}.{w=0.2}.{w=0.2} to drain whoever we want.{w=0.5} Not enclosed in this ugly ass concrete box."

    p "{i}Oh,{w=0.2} boy,{w=0.2} what am I putting myself into?!{/i}"

    p "Agreed!"

    p "...They should be afraid of us,{w=0.2} not the other way around!{w=0.5} I think I'm trying to get out of here,{w=0.2} just like your brother."

    n "I don't know if that's a good idea..."

    p "I've got nothing to lose.{w=0.2}.{w=0.2}.{w=0.2} But I need your help if I want to succeed."

    p "Once I'm out,{w=0.2} it's easier to help you escape.{w=0.5} They won't ever believe I'll be heading back to get you."

    n "Really?!{w=0.5} Would you do that for me?"

    p "Of course!"

    p "If you help me,{w=0.2} I'll help you.{w=0.5} It's for a common cause my friend!"

    p "{i}Please believe me.{/i}"

    n "Hmm..."

    n "It would be very risky.{w=0.2}.{w=0.2}.{w=0.2} but I think there's a blueprint of the mall with all of its vents registered."

    n "They might be our only way out.{w=0.5} After my brother tried to go through one.{w=0.2}.{w=0.2}.{w=0.2} they sealed it,{w=0.2} but for all I know,{w=0.2} that's the only one they've taken care of."

    n "Problem is: the blueprint is in the security guard's control room."

    p "Do you think I can take it without him noticing?"

    n "It's very unlikely.{w=0.2}.{w=0.2}.{w=0.2} but not impossible."

    n "He usually walks around the mall entry and it takes him more or less 90 to go from his room,{w=0.2} around the entrance,{w=0.2} and back."

    n "So,{w=0.2} you need to be quick."

    p "Alright."

    p "I'll try not to get drained haha."

    hide newspaper boy
    with dissolve

label chapter_XI:

    scene black 
    with fade

    p "Okay,{w=0.2} I see it!"

    p " The control room!"

    p " I must be quick."

    # Int. Coppertale Mall - Control Room. Night

    "As you enter the room you see two paper trays piled up on the left and two cabinets side by side on top of the front desk."

    "You take a look around.{w=0.5} The office looks messy and most of the equipment seems outdated and a bit cluttered."

    "Despite this,{w=0.2} you can't help but notice an old security guard's jacket in a coat hanger behind the door."

    p "Where should I start?"

    show screen countdown(90)

label chapter_XI_first_options:

    menu:
        "Search through the documents in the paper trays.":

            jump chapter_XI_paper_strays

        "Search the paper cabinets on top of the front desk.":

            jump chapter_XI_paper_cabinets

        "Search the jacket on the coat hanger.":

            jump chapter_XI_jacket

label chapter_XI_paper_strays:

    "There's a stack of paper in each tray.{w=0.5} The bottom one is practically full while the top one only has a couple of loosely folded sheets of paper."

    menu:

        "Search the tray at the bottom.":
            
            jump chapter_XI_bottom

        "Search the tray at the top.":

            jump chapter_XI_top

        "Look somewhere else.":

            jump chapter_XI_first_options

label chapter_XI_bottom:

    "You notice a logo in each paper resembling the one from the newspaper you saw earlier.{w=0.5} Each has some distinct black spots which you assume are some kind of pictures of shadows."

    jump chapter_XI_paper_strays

label chapter_XI_top:

    "These seem to be some kind of personal notes.{w=0.5} Teared up pieces of diary?{w=0.5} Maybe some cooking recipes?{w=0.5} Who knows."

    jump chapter_XI_paper_strays

label chapter_XI_paper_cabinets:

    "The paper cabinet on the left is open.{w=0.5} Inside,{w=0.2} the documents seem to be arranged in a very disordered manner.{w=0.5} The cabinet on the right is closed."

    menu:

        "Go through the documents on the left cabinet.":
            
            jump chapter_XI_left_cabinet

        "Try to open the right cabinet.":

            jump chapter_XI_right_cabinet

        "Look somewhere else.":

            jump chapter_XI_first_options

label chapter_XI_left_cabinet:

    "You take a quick look at the documents on the left cabinet.{w=0.5} These seem to be identity documents of the mall's vendors."

    jump chapter_XI_paper_cabinets

label chapter_XI_right_cabinet:

    if has_keys:

        menu:

            "Use the small key with a golden shell engraved.":

                jump chapter_XI_small_key

            "Use the medium-sized key (rusty and old).":

                jump chapter_XI_medium_key

            "Use the large key with a blue tag.":

                jump chapter_XI_large_key

    else:

        "You try to open the right cabinet.{w=0.5} It's locked.{w=0.5} You would need a key to open it."

        jump chapter_XI_paper_cabinets

label chapter_XI_jacket:

    "You check both pockets on the jacket.{w=0.5} The one on the right is ripped,{w=0.2} while the other has some lint and a couple of strange coins."
    
    "You're about to give up,{w=0.2} but you notice an inner pocket."

    menu:

        "Check the inner pocket.":

            jump chapter_XI_inner_pocket

        "Look somewhere else.":

            jump chapter_XI_first_options

label chapter_XI_inner_pocket:

    if has_keys:

        "You already got the keys."

        jump chapter_XI_jacket

    else:

        "There are three keys inside.{w=0.5} A small one with a golden shell engraved,{w=0.2} a medium-sized one,{w=0.2} rusty and old,{w=0.2} and a large one with a blue tag."

        p "{i}I'll keep them.{w=0.5} They might be useful!{/i}"

        $ has_keys = True

    jump chapter_XI_first_options

label chapter_XI_small_key:

    p "{i}A small for a small cabinet.{/i}"

    "After a few tries,{w=0.2} you acknowledge that you picked the wrong key."

    jump chapter_XI_right_cabinet

label chapter_XI_medium_key:

    p "{i}The middle one it is.{/i}"

    "After a few tries,{w=0.2} you acknowledge that you picked the wrong key."

    jump chapter_XI_right_cabinet

label chapter_XI_large_key:

    p "{i}Maybe the blue tag is referring to the blueprints.{/i}"

    "The lock opens."

    p "Finally!"

    hide screen countdown

label chapter_XII:

    # Int. Coppertale Mall - Mall entry. Night

    p "I got it!"

    p "Now,{w=0.2} I just need to check where these vents are!"

    p "Hm,{w=0.2} I can't understand anything here!"

    p "It's all blurry!"

    show newspaper boy
    with dissolve

    if tricked_news:

        jump chapter_XII_decrease

    else:

        jump chapter_XII_agree

label chapter_XII_decrease:

    $ relationship = newspaper_boy_rel

    show screen relationships

    n "What's that on your hand?"

    p "Oh it's you!"

    n "..."

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    p "This is.{w=0.2}.{w=0.2}.{w=0.2} ahm.{w=0.2}.{w=0.2}.{w=0.2} some documents from this business I run.{w=0.5} Nothing that important,{w=0.2} but I'm kind of in a hurry to deliver them."

    hide screen relationships
    with dissolve

    n "Yeah,{w=0.2} sure you are!"

    n "Now tell me..."

    n "What are you planning to do with those blueprints?"

    p "{i}Fuck.{/i}"

    p "Look,{w=0.2} I'm sorry I didn't tell you my plan before.{w=0.5} I wanted to keep it as secretive as I could.{w=0.5} It's nothing personal!"

    n "Then you shouldn't be walking around with blueprints on your hands.{w=0.5} I can sense them from half a mile away."

    p "Yeah..."

    n "So,{w=0.2} what's our plan?"

    p "\"Our\" plan?"

    n "Yeah,{w=0.2} how are we going to get out of here?"

    p "Well.{w=0.2}.{w=0.2}.{w=0.2} I was thinking about escaping through one of the vents..."

    p "I've managed to keep a low profile until now,{w=0.2} so I think I might have a chance of making it."

    n "True,{w=0.2} you're not known around here,{w=0.2} but you're not as familiar with the mall and its environment as I am.{w=0.5} I think I can be a great asset."

    p "...Yes,{w=0.2} you're right.{w=0.5} I could use some help in.{w=0.2}.{w=0.2}.{w=0.2} ahm.{w=0.2}.{w=0.2}.{w=0.2} interpreting this blueprint."

    n "Yeah,{w=0.2} for sure."

    n "When were you planning to escape?"

    p "Today."

    n "Today?!"

    p "Yes.{w=0.5} I can't wait any longer.{w=0.5} I just need your opinion on this blueprint."

    p "And if I succeed,{w=0.2} I'll come back for you as soon as I can."

    n "Hm.{w=0.2}.{w=0.2}.{w=0.2} Do I need to remind you that you just tried to trick me?{w=0.5} \"It's for a bussiness I run\",{w=0.2} you said.{w=0.5} How the hell am I supposed to trust you after that?"

    p "{i}Okay,{w=0.2} time to bluff my way out of this!{/i}"

    p "The truth is: You just have to!"

    p "I mean.{w=0.2}.{w=0.2}.{w=0.2} Do you have any other ideas?{w=0.5} This is the only way!"

    p "And if you rat on me,{w=0.2} you also lose everything.{w=0.5} I'll tell everyone you were also planning to escape and planning to avenge your brother by taking on the security guard."

    p "If I go down,{w=0.2} you go down with me!"

    n "..."

    n "Ok Ok fine,{w=0.2} you win!"

    n "Give me that damn blueprint then."

    # Paper sound effect

    n "..."

    n "Hmmm from what I can sense here,{w=0.2} the only way out is through a vent inside the security guard's control room itself."

    n "Did you see it by chance while you were there?"

    p "No,{w=0.2} I spent very little time there."

    n "Well,{w=0.2} I'm afraid you'll have to go in there again and try to find the hidden conduct."

    p "Alright.{w=0.5} I'll do my best!{w=0.5} And I assure you,{w=0.2} if I can get out of this alive,{w=0.2} I'll make sure you're next."

    p "So don't raise any suspicion until then."

    n "It's not like I have much choice in believing you or not,{w=0.2} but okay."

    n "I wish you good luck.{w=0.5} And not A WORD about me if you get caught."

    p "\"Mum's the word.\""

    hide newspaper boy
    with dissolve

    p "{i}I can't believe I just pulled that one off.{w=0.2}.{w=0.2}.{w=0.2} Now I REALLY need to get out of here as quickly as possible.{/i}"

    jump chapter_XIII

label chapter_XII_agree:

    $ relationship = newspaper_boy_rel

    show screen relationships

    n "You GOT IT!"

    $ newspaper_boy_rel += 1

    $ relationship = newspaper_boy_rel

    p "Oh,{w=0.2} hey!"

    hide screen relationships
    with dissolve

    p "Yeah,{w=0.2} I got it!"

    n "So,{w=0.2} where can we find these vents?"

    p "I'm not sure yet!"

    n "Open it then!"

    p "You can check it out first if you want..."

    n ".{w=0.2}.{w=0.2}.{w=0.2} Okay,{w=0.2} let me sense it."

    n "..."

    p "..."
    
    p "What are our options?"

    n "Well..."

    n "Apparently,{w=0.2} they sealed all of the vents but one."

    p "Where is it?"

    n "..."

    n "It's -.{w=0.5} I feel bad telling you this,{w=0.2} but the vent is in the {b}security guard's control room{/b}..."

    n "Did you see it by chance?"

    p "No,{w=0.2} I spent very little time there."

    n "Are you thinking about going in again?"

    p "What choice do I have?"

    p "I already stole the blueprint.{w=0.5} If the guard ever finds that out,{w=0.2} I'm screwed."

    p "Might as well just go through with the plan."

    n "That's the spirit!"

    p "If in the next 10 minutes,{w=0.2} things stay as calm as they are right now,{w=0.2} take it as a win!"

    p "Then,{w=0.2} once I'm out there,{w=0.2} I'll make sure you're next,{w=0.2} so don't raise any suspicion until then."

    n "That's very brave.{w=0.5} I'm sure you are going to be a great asset in my escape."

    n "Then I'll avenge my brother and show the shadows a better way of life!"

    p "...I'm glad to help you out..."

    hide newspaper boy
    with dissolve

    scene black
    with fade

    p "{i}I guess if there are lunatics in the human world,{w=0.2} the shadow world won't be much different.{/i}"

label chapter_XIII:

    # Int. Coppertale Mall: Control Room. Night

    p "Where would a vent in this room be?!"

label chapter_XIII_first_choices:

    $ control_room_tries += 1

    if control_room_tries > 3:

        jump chapter_XIII_guard

    menu:

        "Look behind the monitor.":

            jump chapter_XIII_monitor

        "Look under the desk.":

            jump chapter_XIII_desk

        "Look behind the wooden board.":

            jump chapter_XIII_board

        "Look behind the soundboard.":

            jump chapter_XIII_soundboard


label chapter_XIII_monitor:

    "You look behind the monitor."

    "Surprise,{w=0.2} surprise!{w=0.5} It's a white plane wall."

    jump chapter_XIII_first_choices

label chapter_XIII_desk:

    "You look under the desk.{w=0.5} I hope they can sense dust because this surely needs to be vacuumed."

    jump chapter_XIII_first_choices

label chapter_XIII_board:

    "You look behind the wooden board.{w=0.5} There's a hole in the wall,{w=0.2} the size of a football."

    menu:

        "Check the hole.":

            jump chapter_XIII_beer

        "Look somewhere else.":

            jump chapter_XIII_first_choices

label chapter_XIII_beer:

    "There are two packs of craft beer inside.{w=0.5} Engraved on the cap,{w=0.2} you can see the Exit Bar logo."

    p "Oops,{w=0.2} I think I found the guard's personal stock."

    jump chapter_XIII_board

label chapter_XIII_soundboard:

    "You look behind the soundboard.{w=0.5} A bird's nest is tucked between cables.{w=0.5} This soundboard hasn't been used for at least a decade."

    jump chapter_XIII_first_choices

label chapter_XIII_guard:

    show security guard
    with dissolve

    s "Who are you?!{w=0.5} And what are you doing here?!"

    p "..."

    p "ahm-ah-I..."

    p "..."

    s "I said: Who are you?!"

    show bartender normal at right
    with dissolve

    b "Hey Tony,{w=0.2} what's going on here?{w=0.5} [name],{w=0.2} I need you back in the bar..."

    s "..."

    b "Tony.{w=0.2}.{w=0.2}.{w=0.2} sorry about him,{w=0.2} that's my new employee.{w=0.5} He's a bit shy.{w=0.2}.{w=0.2}.{w=0.2} and a bit lost to be honest."

    s "Lucas.{w=0.5} Didn't sense you there.{w=0.5} Can you explain to me the reason why your new \"companion\" is here?"

    b "He's just lost.{w=0.5} He has a horrible sense of direction and is still getting used to the mall.{w=0.5} Isn't that right.{w=0.2}.{w=0.2}.{w=0.2} \"[name!u]\"?!"

    p "Ahm.{w=0.2}.{w=0.2}.{w=0.2} yes.{w=0.2}.{w=0.2}.{w=0.2} that's right..."

    s "Lucas,{w=0.2} you know what snooping around gets you into..."

    s "I'm gonna let this one slide because I owe you one,{w=0.2} but you better discipline this friend of yours or I'll make sure to do it myself..."

    s "And shadows around here sure don't describe me as friendly.{w=0.2}.{w=0.2}.{w=0.2} or forgiving."

    b "You're right,{w=0.2} Tony.{w=0.5} Won't bother you again.{w=0.5} Come on [name].{w=0.5} I need to have a word with you."

    hide security guard
    with dissolve

    hide bartender normal
    with dissolve

label chapter_XIV:

    # Int. Coppertale Mall: Mall Entry. Night

    show bartender normal
    with dissolve

    b "Are you out of your mind?!{w=0.5} In all the places you could be,{w=0.2} you decided to be in the middle of the office of the most dangerous shadow of the entire mall?!"

    b "Do you WANT to get yourself killed out here?"

    p "Sorry,{w=0.2} but that was my way out!"

    p "The only vent they did not seal after that incident,{w=0.2} was the one in the guard's control room!"

    b "What makes you say that?"

    p "It's on the mall's blueprint that I found in the security room."

    b "Blueprint?{w=0.5} Give it to me so I can sense it."

    b "..."

    b "..."

    b "I see..."
    
    b "Well,{w=0.2} I don't know how you came to that conclusion,{w=0.2} but according to this,{w=0.2} the only vent that wasn't sealed is on the second floor,{w=0.2} store 22,{w=0.2} as soon as you enter on your right."

    p "{i}That damn liar must have given me the wrong direction on purpose.{/i}"

    p "Oh,{w=0.2} I'm sorry Lucky.{w=0.5} I need to go there right now.{w=0.5} Thank you for saving me back there."

    b "[name],{w=0.2} wait..."

    p "Yes?"

    b "So,{w=0.2} you're really out of your mind."

    p "You can say so,{w=0.2} yes."

    b "hahahah,{w=0.2} crazy.{w=0.2}.{w=0.2}.{w=0.2} but a nice {b}person{/b},{w=0.2} I mean shadow.{w=0.2}.{w=0.2}.{w=0.2} haha"
    
    b "Goodbye,{w=0.2} pal."

    hide bartender normal
    with dissolve

    if not had_conversation:
        
        p "{i}Did he just say person?{w=0.5} He knew all along?!{/i}"
        
        p "{i}Well,{w=0.2} I guess the janitor must be lucky to have someone looking out for him.{w=0.5} What a great shadow!{/i}"

label chapter_XV:

    # Int. Coppertale Mall: Arcade. Night

    p "{i}I can't believe it was here all this time.{w=0.5} How didn't I see it?!{/i}"

    p "{i}It doesn't matter now!{w=0.5} I need to find him before he gets away.{/i}"

    p "{i}...{/i}"

    p "{i}Oh my!{w=0.5} It's back there,{w=0.2} it's the arcade just like mine!{/i}"

    menu:

        "Go to the back to get the chip.":

            jump chapter_XV_chip

        "Go to your right to find the vent.":

            jump chapter_XVI_vent

label chapter_XV_chip:

    p "{i}Finally,{w=0.2} I can't believe I actually got it after all of this mess!{/i}"

    p "{i}Now,{w=0.2} I should really get going now before that damn shadow escapes!{/i}"

    p "{i}...{/i}"

    p "{i}That 's it!{w=0.5} That has GOT to be the vent Lucky was talking about{/i}"

    # chapeu do newspaper boy

    p "{i}Is that his hat?!{w=0.5} What does that mean?{w=0.5} Was he able to get out?!{/i}"

    p "{i}...{/i}"

    p "{i}Is that the exit?!{w=0.5} Is it half opened?!{w=0.5} Oh god.{w=0.2}.{w=0.2}.{w=0.2} I think he might have already gotten out...{/i}"

    p "{i}Damn it!{w=0.5} I didn't reach him in time!{w=0.5} I hope that doesn't bring much trouble to our world.{/i}"

    p "{i}At least I got out of that nightmare.{w=0.2}.{w=0.2}.{w=0.2} AND I got the chip,{w=0.2} so that's a plus...{/i}"

label chapter_XVI_chip:

    # Int. Player's house. Night

    p "\"three families have mysteriously disappeared in their homes in Bay Meadows Avenue..."

    p "...undergoing investigation due to unsolved mysteries..."

    p "...seven bodies found in two houses near the old Coppertale Mall...\""

    p "{i}Oh dear god.{w=0.2}.{w=0.2}.{w=0.2} what have I done?{/i}"

    p "{i}I can't believe I might have just opened a hole for our demise just to add another thing to my collection...{/i}"

    scene black
    with fade

    "The end."

    return

label chapter_XVI_vent:

    # player sees the newspaper boy entering the vent

    p "HEY!{w=0.5} You tricked me,{w=0.2} you bastard!"

    show newspaper boy
    with dissolve

    n "Yeah so?{w=0.5} What were you expecting?{w=0.5} Did you really think I would ever believe you?"

    menu:

        "Try to gain his trust again by pretending you are sticking to the plan.":

            jump chapter_XVI_pretend

        "Try and trick the newspaper boy to leave the vent.":

            jump chapter_XVI_trick

label chapter_XVI_pretend:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "We had a plan!{w=0.5} You are gonna make us both get caught!"

    $ newspaper_boy_rel += 1

    $ relationship = newspaper_boy_rel

    n "No!{w=0.5} YOU had a plan!{w=0.5} I just followed YOUR instructions!{w=0.5} Why can't I be the one to leave first?!{w=0.5} It isn't that hard anyways!"

    hide screen relationships
    with dissolve

    n "If you are really against us being stuck here like slaves,{w=0.2} come with me and let's leave together!{w=0.5} They will never catch up to us!"

    p "They'll notice your absence!{w=0.5} I mean,{w=0.2} you are pretty much the face of his mall!{w=0.5} Everybody knows you!"

    n "AND I DON'T CARE!{w=0.5} I'M NOT GOING BACK!{w=0.5} I TOLD YOU I WOULD AVENGE MY BROTHER..."

    jump chapter_XVI_guard

label chapter_XVI_trick:

    $ relationship = newspaper_boy_rel

    show screen relationships

    p "That's also the wrong vent!{w=0.5} I've seen the blueprint again,{w=0.2} and it's definitely in another store!"

    $ newspaper_boy_rel -= 1

    $ relationship = newspaper_boy_rel

    if newspaper_boy_rel <= 0:

        n "Seen?{w=0.5} What do you mean by that?"

        hide screen relationships
        with dissolve

        p "..."

        p "Ahm.{w=0.2}.{w=0.2}.{w=0.2} I mean.{w=0.2}.{w=0.2}.{w=0.2} sense!"

        n "..."

        n "You fool.{w=0.5} I had my doubts there for a second,{w=0.2} but I'm sure now.{w=0.2}.{w=0.2}.{w=0.2} you damn filthy.{w=0.2}.{w=0.2}.{w=0.2} HUMAN!"

        # Newspaper boy proceeds to drain the Player

        # Gameover

        return
    
    n "NO IT ISN'T!"

    hide screen relationships
    with dissolve

    n "I SENSED IT AS WELL AND THERE WERE NO DOUBTS ABOUT IT,{w=0.2} AND THIS IS CLEARLY AN EXIT..."

    p "Ok ok.{w=0.5} Keep your voice down.{w=0.2}.{w=0.2}.{w=0.2} People will hear us..."

    n "...DON'T TRY TO FOOL ME!{w=0.5} WHAT DO..."

label chapter_XVI_guard:

    p "Hey.{w=0.2}.{w=0.2}.{w=0.2} Lower your voice.{w=0.2}.{w=0.2}.{w=0.2} You're gonna get us both in trouble!"

    n "I'M GETTING OUT OF HERE!{w=0.5} AND THERE IS NOTHING..."

    # Security Guard appears
    show security guard at right
    with dissolve

    s "HEY!{w=0.5} I knew you were trying to get away someday!{w=0.5} Unlucky for you,{w=0.2} I'm the guard here."

    n "AAHHHH..."

    n "..."

    # starts draining NPBoy

    hide newspaper boy
    with fade

    p "{i}HOLY CRAP!{/i}"

    menu:

        "Try to run past them and escape through the vents":

            jump chapter_XVI_escape

        "Try and talk your way out of it.":

            jump chapter_XVI_talk

        "Try to hide from the Security Guard":

            jump chapter_XVI_hide

label chapter_XVI_escape:

    "..."

    s "Hey you!{w=0.5} Get back here!"

    p "{i}No [name].{w=0.5} Do not go back.{w=0.5} Do not LOOK back.{w=0.5} Don't even think of the word back right now!{w=0.5} Just keep running until you see an exit or you die of exhaustion!{w=0.5} Nothing else!{/i}"

    "..."

    "The vent door breaks."

    p "{i}arrgh ah.{w=0.2}.{w=0.2}.{w=0.2} ah?!{w=0.5} what?!{w=0.5} Where am I.{w=0.2}.{w=0.2}.{w=0.2} Am I.{w=0.2}.{w=0.2}.{w=0.2} YES!{w=0.5} OH MY GOD YES!{w=0.5} I MANAGED TO GET OUT OF THERE!!!{/i}"

    "Congratulations!{w=0.5} You got out!"

    "The end"

    return

label chapter_XVI_talk:

    p "Oh,{w=0.2} thank god you got him!{w=0.5} I really thought he was gonna escape there!{w=0.5} I'm glad I stopped him until you got here or things could have turned out for the worse."

    s "Do you really think I couldn't sense you back there?{w=0.5} I can sense fear and lies from a mile away.{w=0.5} I know all its ins and outs,{w=0.2} secrets and paths,{w=0.2} shadows and intruders..."

    s "..."

    s "I didn't seal this vent on purpose in case smartheads like you tried something like this..."

    "Gameover."

    return

label chapter_XVI_hide:

    p "{i}Oh god oh god god{/i}"

    p "{i}This guy is a true maniac!{w=0.5} What can I do...?!{/i}"

    p "{i}...{/i}"

    s "I can't believe you just tried to hide from me.{w=0.2}.{w=0.2}.{w=0.2} We can SENSE things you foolish {b}person{/b}."

    "Gameover."

    return

label gameover:

    p "Oh,{w=0.2} I took too much time!"

    s "HEY!"

    "Gameover"

    return

# Image button
screen newspaper:
    imagebutton:
        xpos 0.25
        ypos 0.15
        idle "images/newspaper.png"

        action Jump("chapter_IV_newspaper")

screen letter:
    imagebutton:
        xpos 0.05
        ypos -0.01
        idle "images/letter.png"

        action Jump("chapter_III_letter")