####################
## New Key Bindings

init: # -1 python hide:
    $ config.keymap['rollback'].append('K_UP')
    $ config.keymap['rollback'].append('repeat_K_UP')
    $ config.keymap['focus_up'].remove('K_UP')
    $ config.keymap['rollforward'].append('K_DOWN')
    $ config.keymap['rollforward'].append('repeat_K_DOWN')
    $ config.keymap['focus_down'].remove('K_DOWN')
    # $ config.keymap['game_menu'].remove('mouseup_3')
    $ _game_menu_screen = "pause_menu"