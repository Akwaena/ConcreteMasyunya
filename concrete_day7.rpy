label concrete_day7:
    pass

label concrete_createvars_day7:
    $ vars_done = True
    if not debug_revars_check:
        jump concrete_day1
    else:
        $ debug_revars_check = False
        jump debug_control