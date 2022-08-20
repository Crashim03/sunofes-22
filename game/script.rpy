# Characters

define n = Character("{b}Newspaper Boy{/b}", color="#ffffff")
define uk = Character("{b}???{/b}", color="#ffffff")
define p = Character("{b}[name]{/b}", color="#ffffff")
define m = Character("{b}Matthew{/b}", color="#ffffff")
define v1 = Character("{b}Voice 1{/b}", color="#ffffff")
define v2 = Character("{b}Voice 2{/b}", color="#ffffff")
define j = Character("{b}Janitor{/b}", color="#ffffff")
define b = Character("{b}Barman{/b}", color="#ffffff")

# The game starts here.
label start:

    # Variables
    $ escalator_tries = 0
    $ dark_hallway_tries = 0
    $ merry_go_round_tries = 0

    # Relationships
    $ newspaper_boy_rel = 3
    $ barman_rel = 3

    $ asked_drinks = False
    $ lucky_shadow = False

    stop sound
    stop music fadeout 2.0

label chapter_I:

    # A maneira como se pergunta o nome do jogo tem que ser melhorada
    python:

        name = renpy.input("What's your name?")

        name = name.strip()

    # Int. Cafe. Daytime.
 
    p "Hey Matthew!{w=0.5} Glad you called.{w=0.5} Is everything okay?"

    m "Yes,{w=0.2} it's all good!{w=0.5} I actually called because of the {b}chip{/b} you're looking for."

    p "Oh!"
    
    p "I hope you have some good news for me!"

    p "I'm starting to feel like a very unlucky person in general."

    p "I've been looking for one to replace in my {b}arcade{/b} for far too long now."

    m "Well,{w=0.2} I've been searching on several websites and second-hand shops and still nothing."

    m "I even set aside some time to dig into the arcade model itself and I'm afraid to break it to you that it hasn't been produced since 1971,{w=0.2} which makes it a lot harder to find that chip than it already is."

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

    p "Ahmm... did you try going into that arcade-themed cafe in the mall?{w=0.5} I heard they have some pretty rare arcades."

    m "Yes,{w=0.2} I did!{w=0.5} I went to a bunch of malls actually!"

    p "Okay okay,{w=0.2} I believe you!"

    p "I think we should wait a couple more days to see if anyone answers the ad."

    p "If not,{w=0.2} I guess I'll give up my arcade."

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

    # Fades to black

    "{b}Coppertale Mall
    11:54 p.m.{/b}"

    # Int. Coppertale Mal- Mall Entry. Night.

    p "{i}This is way different than I recalled.{w=0.5} A lot bigger too.{w=0.5} I hope I can find a way to the arcade.{/i}"

label chapter_II_choice:

    menu:

        "Go foward.":

            jump chapter_II_go_foward

        "Turn right.":

            jump chapter_II_turn_right

label chapter_II_go_foward:

    "..You walk foward.{w=0.5} In front of you is an rundown old escalator that leads into an old food court.{w=0.5} To your left,{w=0.2} there's a dark hallway where you can see a shimmering light in the distance."

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

    "One of the stores to your right is lit with candles.{w=0.5}You get a little bit closer and hear two distinct {b}voices{/b} coming from inside."

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

    # Carta para clicar

    # Aparece carta com texto:

    "Letter:
    To anyone who can read this,

    I don't have much time left, so I'm trying to make this as brief as possible. 
    If you have been hearing and having some strange sights, be aware. These aren't what you are expecting as they're not human and definitely not friendly either. 
    Despite that, DON'T PANIC!{w=0.5} They cannot see you, just hear and feel your presence. If they find out you're a human, your life will be at stake.
    Unfortunately, I've come to discover this too late, but I hope you don't make the same mistakes as me."

    p "{i}Okay this is just too weird for me. I think for now I'll just head back home.{/i}"

    "You turn back to see the newspaper stand."

label chapter_IV:

    # Int. Coppertale Mall - Newspaper Stand. Night. 

    p "I think this is the newspaper stand that I passed through a while ago."

    call screen newspaper

label chapter_IV_newspaper:
    
    # Front page appears

    p "August 3rd,{w=0.2} 12 055."

    p "..."

    p "Why are all of these pictures like this?"

    p "What a bizarre newspaper."

    uk "I know right?"

    # Newspaper boy appears

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

    menu:

        "What do you mean by draining?":

            $ newspaper_boy_rel -= 1

            jump chapter_IV_lose_news

        "How can humans not be a threat?":

            $ newspaper_boy_rel += 1

            jump chapter_IV_gain_news

label chapter_IV_lose_news:

    p "Errm... No.{w=0.5} What do you mean by draining?"

    n "Oh,{w=0.2} you know... consume them."

    p "{i}Consume?{w=0.5} Just like straight up eating us?{w=0.5} Oh,{w=0.2} man,{w=0.2} don't tell me that letter was right when it talked about my life being at stake.{/i}"

    p "Ah,{w=0.2} I- I see what you mean..."

    n "I sense you're slightly nervous,{w=0.2} pal... Are you okay?"

    p "Yeah yeah I'm okay!"

    p "Just had a rough day you know?"

    n "Right..."

    n "Well,{w=0.2} as I was saying,{w=0.2} it's by locking us in that most of us are not aware of our potential."

    n "We are being restrained by ourselves... Perpetually afraid and ignorant,{w=0.2} while humans are freely roaming around."

    n "But I'm not gonna succumb to this sort of mindset!"

    n "You'll see,{w=0.2} one of these days,{w=0.2} I'll find a way around that {b}guard in the main entrance{/b} and I'll reach the outside..."

    p "{i}I think he was a bit suspicious about my question and I don't want to find out what being drain actually feels like.{/i}"

    p "{i}Better be more cautious next time.{/i}"

label chapter_IV_gain_news:

    p "Hmm... No.{w=0.5} How can humans not be a threat?{w=0.5} I heard they took out 30 of our own..."

    n "What about the incident in the {b}old mansion{/b}?!{w=0.5} I think everyone is making that a bigger fuss than it is."

    n "Of course there are always gonna be dangers,{w=0.2} especially when they come in packs,{w=0.2} but that doesn't mean that we can't easily take them down."

    p "And how come humans become a threat when they're in packs?"

    n "Think with me,{w=0.2} pal."

    n "Their presence makes us weaker,{w=0.2} makes us fade from existence as we are shadows and they are conscious living beings.{w=0.5} Therefore,{w=0.2} we can't coexist."

    n "However,{w=0.2} I think that only happens when there's a stronger presence.{w=0.5} That's why it's harder for us to notice them if they're alone and need to be careful about any intruders."

    p "{i}Damn it,{w=0.2} I'm so screwed!{/i}"

    p "{i}At least my presence is not strong enough for him to sense I'm a human,{w=0.2} so I don't think he's suspicious about me.{/i}"

    n "We emerge and thrive in abandoned places.{w=0.5} When they start being inhabited again we just cease to exist."

    n "That's what happened in the old mansion,{w=0.2} but then again,{w=0.2} I think we're individually stronger.{w=0.5} So we could easily avoid these types of incidents if we're just smart about it instead of reinforcing security."

    n "I've encountered one and I'm perfectly fine... But I can't say the same for him.{w=0.5} Ha ha ha ha."

    p "Ha ha ha..."

    p "{i}WHAT DOES HE MEAN HE CAN'T SAY THE SAME FOR HIM?!{w=0.5} DID HE KILL HIM?{/i}"

    p "{i}Oh man,{w=0.2} I should really get out of here as quickly as possible.{w=0.5} In and out,{w=0.2} without raising suspicion.{/i}"

    n "I swear to you,{w=0.2} pal... one day I will try to get out of this rathole and be free!{w=0.5} Just like my brother always wanted..."

    n "My brother... my poor brother... you remind me of him... he also was very shy and quiet like you... until that DAMN SECURITY GUARD took him out just because he had hopes bigger than ours..."

    n "You'll see... that security won't even see what's coming for him!"

label chapter_IV_person:

    p "{i}Is that a person I'm seeing?{w=0.5} Finally,{w=0.2} I might have found a way out of this place!{/i}"

    p "{i}Maybe he's as lost as I am and we can work together to get out of here.{w=0.5} Or,{w=0.2} at least,{w=0.2} we can make some sense of what is going on here!{/i}"

    p "Excuse me,{w=0.2} I really need to go now."

    n "Are you going to buy that newspaper?"

    p "Hmm,{w=0.2} I'm sorry.{w=0.5} I don't have any cash on me."

    $ newspaper_boy_rel -= 1

    n "yeah... Right!"

label chapter_V:

    # Int. Mall Entry. Night.

    # (An old janitor appears)

    p "Finally!{w=0.5} A human!"

    j "Hello,{w=0.2} sir,{w=0.2} may I help you with anything?"

    p "Yes!"

    p "Please do you know what's going on here?{w=0.5} What are these shadowy -... thingies?{w=0.5} Can they really kill us?!"

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

    # janitor smiles

    # janitor disappears

    p "{i}How can he be here for that long?{w=0.5} And they've never noticed him?!{w=0.5} This is a heck of a situation.{/i}"

    p "{i}These creatures are traces of a long gone human presence,{w=0.2} but they coexist with us because we bring liveliness to places.{/i}"

label chapter_VI:

    # Int. Coppertale Mall - Exit Bar (exterior). Night

    # (A door with a big Exit sign appears)

    p "This has got to be it!{w=0.5} And no security guard to be seen.{w=0.5} Good to know!"

    p "I'm so relieved to finally get out in one piec-"

label chapter_VII:

    # Int. Coppertale Mall - Exit Bar (interior). Night

    # (One the other side of that door there’s a bar. In the center is a shadow which is the Barman.)

    b "Welcome to the Exit Bar!{w=0.5} Can I get you anything?"

    p "{i}That freaking janitor.{/i}"

    p "{i}Relax.{w=0.5} Just talk to him.{w=0.5} Casual,{w=0.2} normal,{w=0.2} you're just a regular customer,{w=0.2} [name].{w=0.5} You can talk your way through this.{/i}"

    b "..."

    p "..."

    b "Hello?"

    p "Sorry.{w=0.5} Can you repeat that?"

    b "Oh,{w=0.2} I {b}sensed{/b} you were new here.{w=0.5} We serve beer,{w=0.2} margarita,{w=0.2} whiskey sour,{w=0.2}...?{w=0.5} What are we having today?"

    menu:

        "I'll have a beer.":

            $ barman_rel += 1
            $ asked_drinks = True

            jump chapter_VII_beer

        "Do you serve martinis?":

            $ barman_rel += 1
            $ asked_drinks = True

            jump chapter_VII_martini

        "I'm good,{w=0.2} thanks.":

            $ barman_rel -= 1

            jump chapter_VII_nothing

label chapter_VII_beer:

    p "I'll have a beer."

    b "You are my kind of guy!{w=0.5} The classic never fails!"

    jump chapter_VII_conversation

label chapter_VII_martini:

    p "Do you serve martinis?"

    b "Of course I do.{w=0.5} Just one?"

    p "Yes please."

    jump chapter_VII_conversation

label chapter_VII_nothing:

    p "I'm good,{w=0.2} thanks."

    b "Okay... so,{w=0.2} are you coming to meet some friends?{w=0.5} Or did you come by mistake?"

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

    b "What about you?{w=0.5} What do you do Mr... I'm sorry,{w=0.2} what's your name again?"

    menu:

        "I'm [name],{w=0.2} a not so lucky shadow.":

            barman_rel += 1

            lucky_shadow = True

            jump chapter_VII_not_lucky

        "I'm [name],{w=0.2} an ophthalmologist":

            barman_rel -= 1

            jump chapter_VII_ophtal

label chapter_VII_not_lucky:

    p "I haven't said it.{w=0.5} I'm [name].{w=0.5} a not so lucky -... shadow."

    b "ha ha ha,{w=0.2} then let me tell you my secret.{w=0.5} Shadows say I'm lucky,{w=0.2} but in reality I'm just very optimistic."

    b "It's my motto.{w=0.5} “No matter what situation you're in,{w=0.2} there's always a way to win.” There's always an upside.{w=0.5} And THAT's where you should focus on."

    b "For example:"

    b "During the first couple of years,{w=0.2} after I opened this bar,{w=0.2} I had to sleep on this very floor.{w=0.5} I honestly had no hopes of a better tomorrow,{w=0.2} but I just persevered,{w=0.2} you know?"

    b "Now,{w=0.2} here I am!{w=0.5} Just living the dream!{w=0.5} Hanging out everyday with the drunks!{w=0.5} I always knew this was meant for me!{w=0.5} I always knew I wanted to serve drinks for a living.{w=0.5} haha."

    if asked_drinks:

        b "Speaking of the devil,{w=0.2} here's yours!"

        p "Thank you."

    p "I understand that,{w=0.2} but sometimes I just feel like I tried just about everything... not only for me,{w=0.2} but for my son as well."
    
    p "I even find myself {b}where I don't belong{/b} sometimes,{w=0.2} you know?{w=0.5} There's -"

    jump chapter_VII_beers_fall

label chapter_VII_ophtal:

    b "An ophthalmologist?{w=0.5} What is that?"

    p "An eye care specialist."

    b "Eye?"

    p "{i}Damn it!{w=0.5} I fucked up already.{/i}" 
    
    p "It's just a fancy way of saying I help people... through... their... senses..."

    b "..."

    jump chapter_VII_beers_fall

label chapter_VII_beers_fall:

    # noise of beers falling

    b "Oh god damn it!{w=0.5} What a damn mess!"

    b "Look,{w=0.2} sorry if this is asking too much,{w=0.2} but do you think you could go outside and get me the janitor?"

    b "I just have a lot on my plate right now and I think you are the only one here who can still walk in a straight line."
    
    p "Yeah yeah,{w=0.2} no worries."

    # black screen

    if lucky_shadow:

        p "{i}Phew!{w=0.5} Well... he seems nice!{w=0.5} Still scared... for my life!{w=0.5} But I think I'm doing okay.{/i}"

        p "{i}Maybe when I come back I can get him to tell me where I can get out of this hell hole.{/i}"
    
    else:

        p "{i}God freaking dammit!{w=0.5} I was too suspicious!{w=0.5} If it wasn't for those beers dropping,{w=0.2} I would be so screwed!{/i}"

label chapter_VIII:

    # Int. Coppertale Mall - Mall entry. Night

    p "Excuse me,{w=0.2} sir?"

    j "Hello,{w=0.2} sir,{w=0.2} may I help you with anything?"

    p "Hello again."

    j "Oh,{w=0.2} I remember you.{w=0.5} Did you find the bar you were looking for?"

    p "Well,{w=0.2} kind of,{w=0.2} yes.{w=0.5} Speaking of it,{w=0.2} the bartender,{w=0.2} Lucky,{w=0.2} asked for you."

label chapter_IX:

    # Int. Coppertale Mall - Exit Bar. Night

    p "We're here!"

    b "Thank you,{w=0.2} [name]."

    b "Hmm... I'm sensing something off... Do you feel that...like something eerie?{w=0.5} Or is it just me?"

    p "{i}I completely forgot that we can't have a strong presence,{w=0.2} otherwise they'll notice we're humans.{/i}"

    menu:

        "No,{w=0.2} I don't feel anything."

            barman_rel += 1

            jump chapter_IX_dont_feel

        "Yes,{w=0.2} I do feel a little something."

            barman_rel -= 1

            jump chapter_IX_feel

label chapter_IX_dont_feel:

    p "No,{w=0.2} I don't feel anything.{w=0.5} What about you... hm... Mr... Janitor?{w=0.5} Do you feel anything?"

    # suspanse

    j "I do,{w=0.2} actually... I sense... beer!{w=0.5} I'll go ahead and clean it up."

    b "Right!{w=0.5} Almost forgot about that.{w=0.5} Thank you again [name] for the help!"

    b "However I can repay you,{w=0.2} just say the word.{w=0.5} Drinks tonight are on the house!"

    jump chapter_IX_goodbye

label chapter_IX_feel:

    p "Yes,{w=0.2} I do feel a little something.{w=0.5} If you ask me,{w=0.2} I think it's coming from those shadows in the back..."

    j "No,{w=0.2} people always tell me that.{w=0.5} It's probably because they {b}sense{/b} we're two most good-looking individuals around the block."

    p "{i}The fact that this guy hasn't died yet is a complete mystery to me!{/i}"

    b "It's definitely coming from around here and it's making me feel a bit nauseated."

    b "Nevertheless,{w=0.2} do you think you could clean up that mess next to the jukebox?"

    j "Sure will boss!{w=0.5} On it."

    b "Thank you again [player] for the help!{w=0.5} However I can repay you,{w=0.2} just say the word."

label chapter_IX_goodbye:

    if barman_rel <= 0:

        b "Hey,{w=0.2} now that's just the two of us.{w=0.5} I need to tell you a couple of words."

        b "..."

        b "Humans are not welcome here."

        p "...Humans?{w=0.5} I don't know what you mean."

        b "Don't try to fool me."

        b "Just be glad I'm the one finding it out.{w=0.5} Others won't be so forgiving,{w=0.2} so I'd strongly advise you not to give yourself away that easily or you'll never get out of here intact."

        b "I've been able to get old Jimmy “janitor” there off the hook a couple of times now,{w=0.2} but he's not getting any younger,{w=0.2} or smarter."

        b "What I'm saying is: I'm already putting myself at risk here,{w=0.2} but I'm not gonna take a bullet for you."

        b "Don't get me wrong.{w=0.5} You're a nice kid,{w=0.2} but the moment the shadows find out you're a human,{w=0.2} they are definitely gonna take you as a threat."

        b "So just... be careful out there!"

    p "Thanks."

    p "Anyways I can't stay here much longer."

    b "Already?{w=0.5} But you just got here."

    p "Yeah I know,{w=0.2} but you COULD help me with something else if you're willing."

    b "What is it."

    p "When I got here,{w=0.2} I was actually looking for an outside exit,{w=0.2} not the Exit Bar.{w=0.5} Do you,{w=0.2} for any reason,{w=0.2} know one?"

    p "I know the main entrance is protected by a guard,{w=0.2} and they are planning to reinforce security."

    b "..."

    b "Well kid... not gonna lie to you.{w=0.5} Nobody has gone out there for years now."

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

label chapter_X:

    # Int. Coppertale Mall - Newspaper Stand. Night.

    p "Hello again."

    n "Hey."

    n "Are you looking for something specific I can help you with?"

    p "Yes,{w=0.2} actually."

    menu:

        "Trick the newspaper boy to giving you the information.":

            newspaper_boy_rel += 1

            jump chapter_X_trick

        "Agree with Newspaperboy's ideologies in order to give to the information."

            newspaper_boy_rel += 1
            
            jump chapter_X_agree

label chapter_X_trick:

    p "Sorry for leaving so abruptly,{w=0.2} you were in the  middle of the story of your brother..."

    n "Why do you care?!"

    p "Well,{w=0.2} you said something about the security guard taking out your brother... How did he find out your brother was leaving?"

    n "You see,{w=0.2} my brother was always smart,{w=0.2} but not very cautious... The day he planned his escape,{w=0.2} he was followed by the guard until one of the vents."

    p "I see..."

    n "They then proceeded to publicly drain him so the community saw what would happen if anybody else tried to escape."

    n "To this day I still have nightmares about that night..."

    p "And you said you were planning something against that security guard... how so?"

    n "That mall entrance security guard was the damn bastard who sentenced my brother."

    n "I WILL make him pay.{w=0.5} But I can only do that when I have a way out of this place where I can get out!"

    p "Do you think there are any other exits?"

    n "The only thing I know for certain is this: there has GOT TO BE another exit.{w=0.5} The vents on this mall are way bigger than they look."

    n "After my brother's escape,{w=0.2} the security around that area got a lot less supervised because they sealed it pretty well,{w=0.2} and discarded any other possible exits through the vents."

    p "And how can you know where the other exits are?"

    n "Now THAT is the big problem I'm still trying to solve.{w=0.5} The vents of the mall are all registered in its blueprints,{w=0.2} which are located in the security guard's control room."

    n "Problem is: The guard is trained to sense from very far away so he can easily feel anyone just by getting near the room."

    n "Plus,{w=0.2} after getting in,{w=0.2} we would still need some time to unlock the safe where the prints are,{w=0.2} which is very impossible due to the fact the security guard doesn't go farther than a 45-60 seconds distance from the room."

    n "So yeah,{w=0.2} that's the biggest challenge to get through.{w=0.5} But as I said: one day I WILL find a way and get the hell out of this rat hole!"

    p "What a hell of a story... I sincerely wish you the best of luck finding a way!"

    n "Cheers bud!"

    n "Besides that,{w=0.2} can I help you with anything else?{w=0.5} Maybe you finally brought that cash you needed... haha"

    p "No,{w=0.2} thanks anyway though!"

label chapter_X_agree:

    p "What you said about us not reaching our full potential got me thinking..."

    n "I knew you weren't brainless like most."

    p "Yeah,{w=0.2} thank you for enlightening me."

    p "Humans are in fact no danger to us and still we're hiding out here.{w=0.5} It's an absurdity!"

    n "That's what I always say.{w=0.5} Security reinforcement doesn't protect us,{w=0.2} it protects them."

    n "If more shadows would have listened to me,{w=0.2} we would be outside by now... free to go wherever we like... to drain whoever we want.{w=0.5} Not enclosed in this ugly ass concrete box."

    p "{i}Oh,{w=0.2} boy,{w=0.2} what am I putting myself into?!{/i}"

    p "Agreed!"

    p "...They should be afraid of us,{w=0.2} not the other way around!{w=0.5} I think I'm trying to get out of here,{w=0.2} just like your brother."

    n "I don't know if that's a good idea..."

    p "I've got nothing to lose... But I need your help if I want to succeed."

    p "Once I'm out,{w=0.2} it's easier to help you escape.{w=0.5} They won't ever believe I'll be heading back to get you."

    n "Really?!{w=0.5} Would you do that for me?"

    p "Of course!"

    p "If you help me,{w=0.2} I'll help you.{w=0.5} It's for a common cause my friend!"

    p "{i}Please believe me.{/i}"

    n "Hmm..."

    n "It would be very risky... but I think there's a blueprint of the mall with all of its vents registered."

    n "They might be our only way out.{w=0.5} After my brother tried to go through one... they sealed it,{w=0.2} but for all I know,{w=0.2} that's the only one they've taken care of."

    n "Problem is: the blueprint is in the security guard's control room."

    p "Do you think I can take it without him noticing?"

    n "It's very unlikely... but not impossible."

    n "He usually walks around the mall entry and it takes him more or less 45 seconds to a minute to go from his room,{w=0.2} around the entrance,{w=0.2} and back."

    n "So,{w=0.2} you need to be quick."

    p "Alright."

    p "I'll try not to get drained haha."

label chapter_XI:

    # Int. Coppertale Mall - Control Room. Night

    p "{i}I think this is it!{/i}"

# Image button
screen newspaper:
    imagebutton:
        xpos 0.25
        ypos 0.15
        idle "images/newspaper.jpg"

        action Jump("chapter_IV_newspaper")