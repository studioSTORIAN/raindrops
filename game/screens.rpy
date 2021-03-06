﻿# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            order_reverse True
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    # use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    # use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    # use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

init -1 python:
    def safeload(filename="savedrops",*args,**kwargs):
        if renpy.can_load(filename,args):
            return renpy.load(filename)
        else:
            persistent.character = None
            return
    
    def deletesave(filename):
        persistent.character = None
        renpy.unlink_save(filename)
        renpy.full_restart(transition=fade)
        return

    def safestart():
        if renpy.can_load("savedrops"): # if there's a save file
            return renpy.call_screen("yesno_prompt",
                "Are you sure you would like to start over? Starting a new game will overwrite your current save file.",
                Start("Juni_start"), Return())
        else:
            renpy.Start("Juni_start")
screen main_menu():
    tag menu
    if persistent.complete == True:
        use main_menu_complete
    elif persistent.juni_complete == True:
        use main_menu_base
    elif persistent.character == "juni" and renpy.can_load("savedrops"):
        use main_menu_juni
    else:
        use main_menu_base

screen main_menu_base():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"


    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .9

        # xminimum int(config.screen_width * .4)

        has vbox

        textbutton _("start") action Start("Juni_start")
        # textbutton _("pause") action ShowMenu("pause_menu")
        # textbutton _("start") action NullAction() # Start()
        # textbutton _("continue") action Function(safeload) # ShowMenu("load")
        # textbutton _("reset") action Function(deletesave,"savedrops")
        textbutton _("chapters") action ShowMenu("chapters")
        textbutton _("options") action ShowMenu("preferences")
        # textbutton _("help") action Help()
        # textbutton _("extras") action NullAction()
        textbutton _("quit") action Quit(confirm=False)

    # Left and Right Characters
    # imagemap:
    #     ground "images/jordanbw.png"
    #     hover "images/jordan.png"
    #     xalign 0
    #     yalign 1.0
    #     hotspot (0,0,250,350) action Start("Jase_start")

    # imagemap:
    #     ground "images/barkleybw.png"
    #     hover "images/barkley.png"
    #     xalign 1.2
    #     yalign 1.0
    #     hotspot (85,0,265,350) action Start("Juni_start")

screen main_menu_juni():
    tag menu
    window:
        style "mm_root"
    frame:
        style_group "mm"
        xalign .5
        yalign .9
        has vbox

        # textbutton _("start") action NullAction() # Start()
        textbutton _("start") action ShowMenu("restart_prompt")
        textbutton _("continue") action Function(safeload) # ShowMenu("load")
        # textbutton _("pause") action ShowMenu("pause_menu")
        textbutton _("chapters") action ShowMenu("chapters")
        textbutton _("options") action ShowMenu("preferences")
        # textbutton _("reset") action Function(deletesave,"savedrops")
        textbutton _("quit") action Quit(confirm=False)

screen main_menu_complete():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"


    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .9

        # xminimum int(config.screen_width * .4)

        has vbox


        textbutton _("start") action NullAction() # Start()
        # textbutton _("continue") action Return() # ShowMenu("load")
        textbutton _("chapters") action ShowMenu("chapters")
        textbutton _("options") action ShowMenu("preferences")
        # textbutton _("help") action Help()
        # textbutton _("extras") action NullAction()
        textbutton _("quit") action Quit(confirm=False)

    # Left and Right Characters
    imagemap:
        ground "images/jordanbw.png"
        hover "images/jordan.png"
        xalign 0
        yalign 1.0
        hotspot (0,0,250,350) action Start("Jase_start")

    imagemap:
        ground "images/barkleybw.png"
        hover "images/barkley.png"
        xalign 1.2
        yalign 1.0
        hotspot (85,0,265,350) action Start("Juni_start")

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
        background None


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        # textbutton _("Save Game") action ShowMenu("save")
        # textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"
        ysize 20
        color "#FF0000"
    style gm_nav_button_text:
        size 10
    # style gm_nav_button_text:
        # size 12


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Reset Progress")
                textbutton _("Reset") action Function(deletesave,"savedrops")

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


########################################################################
# Pause Menu
#
# Shows up when the player pauses the game. Displays relevant game info
# such as character, chapter, day, and forecast.
screen pause_menu():
    
    tag menu

    window:
        style "pm_root"

    # vbox:
    #     style_group "pause"

    #     xalign 5.0
    #     yalign 5.0

    #     textbutton _("resume") action Return()
    #     textbutton _("options") action ShowMenu("preferences")
    #     textbutton _("quit") action Quit()
    frame:
        style_group "pm"
        xalign .5
        yalign .6

        has vbox
        
        # pos (0.5, 0.5)
        # anchor (0.5, 0.5)
        
        textbutton _("continue") action Return()
        # textbutton _("Save Game") action ShowMenu("save")
        # textbutton _("Load Game") action ShowMenu("load")
        textbutton _("chapters") action ShowMenu("chapters")
        textbutton _("options") action ShowMenu("preferences")
        textbutton _("quit to menu") action MainMenu()
        # textbutton _("Help") action Help()
        textbutton _("quit to desktop") action Quit()

init -2:
    style pm_button:
        size_group "pm"


##################
# Chapter selection
#
# Jump chapters.
screen chapters():

    tag menu
    window:
        style "cm_root"
    frame:
        style_group "cm"
        xalign .5
        yalign .5

        has vbox

        textbutton _("Juni 1: Just Another Day at North Isle High") action Start('juni1')
        textbutton _("Juni 2: Another Passing on the Walk Home") action Start('juni2')
        textbutton _("Juni 3: Lacklovester Wednesday") action Start('juni3')
        textbutton _("Juni 4: One Morning's Mistakes") action Start('juni4')
        # textbutton _("Juni 5: Exchange in the Rain") action Start('juni5')
        # textbutton _("Juni 6: October Nightingale") action Start('juni6')
        # textbutton _("Juni 7: Blues Barometer") action Start('juni7')
        # textbutton _("Juni 7: October Nightingale II") action Start('juni8')
        # textbutton _("Juni 9: Precipitation") action Start('juni9')
        textbutton _("main menu") action ShowMenu("main_menu")

init -2:
    style cm_button:
        size_group "cm"


#################
# Rollback screen
#
# Replaces the rollback functionality built into RenPy.
screen rollback():

    tag menu
    window:
        style "rb_root"
    frame:
        style_group "rb"


##########
# Restart confirmation
#
# Because it's cleaner this way than trying to fit it all in main_menu_juni as one line.
screen restart_prompt():

    tag menu
    use yesno_prompt("Are you sure you would like to start over? Starting a new game will overwrite your current save file.",
     Start("Juni_start"), ShowMenu("main_menu_juni"))