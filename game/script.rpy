# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000000"
# image school = "school.png"
# image st_john = "st_john.png"
image st_john_north = "images/crossing.jpg"
image north_isle_school = "images/high-school.jpg"
image north_isle_classroom = "images/library.jpg"
image st_john_school = "images/school.png"
# image academy_pacific = "academy_pacific.png"
# image city = "city.png"
# image capial = "capital.png"
# image island = "island.png"

image jazz smile = "images/jazz_smile.png"
image jazz beam = "images/jazz_smile_less.png"
image juni smile = "images/barkley.png"
image jazz = "images/jazz_test_l.png"
image jazz cheeky = "images/jazz_test_l.png"
image ryan = "images/barkley.png"
image kevin = "images/jordan.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define l = Character(_("TARS"), color="#ffcccc")

define u = Character("Juni", color="#ff0000")
define z = Character("Jazz", color="#ffcccc")
define e = Character("Jase", color="#0000ff")
define c = Character("Mark", color="#ccccff")
define s = Character("Savan")
define r = Character("Ryan")
define k = Character("Kevin")
define a = Character("Audrey")

define jase = e
define juni = u
define mark = c
define jazz = z

define n = Character(None, kind=nvl)

define typo = Character("TYPO HERE?", color="#ff0000")


# Add a splashscreen: http://www.renpy.org/wiki/renpy/doc/cookbook/Adding_a_Splashscreen
# Something with Studio Storian logo or whatever. Perhaps move the "SS presents" to the first start
label splashscreen:
    scene black
    with Pause(1)

    show text "Studio STORIAN Presents..." with dissolve
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
    if start_character == "Jase":
        jump jase1
    else:
        jump juni11

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
    jase "My name is Jason Guo."
    mark "But you can just call him Jase. He also likes rain."
    jase "fok u Chad"
    "End Jase section. Congratulations!"
    $ jase_complete = True
    jump transition


label juni11: # Just another day at North Isle High

    # Begin Day 1 Juni
    # play sound "rain1.mp3" fadein
    stop music fadeout 1.0
    play music "sounds/darkcoffee.mp3"
    scene black

    "It's raining.{w} As usual."
    "{cps=35}I lean back in my chair, put my arms up and stretch after another long day of classes.{/cps}"

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
    "Judging from their growing restlessness, I don't think they realized what they were in for."
    "As the last of the students leave, Jazz appears in the doorway."

    # stop sound "crowd.mp3" fadeout
    # play sound "footsteps.mp3" fadein
    # show jazz smile
    show jazz at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
        # linear 1.0 xalign 0.2
    # with dissolve

    z "Hey Juni!"

    # show juni smile

    u "Hi Jazz. How was the chemistry quiz?"
    z "Mmm, not too bad. The hardest part was the ion balancing, and that was just
    because she didn't give us the periodic table."

    # another juni smile????
    u "Ha, that's too bad. I'm sure they'll give it to you on the test-"

    # play sound "footsteps.mp3" fadein

    "As the last two students narrowly escape Mr. Schumacher's neverending lesson on
    King Henry's infidelities, Ryan and Kevin come in."

    hide jazz
    show jazz cheeky at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
    z "Hey you two! Good job remembering to come to practice today. I thought I was going
    to have to track you down again like last week."

    "Ryan beams back at Jazz while Kevin tilts his head sheepishly.
    I'm glad Ryan has already learned how to deal with Jazz, but it looks like Kevin
    might need a little more time to settle in."

    hide jazz cheeky
    show ryan at Position(xpos=0.7, xanchor=0.5, ypos=0.5, yanchor=0.5)
    r "Of course! We didn't join Quiz Bowl for nothing, right, Kevin?"
    show kevin at Position(xpos=0.3, xanchor=0.5, ypos=0.5, yanchor=0.5)
    k "What can I say? You and Jazz - sorry, Jasmine - were pretty convincing."
    # show jazz neutral
    "As they talk, I remember something."
    # speaker juni smile
    hide ryan
    hide kevin
    u "Oh, right, Jazz. Savan's out sick today."
    u "He told me to let you know to run the meeting as usual, and that you'd know what to do."
    show jazz at Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.5)
    z "Yeah! He messaged me."
    z "Okay, you two, I hope you've been reading up on Quiz Bowl questions,
    \'cause today we're going to be doing your first-ever live practice!"
    "Ryan lights up even more while it looks like it's taking Kevin everything he has not to
    roll his eyes and groan."
    r "With the buzzer?"
    z "With the buzzer."

    # 

    "As Ryan pumps his fist with an audible yes, I turn to Mr. Schumacher, who's been
    quietly smirking behind his desk, pretending to grade papers."

    # juni smile

    u "Mr. Schumacher, do you mind if I get the buzzer from your cabinet?"
    "As I dig through his cabinets trying to remember where we left the set last summer,
    Jazz starts assigning the teams."

    # jazz :O

    z "Alright, Ryan, how about you pair up with Kevin, and Juni...{w} you're on your own."
    u "Wait, what? What about you?"

    # jazz neutral

    z "I'm moderating, of course. Someone has to read the questions if Savan isn't here."

    # juni pout

    u "But, Jazz..."
    z "Juni, you already know these like the back of your hand. The only way these two
    can win is by having a faster reaction time, and you're pretty good at that, too."
    z "If anything, Savan would've asked you to handicap yourself anyway."

    # juni surprise nervous sweat
    u "...Mr. Schumacher! Could you read the questions?"
    "He raises his hands and makes the excuse that he's already behind on grading,
    leaving me on my own."
    "Defeated, I hand everyone their buzzers. Jazz takes out her binder full of past
    questions and practice begins."
    z "First question: How many circles can be tangent to two parallel lines?"
    "Ryan shouts, \"I know!\" but I've already hit the buzzer. I hope I'm not being too hard on them."

    # scene ?

    "The sounds of our lively Quiz Bowl team drift out into the hallway as the rain
    continues on without a care for my walk home."

    # scene black
    # with dissolve
    # stop sounds
    jump juni2

label juni2:

    scene st_john_north
    with fade
    # play sound rain 
    # show jazz cheeky umbrella
    z "Bye Juni! Careful around puddles!"
    "I stick my tongue out at her, remembering the last time I came to school with my
    cardigan wet after tripping into one."
    # show Juni smile
    u "Hpmh! See you tomorrow!"
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
    n "I pass by him about once a week."
    n "His face is familiar but I can't seem to remember his name."
    n "These are tracks my mind has worn down for a while now, but going through it again should keep my mind off the rain long enough to get home."
    n "This jogger is on the other school's Quiz Bowl team, but I don't think I can say that
    we've ever met."
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
    n "Because it was summer, our upperclassmen had graduated and our team hadn't yet
    been able to recruit Ryan and Kevin, so it was only me, Jazz, and Savan."
    n "They were in a similar predicament, with only Audrey, him, and a third person on their team."
    n "I remember him being a bit hesitant to sit as a team member, making the excuse that
    he was only supposed to be the alternate.{w} I found this strange because he was clearly the oldest one on their team."
    n "After I dug out the same buzzer we used during practice today, we took our seats.
    Savan had asked another friend to moderate, and so the game began."
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

    scene black
    with dissolve

    jump juni0

label juni0:

    ##############
    # Old filler #
    ##############

    juni "My name is Juniper Young."

    jazz "We just call her Juni. She hates rain."

    juni "You can stay under my umbrella, eh!"

    "End Juni section. Congratulations!"

    $ juni_complete = True

    jump transition


label transition:
    
    with dissolve
    scene black

    if start_character == "Jase":
        if jase_complete:
            if not juni_complete:
                jump juni11
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

    mark "And they lived happily ever after."

    jazz "We're Canadian."

    "The End."

    return