# Splash screen and story script.

# Declare images below this line using the image statement.
image black = "#000000"
# image school = "school.png"
# image st_john = "st_john.png"
image st_john_north = "images/crossing.jpg"
image north_isle_school = "images/high-school.jpg"
image north_isle_classroom = "images/classroom.jpg"
image st_john_school = "images/school.png"
# image academy_pacific = "academy_pacific.png"
# image city = "city.png"
# image capial = "capital.png"
# image island = "island.png"

image juni smile = "images/barkley.png"

image jazz smile = "images/jazz_smile.png"
image jazz beam = "images/jazz_smile_less.png"
image jazz = im.FactorScale("images/jazz_test.png", .29, .29)
image jazz neutral = im.FactorScale("images/jazz_neutral.png", .29, .29)
image jazz neutral talk = im.FactorScale("images/jazz_ntrltalk.png", .29, .29)
image jazz cheeky = im.FactorScale("images/jazz_cheeky.png", .29, .29)
image jazz serious = im.FactorScale("images/jazz_seriuos.png", .29, .29)
image jazz serious talk = im.FactorScale("images/jazz_srstalk.png", .29, .29)

image ryan = "images/barkley.png"
image kevin = "images/jordan.png"

# Declare characters used by this game.
define U = Character("Juni", color="#ff0000")
define Z = Character("Jazz", color="#ffcccc")
define E = Character("Jase", color="#0000ff")
define C = Character("Mark", color="#ccccff")
define S = Character("Savan")
define R = Character("Ryan")
define K = Character("Kevin")
define A = Character("Audrey")

define jase = E
define juni = U
define mark = C
define jazz = Z

define n = Character(None, kind=nvl)

define typo = Character("TYPO HERE?", color="#ff0000")


# Add a splashscreen: http://www.renpy.org/wiki/renpy/doc/cookbook/Adding_a_Splashscreen
# Something with Studio Storian logo or whatever. Perhaps move the "SS presents" to the first start
label splashscreen:
    scene black
    with Pause(1)

    show text "studio STORIAN presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# Lead in to title. Ambient rain, backdrop of hillside city, show "raindrops" logo.
# 	Two silhouettes, boy and girl facing away from e/o. Maybe make the characters pop up
#   after pressing start?

# Title menu. Styling goes in options.rpy.

# The game starts here.
label start:
    $ jase_complete = False
    $ juni_complete = False
    $ _game_menu_screen = "pause_menu"
    if start_character == "Jase":
        jump jase1
    else:
        jump juni1

label Jase_start:
    $ start_character = "Jase"
    jump start

label Juni_start:
    $ start_character = "Juni"
    jump start

label jase1:
    stop music fadeout 1.0
    play music "sounds/darkcoffee.mp3"
    scene st_john_school
    with fade
    jase "My name is Jase Guo."
    mark "My name's Chad. No, Mark. No, Swiss Chard. I play lacrosse and fuck people up."
    jase "yeah what a dick right"
    "End Jase section."
    $ jase_complete = True
    jump transition


label juni1: # Just another day at North Isle High

    # Begin Day 1 Juni
    # play sound "rain1.mp3" fadein
    stop music fadeout 1.0
    scene black

    "It's raining.{w} As usual."
    play music "sounds/dankcoffee.mp3"
    "{cps=35}I lean back in my chair, put my arms up, and stretch after another long day of classes.{/cps}"

    scene north_isle_classroom
    with dissolve
    # play sound "crowd.mp3" fadein # loop

    "The chatter around me builds up and dies down as my classmates pack their things and head home."
    # scene notebook
    # with dissolve
    "I take another look at my notebook, flipping through what I wrote down during Mr.
    Schumacher's lecture today."
    "We'll be doing a practice essay question on the Protestant Reformation later this week,
    so I need to make sure I understand everything he covered."
    "To my right, Mr. Schumacher is still talking to two other students about
    the reasons behind the creation of the Anglican Church."
    "Judging from how antsy they're getting, I don't think they realized what they were in for."
    "As the last of the students leave, Jazz appears in the doorway."
    stop music fadeout 1.0

    # stop sound "crowd.mp3" fadeout
    # play sound "footsteps.mp3" fadein
    # show jazz smile
    show jazz at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
        # linear 1.0 xalign 0.2
    # with dissolve

    Z "Hey Juni!"

    # show juni smile

    U "Hi Jazz. How was the chemistry quiz?"
    Z "Mmm, not too bad. The hardest part was the ion balancing, and that was just
    because she didn't give us the periodic table."

    # another juni smile????
    U "Ha, that's too bad. I'm sure they'll give it to you on the test-"

    # play sound "footsteps.mp3" fadein

    "As the last two students narrowly escape Mr. Schumacher's neverending lesson on
    King Henry's infidelities, Ryan and Kevin come in."

    hide jazz
    show jazz cheeky at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
    Z "Hey you two! Good job remembering to come to practice today. I thought I was going
    to have to track you down again like last week."

    "Ryan beams back at Jazz while Kevin tilts his head sheepishly.
    I'm glad Ryan has already learned how to deal with Jazz, but it looks like Kevin
    might need a little more time to settle in."

    hide jazz cheeky
    show ryan at Position(xpos=0.7, xanchor=0.5, ypos=0.5, yanchor=0.5)
    R "Of course! We didn't join Quiz Bowl for nothing, right, Kevin?"
    show kevin at Position(xpos=0.3, xanchor=0.5, ypos=0.5, yanchor=0.5)
    K "What can I say? You and Jazz - sorry, Jasmine - were pretty convincing."
    show jazz neutral
    "As they talk, I remember something."
    # speaker juni smile
    hide ryan
    hide kevin
    U "Oh, right, Jazz. Savan's out sick today."
    U "He told me to let you know to run the meeting as usual, and that you'd know what to do."
    show jazz at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
    Z "Yeah! He messaged me."
    Z "Okay, you two, I hope you've been reading up on Quiz Bowl questions,
    \'cause today we're going to be doing your first-ever live practice!"
    "Ryan lights up even more while it looks like it's taking Kevin everything he has not to
    roll his eyes and groan."
    R "With the buzzer?"
    Z "With the buzzer."

    # 

    "As Ryan pumps his fist with an audible yes, I turn to Mr. Schumacher, who's been
    quietly smirking behind his desk, pretending to grade papers."

    # juni smile

    U "Mr. Schumacher, do you mind if I get the buzzer from your cabinet?"
    "As I dig through his cabinets trying to remember where we left the set last summer,
    Jazz starts assigning the teams."

    show jazz serious talk at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)

    Z "Alright, Ryan, how about you pair up with Kevin, and Juni...{w} you're on your own."
    U "Wait, what? What about you?"

    show jazz neutral at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)

    Z "I'm moderating, of course. Someone has to read the questions if Savan isn't here."

    # juni pout

    U "But, Jazz..."
    Z "Juni, you already know these like the back of your hand. The only way these two
    can win is by having a faster reaction time, and you're pretty good at that, too."
    Z "If anything, Savan would've asked you to handicap yourself anyway."

    # juni surprise nervous sweat
    U "...Mr. Schumacher! Could you read the questions?"
    "He raises his hands and makes the excuse that he's already behind on grading,
    leaving me on my own."
    "Defeated, I hand everyone their buzzers. Jazz takes out her binder full of past
    questions and practice begins."
    Z "First question: How many circles can be tangent to two parallel lines?"
    "Ryan shouts, \"I know!\" but I've already hit the buzzer. I hope I'm not being too hard on them."

    # scene ?

    "The sounds of our lively Quiz Bowl team drift out into the hallway as the rain
    continues on without a care for my walk home."

    # scene black
    # with dissolve
    # stop sounds

label juni2: # Another Passing on the Walk Home

    scene st_john_north
    with fade
    # play sound rain 
    # show jazz cheeky umbrella
    Z "Bye Juni! Careful around puddles!"
    "I stick my tongue out at her. Admittedly, if I did fall into a puddle on the way back it wouldn’t be the first time."
    # show Juni smile
    U "Hpmh! See you tomorrow!"
    "Jazz heads home with the usual spring in her step."
    
    # novel mode
    n "By the time our first practice session was done, the sun was about to set behind the clouds."
    n "I look uphill at the long path home. Maybe I should ask my parents for a bike."
    n "I shake my head. How would I hold an umbrella while riding? Going any faster would mean riding into the rain, too."
    n "With a sigh, I start walking forward."
    nvl clear

    # scene tree-lined intersection
    n "The light dims as I feel the sun drop lower in the sky. I'm a little over halfway home."
    n "Not many students live this way, and the few that do left school before I did. The
    sidewalk is quiet and only the rare car passes by to break up the monotony of the
    neverending rain."
    n "As I make my way forward, I begin to hear the splish-splash of someone running in the
    rain heading in my direction.{w} It must be him again."
    n "I try my best to look forward without looking at him directly. The road is straight for
    a good while here so I have no reason to feel weird about it, but I imagine it would still
    be a bit awkward to be staring at him the entire time."
    nvl clear

    # dialogue mode
    # show jase jog
    # play sound wet jogging, faint
    "As usual, he's wearing a light raincoat but his hood isn't up."
    # show jase jog bigger
    "His head and hair must be soaked."
    # Jase gets closer
    "I can't even begin to imagine living like he does."
    "And yet my curiosity gets the better of me."
    "Just before he passes by, I dart my eyes to get a better look at him."
    # even closer
    "He appears to have the same idea."
    "Our eyes meet for a brief, awkward moment."
    
    # "I blink,"
    # scene black
    # scene st_john_north
    # "{cps=0}I blink, {/cps}and he's gone."
    "I blink,{w} and he's gone." #insert blink animation here.
    
    # novel mode 
    n "I arc my head back and sigh at my umbrella.{w} Why did I do that?"
    nvl clear
    
    n "Continuing my walk home, I start to think back on what I know of him."
    n "These are tracks my mind has worn down for a while now, but going through it again should keep my mind off the rain long enough to get home."
    n "I pass by him about once a week."
    n "His face is familiar but I can't seem to remember his name."
    n "This jogger is on the other school's Quiz Bowl team, but I don't think I can say that we've ever met."
    n "I've seen him occasionally at regional tournaments, but I've never spoken to him directly."
    nvl clear

    # flashback time!

    # scene st_john_north bw
    # with fade
    scene black
    with dissolve
    n "In August, we held a scrimmage with his Quiz Bowl team, the one from the city's Catholic high school."
    # play flashback music
    n "Our upperclassmen had been meaning to do this for years, but it was only when
    Jazz earned her officer position that she finally pushed it through."
    # scene talks
    n "She got in touch with her friend there - I think Audrey was her name.{w}"
    n "Even though she was a year younger than us, she'd been named the president of
    their Quiz Bowl team, a fact I think Jazz was a bit envious of."
    n "From what she explained to me, Audrey herself seemed a bit insecure about it all.{w}
    Eager to prove herself, she and Jazz set up the scrimmage at our high school."
    nvl clear
    # new page

    # scene north_isle_classroom bw
    n "Because it was summer, our upperclassmen had graduated and our team hadn't yet been able to recruit Ryan and Kevin, so it was only me, Jazz, and Savan."
    n "They were in a similar predicament, with only Audrey, him, and a third person on their team."
    n "I remember him being a bit hesitant to sit as a team member, making the excuse that
    he was only supposed to be the alternate.{w} I found this strange because he was clearly the oldest one on their team."
    n "After I dug out the same buzzer we used during practice today, we took our seats. Savan had asked another friend to moderate, and so the game began."
    nvl clear

    n "For the reaction-time buzzer-beater questions, we were about evenly matched,
    but not entirely because we were equally skilled."
    n "To my surprise, the jogger didn't even pick up his buzzer.{w} Instead, he leaned back and stared off into space,
    seemingly in deep concentration yet producing no results."
    n "At first, I thought that was dead weight to their team, but I was forced to
    reconsider when they won the opportunity to answer their first bonus question, the
    ones with no time pressure."
    n "I don't remember what the question was, but I do remember what he did."
    nvl clear

    n "Instead of going straight for it like I expected them to, Audrey and the other
    person turned to him and he just started talking.{w} Reasoning."
    n "Whatever the question was, he began to explain everything, in meticulous detail.{w}
    He laid out each possible answer he came up with, and a thorough case of pros and cons
    for each choice."
    nvl clear

    n "All in all, he gave his team around five options and spent enough time on each decision
    to bore our team and the moderator to near tears."
    n "It was clear that he hadn't studied the material as hard as, say, Savan or I did,
    but his reasoning more than made up for it."
    n "Jazz, Savan, and I exchanged a look as Audrey, after double-checking with their
    third member, chose what she decided was the strongest option the jogger offered as
    their answer for the moderator."
    n "She also asked the jogger what he thought, but instead of picking any of his
    choices, all he could do was shrug.{w} Absolutely baffling."
    n "And yet, as we knew, they were right."
    nvl clear

    n "This continued for the rest of the scrimmage. Although we were evenly matched for
    the buzzer questions, we were outperformed on the bonus questions thanks to him, and
    St. John's Academy of Religious Studies won our first interscholastic scrimmage."
    n "What a curious character."
    nvl clear

    # scene juni house
    n "As I climb up the steps to my house, I shake my head."
    n "I can't even begin to imagine what he's thinking."
    nvl clear

    scene black
    with dissolve

label juni3: # Lacklovester Afternoon
    # scene class
    # play sound heavy rain
    n "After another day of class, Jazz and I find ourselves in Mr. Schumacher’s room again, even though we don’t have practice."
    n "Savan’s back today, too."
    n "(I have a sneaking suspicion that he wasn’t sick yesterday either, but I’ll keep it to myself.)"
    n "More often than not, we spend time in Mr. Schumacher’s room after school, waiting for the rain to let up before we start heading home."
    n "Before they graduated, our upperclassmen in Quiz Bowl did the same thing, and I guess we picked it up from them."
    nvl clear

    R "Heyo!"
    "As if to punctuate my thought, Ryan pokes his head in the door."
    show jazz smile
    Z "No Kevin today?"
    R "Like I said, it’s hard enough to get him to come to practice. No way in hell could I convince him to hang out here."
    "Mr. Schumacher had already left to coach the weightlifting team, leaving us in charge of his room.{w} Following school regulations, he had locked the door, so we propped it open in case anyone wanted to visit or drop something off for him.{w} Sure enough, someone did."
    S "What brings you here today, uh—"
    U "Ryan."
    S "Right, Ryan."
    #hide jazz smile
    #show jazz annoyed
    "Jazz stands up and leans over her desk to berate Savan."
    Z "Come on, Savan, he and Kevin have been in the club for a month now. Is the president knowing the names of our two new members too much to ask?"
    "Savan, laid-back as ever, just tilts his head and shrugs."
    S "What can I say? I’m bad with names, you know."
    R "It’s okay Jazz, I don’t really mind. We’ve only had, like, three meetings so far, right?"
label juni31:
    "Begrudgingly, Jazz drops back in her seat."
    R "That reminds me — all three of you are seniors, so what was the club like before I joined?"
    #hide jazz annoyed
    #show jazz thoughtful
    #show juni thoughtful
    "The three of us think for a bit."
    S "Well, I don’t think it was much different from now, you know?"
    U "Quiz Bowl has always been a very small and tight-knit club."
    Z "In fact, we usually don’t recruit, but after two of us graduated last year, we had to step it up or be at a disadvantage for competition."
    R "Really? What were they like?"
    U "Well…"
    "The conversation goes on in much the same fashion as the rain continues hitting the classroom windows. Showing no signs of letting up, our conversation drifts from team history to—"
    #hide juni thoughtful
    #hide jazz thoughtful
    #show jazz surprised
    Z "Me? No way!"
    S "Ha. Don’t get ahead of yourself, kid. She may not look it, Jazz has absolutely zero experience with relationships."
    #hide jazz surprised
    #show jazz glare
    Z "I will {i}kill{/i} you."
    "As Jazz and Savan sass each other, Ryan and I share a look."
    "Someone unkind and uncreative would probably describe these two as an old married couple.{w} I’d say they’re more like brother and sister."
    S "Well, is it not objective truth that you’ve never been in a relationship?"
    #hide jazz glare
    #show jazz pout
    Z "Well, yes..."
    "Turning back to Ryan, Savan says,"
    S "So now your question would be why, right?"
    "Ryan nods eagerly, oblivious to the trouble brewing in front of him."
    S "If I had to guess, it’s because of her standards."
    #hide jazz pout
    #show jazz serious
    "Jazz goes silent as I sense imminent danger."
    S "Because of her competitive streak, not only does he have to be handsome and well built, he also has to be just as talented {i}but no more than Jazz is{/i} in academics and music."
    S "Likewise, his college and career prospects have to be just as good as, but no better than hers."
    "Wait, no, stop, you’re hitting too close to home!"
    S "We’re only in high school, and yet she’s already looking for a committed life partner when most guys just want to touch the goods."
    "I try to get Savan’s attention, mouthing “nonono” at him over and over."
    S "Needless to say, there’s no one in this school that fits these far too specific requirements, and so Jazz is still single."
    "As Jazz sinks deeper, I frantically wave my hands at Savan trying to get him to cut it out while he still can, but he’s going in for the kill."
    S "Simply put, she’s just far too demanding, y’know?"

    # screen shakes
    # hide jazz serious
    # show jazz exclaim
    Z "You’re wrong you're wrong you're wrong!"
    "Instead of going for Savan this time, Jazz turns to me in a flurry."
    "She hugs,{w} clutches me from the side.{w} Very,{w} very{w} tightly."
    "Near tears, she exclaims,"
    Z "I’m {i}not{/i} single and I’m {i}definitely not{/i} too demanding!"
    Z "Juni is the only one for me! No one can separate our love!"
    # hide jazz exclaim
    # show jazz hug
    "Inside her iron grip, I smile genuinely and laugh nervously.{w} I’m glad she feels (and grabs) so strongly but I don’t think I can reciprocate."
    "After a few moments, Jazz breaks and gives Ryan another one of her cheeky looks before letting go and recomposing herself."
    "She was joking.{w} Probably."
    S "Well, you know, despite her appearance, Juni is surprisingly popular too."
    "Hey!"
    # hide jazz hug
    # show jazz glare
    Z "You have a death wish, don’t you?"
    "Savan raises his palms up to protect his face, smirking the entire time."
    S "I don’t know, maybe they find her perpetual bedhead cute?"
    # SCN: Juni disapproving
    # SCN: Juni looking up cute
    "As Jazz gets up to punish Savan some more, I paw at one of my unkempt locks."
    "It’s more that, no matter how much time I spend on it in the morning, my hair and the weather refuse to get along and, considering the climate, it’s always humid."
    "Meanwhile, Savan squirms his head out of Jazz’s chokehold to respond to Ryan’s quizzical expression."
    S "Juni has rejected her fair share of dates, you know."
    U "I’m telling you, I just don’t like going to dances."
    S "Even if that’s true, you never really returned their interest either, now did you?"
    U "Well…"
    R "So you’ve never been in a relationship either?"
    U "…I guess not. I’ve never really been interested in them."
    "Ryan leans back in his chair, crosses his arms, and shrugs at the ceiling."
    R "Why not?"
    "I’m a bit taken aback at this question, but I should’ve seen it coming. It’s a question I’ve never really thought over."
    U "…I think it would distract me from my classes."
    "But that’s an excuse.{w} Even so, he seems satisfied with my answer."
    R "Well, if you’re ever looking—"
    "With a reaction time that would put an Olympic goalie to shame, Jazz lets go of Savan and pounces on me, hugging me again and stating firmly,"
    Z "No way I’d let you! Juni is mine, and that’s final!"
    "Sighing, I accept her love."
    S "What’d I say earlier, kid?"
    R "Haha. Well, they didn’t call me Randy Ryan in junior high for nothing."
    "I have to admit, even though he’s brazen, Ryan has a certain air of shameless charisma about him.{w} Too bad for him Jazz and I just aren’t interested."
    "Eager to end this conversation, I check the windows and make my decision."
    U "The rain looks like it’s lightened up, so I think I’ll start heading home."
    "Briskly grabbing my backpack and umbrella before anyone has a chance to respond, I make my way out the door.{w} Ryan looks a bit surprised, but Jazz and Savan know exactly what I’m doing."
    U "Bye everyone!"
    "Jazz will know well enough to keep Ryan preoccupied until I’m out of sight and mind."
    
    scene black with fade 

    n "As I walk down the hallway to the main doors, my head is still filled with uncomfortable thoughts about my lackluster love life."
    n "Fiddling with my umbrella, another girl compliments me warmly on its design, a mesh of maple leaves laid over a transparent film, as if I’m carrying a tree’s canopy with me wherever I go."
    n "I smile and thank her, forgetting about my troubles for just a moment.{w} The cute, colorful design takes some of the edge off of wading through the everyday downpour."
    n "Jazz really outdid herself with her birthday gift this year."
    n "Even though it can’t fit in my backpack like hers does, the lovely pattern more than makes up for it."
    n "I’ll make sure to let her know about the compliments I’ve been getting."
    nvl clear
    
    n "I step outside."
    n "Under the awning before the main doors, I take a deep breath, click open my umbrella, and dive into the dreaded rain."
    #BKG: path between
    n "Aside from the rain having drawn down to a light sprinkle, my walk home is uneventful. "
    n "By the time I pass the halfway point to home, sunlight has started breaking through the clouds."
    n "I look up and smile at the rays brightening my spirits after that draining conversation."
    n "…Though for some reason I feel lonelier than usual."
    nvl clear

label juni4: # One Morning’s Mistakes
    n "Bright and early, I wake up before my alarm.{w} After sitting up and stretching, I turn to disable it before it has a chance to go off."
    n "Outside my window, the sky is clear save for a few decorative clouds.{w} Yesterday’s downpour must have rained out the sky, letting the sun wake me up naturally."
    n "For once, the day may actually be bright and clear."
    n "With a spring in my step, I make my way over to my bathroom to put on my contacts before taking a long look myself in the mirror."
    n "What Savan said yesterday wasn’t wrong; my hair {i}is{/i} always a mess."
    n "Since it’s finally clear today, maybe I’ll be able to do something about it."
    nvl clear
    
    # show juni neutral
    # hide juni neutral
    # show juni glare
    # hide juni glare
    # show juni confused
    # hide juni confused
    # three's probably enough
    # SFX: knocking
    n "In what seems like only a minute, Dad comes knocking on my door, asking if I know what time it is."
    n "…{w}…{w}…crap."
    n "I drop my brush and run back into my room, tripping on my bed and sliding over my covers to my nightstand so I can grab my clock."
    n "This is bad.{w} I have barely enough time to run to class."
    nvl clear
    
    n "I hurriedly explain the situation to my dad behind the door."
    n "He offers to drive me to school, but I tell him that it’s okay.{w} I don’t want to bother him with this, especially since it was my mistake to begin with."
    n "I throw on my clothes, grab my backpack, and basically fall downstairs."
    n "On my way out, Dad offers me a piece of toast, but I decline, jumping into my boots and sprinting out the door."
    nvl clear
    
    # BKG: a bunch of transitions or something
    n "In as brisk of a jog I can muster, I stumble down the road to school.{w} If the path wasn’t sloped downhill the entire way, I’d never have been able to make it."
    nvl clear
    
    # BKG: NIH class
    n "Completely out of breath, I burst into Lit with a minute to spare and my hair as much as a mess as ever."
    nvl clear

label juni5: # Exchange in the rain
    n "Despite the morning rush, another day of class passes by without incident."
    
    nvl clear
    
label juni6: # October Nightingale
    n "Mmmm…"
    n "Mmmm…"
	
    nvl clear

label juni7: # Blues Barometer
    n "On our way out of school the next day, Jazz stops to talk to me."
    
    nvl clear
    
label juni8: # October Nightingale II
    n "\"Add friend\""
    
    nvl clear
    
label juni9: # Precipitation
    n "Getting to the town center is even more of a walk than school is, so I ask my mom to drive me there."
    n "She's busy, and tells me to check with Dad since he’s supposed to be taking her car out for groceries and gas."
    
    nvl clear



label juni0:
    # End Juni section
    $ juni_complete = True
    jump transition



label transition:
    
    with dissolve
    scene black

    if start_character == "Jase":
        if jase_complete:
            if not juni_complete:
                jump juni1
        else:
            e "oh poopers"
    elif start_character == "Juni":
        if juni_complete:
            if not jase_complete:
                jump jase1
        else:
            e "oh poopers x2"
    else:
        e "Strange. Did you not start with Jase or Juni?"

    

    return