init -1199 python:
    from os import path
    mod_prefix = "concrete" # Задаём префикс моду в формате строчки. (например, mod_prefix = 'factory). Если False, то без префикса.
    WRITE_IN_FILE = False # Занесение кода для объявления в отдельный текстовик autoinitialized_music в корне БЛ.
    if mod_prefix:
        mod_prefix = '_' + mod_prefix
    else:
        mod_prefix = ''
    modID = 'ConcreteMasyunya'
    if WRITE_IN_FILE:
        autoinitialized_music_dict = []

    for file in renpy.list_files():
        if modID in file:
            file_name = path.splitext(path.basename(file))[0] + mod_prefix
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                if WRITE_IN_FILE:
                    autoinitialized_music_dict.append("$ {} = \"{}\"".format(file_name, file))
                else:
                    globals()[file_name] = file

    if WRITE_IN_FILE:
        with open('autoinitialized_music.txt', 'w') as opt:
            for i in autoinitialized_music_dict:
                opt.writelines(i + '\n')