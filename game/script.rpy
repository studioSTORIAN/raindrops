# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000000"
# image school = "school.png"
# image st_john = "st_john.png"
image north_isle = "images/high-school.jpg"
image north_isle_classroom = "images/high-school.jpg"
image st_john_school = "images/school.png"
# image academy_pacific = "academy_pacific.png"
# image city = "city.png"
# image capial = "capital.png"
# image island = "island.png"

image jazz smile = "images/jordan.png"
image juni smile = "images/barkley.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define l = Character(_("TARS"), color="#ffcccc")
define jase = Character('Jase', color="#0000ff")
define juni = Character('Juni', color="#ff0000")
define mark = Character('Mark', color="#8888ff")
define jazz = Character('Jazz', color="#ff8888")

define u = Character("Juni", color="#ff0000")
define z = Character("Jazz", color="#ffcccc")
define e = Character("Jase", color="#0000ff")
define c = Character("Mark", color="#ccccff")
define s = Character("Savan")
define r = Character("Ryan")
define k = Character("Kevin")
define a = Character("Audrey")

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

    stop music fadeout 1.0
    play music "sounds/darkcoffee.mp3"
    scene black

    if start_character == "Jase":
        jump Jase_section
    else:
        jump Juni_section


label Jase_start:

    $ start_character = "Jase"
    # $ jase_complete = False
    # $ juni_complete = False

    jump start
 

label Jase_section:

    # with dissolve
    scene st_john_school
    with fade

    jase "My name is Jason Guo."

    mark "But you can just call him Jase. He also likes rain."

    jase "fok u Chad"

    "End Jase section. Congratulations!"

    $ jase_complete = True

    jump transition


label Juni_start:

    $ start_character = "Juni"
    jump start


label Juni_section:

    # Begin Day 1 Juni

    # play sound "rain1.mp3" fadein

    "It's raining.{w} As usual."
    "I lean back in my chair, put my arms up and stretch after another long day of classes."

    scene north_isle_classroom
    with dissolve
    # play sound "crowd.mp3" fadein # loop

    "The chatter around me builds up and dies down as my classmates pack their things and head home.{w} \
    I won't be leaving nearly as soon."
    # scene notebook
    # with dissolve
    "I take another look at my notebook, flipping through what I wrote down of Mr.\
    Schumacher's lecture today."
    "We'll be doing a practice essay question on the Protestant Reformation later this week,\
    so I should make sure that I have what he covered this last section down pat."
    "To my right, Mr. Schumacher is still talking to two more inquisitive students about\
    the reasons behind the creation of the Anglican Church."
    "Judging from their growing restlessness, I don't think they realized what they were in for."
    "As the last of the students leave, Jazz appears in the doorway."

    # stop sound "crowd.mp3" fadeout
    # play sound "footsteps.mp3" fadein
    # show jazz smile
    # with dissolve

    z "Hey Juni!"

    # show juni smile

    u "Hi Jazz. How was the chemistry quiz?"
    z "Mmm, nothing too bad. The hardest part was the ion balancing, and that was just\
    because she didn't give us the periodic table."

    # another juni smile????
    u "Ha, that's too bad. I'm sure it'll be given to you on the test-"

    # play sound "footsteps.mp3" fadein

    "As the last two stragglers narrowly escape Mr. Schumacher’s neverending lesson on\
    King Henry’s infidelities, they’re replaced by another pair of boys."

    # show jazz cheeky
    z "Hey you two! Good job remembering to come to practice today. I was afraid I was going\
    to have to go and find you two again like last week."

    "One of the boys beams back at Juni while the other tilts his head sheepishly.\
    I'm glad Ryan has already learned how to deal with Jazz, but it looks like Kevin\
    might need a little more time to settle in."

    r "Of course! We didn't join Quiz Bowl for nothing, right, Kevin?"
    k "What can I say? You and Jazz - sorry, Jasmine - were pretty convincing."
    "The three of them share a small chuckle before I remember something."
    # show jazz neutral
    # speaker juni smile
    u "Oh, right, Jazz. You might already know this, but Savan is out sick today."
    u "He told me to let you know that we should run the meeting as usual, and that\
    you'd know what to do."
    z "Mm, yeah, he messaged me."
    # show jazz smile
    z "Alright, you two, I hope you've been reading up on the practice Quiz Bowl questions,\
    because we're going to be doing your first-ever live buzzer beaters today!"
    "Ryan perks up even more while it looks like it's taking Kevin everything not to\
    roll his eyes and groan."
    r "With the buzzer?"
    z "With the buzzer."

    # 

    "As Ryan pumps his fist with an audible yes, I turn to Mr. Schumacher, who's been\
    quielty smirking behind his desk, pretending to grade papers."

    # juni smile

    u "Mr. Schumacher, do you mind if I get the buzzer from your cabinet?"
    "As I get the dig through his cabinets trying to remember where we put the set last year,\
    Jazz starts assigning the teams."

    # jazz :O

    z "Alright, Ryan, how about you pair up with Kevin, and Juni... you're on your own."
    u "Ehh? What about you?"

    # jazz neutral

    z "I'm moderating, of course. Someone has to read the questions if Savan isn't here."

    # juni pout

    u "But, Jazz..."
    z "Juni, you already know these like the back of your hand. The only way these two\
    can win is by having a faster reaction time, and you're pretty good at that, too."
    z "If anything, Savan would've asked you to handicap yourself anyway."

    # juni surprise nervous sweat
    u "...Mr. Schumacher! Could you read the questions?"
    "My erstwhile ally raises his hands and explains that he's already behind on grading,\
    leaving me on my own."
    "Defeated, I hand everyone their buzzers. Jazz takes out her binder full of past\
    questions and practice begins."
    z "First question: How many circles can be tangent to two parallel lines?"
    "Ryan shouts, \"I know!\" but I've already hit the buzzer. I hope I'm not being too\
    hard on them."

    # scene ?

    "The sounds of our ever-lively Quiz Bowl team drift out into the hallway as the rain\
    continues on without a care for my walk home."

    scene black
    with dissolve
    # stop sounds





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
                jump Juni_section
        else:
            e "oh poopers"
    elif start_character == "Juni":
        if juni_complete:
            if not jase_complete:
                jump Jase_section
        else:
            e "oh poopers x2"
    else:
        e "Strange. Did you not start with Jase or Juni?"

    mark "And they lived happily ever after."

    jazz "We're Canadian."

    "The End."

    return