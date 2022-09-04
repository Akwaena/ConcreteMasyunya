init python:
    mods["fullcement_masyunya_by_cement_o_concrete_team"] = u"Цельноцементная Масюня"
    flash = Fade(.25, 0, .75, color="#fff")
    try:
        mod_tags["fullcement_masyunya_by_cement_o_concrete_team"] = ["gameplay:vn","length:days","protagonist:male","character:Семён","character:Алиса","character:Ульяна","character:Славя","character:Лена","character:Мику","character:Ольга Дмитриевна","character:Пионер","character:Электроник","character:Шурик","character:Женя","character:Виола","character:Юля"]
    except NameError:
        pass
    mod_name = "Цельноцементная Масюня"
    debug_mode = True
    if debug_mode:
        config.developer = True
    vars_done = False

label fullcement_masyunya_by_cement_o_concrete_team:
    $ debug_revars_check = False
    if debug_mode:
        jump debug_start
    else:
        jump concrete_day1
    
    return