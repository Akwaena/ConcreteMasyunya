init -1200 python:
    import os
    mod_prefix = "concrete" # Задаём префикс моду в формате строчки. (например, mod_prefix = 'factory'). Если False, то без префикса.
    WRITE_IN_FILE = False # Занесение кода для объявления в отдельный текстовик autoinitialized_images в корне БЛ.
    if mod_prefix:
        mod_prefix = '_' + mod_prefix
    else:
        mod_prefix = ''
    modID = 'ConcreteMasyunya'
    mod_dist = {'normal': '', 'far': 'far', 'close': 'close'}
    mod_size = {'normal': (900, 1080), 
                 'far': (675, 1080), 
                 'close': (1125, 1080)}
    if WRITE_IN_FILE:
        autoinitialized_img_dict = []

    for dir, fn in renpy.loader.listdirfiles(False):
        extra_path = ''
        if modID + "/" in fn:
            if fn.startswith(modID):
                mod_imgs_path = dir + '/' + modID + r'/images/'
            else:
                extra_path = fn[:fn.find(modID)]
                modID = extra_path + modID
                mod_imgs_path = dir + '/' + modID + r'/images/'
    for folder in os.listdir(mod_imgs_path):
            path = mod_imgs_path + folder + '/'
            for file in os.listdir(path):
                mod_autoinitializating_images = folder + ' ' + file[:file.find('.')] + mod_prefix
                if folder != 'sprites':
                    if WRITE_IN_FILE:
                        autoinitialized_img_dict.append("$ renpy.image(\"{}\", \"{}\")".format(mod_autoinitializating_images, path[path.find(modID):] + file))
                    else:
                        renpy.image(mod_autoinitializating_images, path[path.find(modID):] + file)
                else:
                    for dist in os.listdir(path):
                        who_path = path + dist + '/'
                        for who in os.listdir(who_path):
                            who_path_num = who_path + who + '/'
                            for numb in os.listdir(who_path_num):
                                sprite_folders = os.listdir(
                                    who_path_num + numb + '/')

                                for i in sprite_folders: 
                                    if 'body.png' in i:
                                        file_body = who_path_num[who_path_num.find(
                                            modID):] + numb + '/' + i
                                        break #FIXME правки исчезаюзего тела уровня /b/
                                    else:
                                        file_body = im.Alpha("images/gui/settings/leaf.png", 0.0) # плейсхолдер (к сожалению, пустой картинки в файлах БЛ не нашлось, пришлось сделать pngшку листка прозрачной) вместо тела.

                                body = sprite_folders
                                clothes_l = list()
                                emo_l = list()
                                acc_l = list()

                                if 'clothes' in sprite_folders:
                                    for clothes in os.listdir(who_path_num + numb + r'/clothes/'):
                                        clothes_l.append([clothes.split(
                                            '_', 2)[-1][:-4], who_path_num[who_path_num.find(modID):] + numb + r'/clothes/'+clothes])

                                if 'emo' in sprite_folders:
                                    for emo in os.listdir(who_path_num + numb + r'/emo/'):
                                        emo_l.append([emo.split(
                                            '_', 2)[-1][:-4], who_path_num[who_path_num.find(modID):] + numb + r'/emo/'+emo])

                                if 'acc' in sprite_folders:
                                    for acc in os.listdir(who_path_num + numb + r'/acc/'):
                                        acc_l.append([acc.split(
                                            '_', 2)[-1][:-4], who_path_num[who_path_num.find(modID):] + numb + r'/acc/'+acc])
                                if WRITE_IN_FILE:
                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\"),
                    im.matrix.tint(
            0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, mod_dist[dist], mod_size[dist], file_body, mod_size[dist], file_body, mod_size[dist], file_body))
                                else:
                                    renpy.image(who + mod_prefix + ' ' + mod_dist[dist],
                                                ConditionSwitch(
                                                    "persistent.sprite_time=='sunset'",
                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                    (0, 0), file_body),
                                                        im.matrix.tint(
                                            0.94, 0.82, 1.0)
                                        ),

                                                    "persistent.sprite_time=='night'",
                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                    (0, 0), file_body),
                                                        im.matrix.tint(
                                            0.63, 0.78, 0.82)
                                        ),

                                                    True,
                                        im.Composite(mod_size[dist],
                                                        (0, 0), file_body)
                                    )
                                    )
                                if 'clothes' and 'emo' and 'acc' in sprite_folders:
                                    for emotion in emo_l:
                                        for clothes in clothes_l:
                                            for acc in acc_l:
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),
                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\",
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, clothes[0], emotion[0], acc[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], emotion[1], acc[1], mod_size[dist], file_body, clothes[1], emotion[1], acc[1], mod_size[dist], file_body, clothes[1], emotion[1], acc[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + clothes[0] + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), emotion[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), emotion[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), clothes[1],
                                                                        (0, 0), emotion[1],
                                                                        (0, 0), acc[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),
                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, clothes[0], emotion[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], emotion[1], mod_size[dist], file_body, clothes[1], emotion[1], mod_size[dist], file_body, clothes[1], emotion[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), emotion[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), emotion[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), clothes[1],
                                                                        (0, 0), emotion[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),
                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, emotion[0], acc[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], acc[1], mod_size[dist], file_body, emotion[1], acc[1], mod_size[dist], file_body, emotion[1], acc[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), emotion[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), emotion[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), emotion[1],
                                                                        (0, 0), acc[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),
                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, clothes[0], acc[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], acc[1], mod_size[dist], file_body, clothes[1], acc[1], mod_size[dist], file_body, clothes[1], acc[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1],
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), clothes[1],
                                                                        (0, 0), acc[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),

                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, emotion[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), emotion[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), emotion[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), emotion[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),

                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, acc[0], mod_dist[dist], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), acc[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), acc[1])
                                                    )
                                                    )
                                                if WRITE_IN_FILE:
                                                    autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
                ConditionSwitch(
                    "persistent.sprite_time=='sunset'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.94, 0.82, 1.0)
        ),

                    "persistent.sprite_time=='night'",
        im.MatrixColor(im.Composite({},
                                    (0, 0), \"{}\",
                                    (0, 0), \"{}\"),
                        im.matrix.tint(
            0.63, 0.78, 0.82)
        ),

                    True,
        im.Composite({},
                        (0, 0), \"{}\",
                        (0, 0), \"{}\")
    )
    )""".format(who, mod_prefix, clothes[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1]))
                                                else:
                                                    renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                                ConditionSwitch(
                                                                    "persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1]),
                                                                        im.matrix.tint(
                                                            0.94, 0.82, 1.0)
                                                        ),

                                                                    "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite(mod_size[dist],
                                                                                    (0, 0), file_body,
                                                                                    (0, 0), clothes[1]),
                                                                        im.matrix.tint(
                                                            0.63, 0.78, 0.82)
                                                        ),

                                                                    True,
                                                        im.Composite(mod_size[dist],
                                                                        (0, 0), file_body,
                                                                        (0, 0), clothes[1])
                                                    )
                                                    )
                                if 'clothes' and 'emo' in sprite_folders:   
                                    for clothes in clothes_l:
                                        for emotion in emo_l:
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, clothes[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), clothes[1])
                                                )
                                                )
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, clothes[0], emotion[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], emotion[1], mod_size[dist], file_body, clothes[1], emotion[1], mod_size[dist], file_body, clothes[1], emotion[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1],
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1],
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), clothes[1],
                                                                    (0, 0), emotion[1])
                                                )
                                                )
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, emotion[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), emotion[1])
                                                )
                                                )
                                if 'clothes' and 'acc' in sprite_folders:
                                    for clothes in clothes_l:
                                        for acc in acc_l:
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, clothes[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), clothes[1])
                                                )
                                                )
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, clothes[0], acc[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], acc[1], mod_size[dist], file_body, clothes[1], acc[1], mod_size[dist], file_body, clothes[1], acc[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1],
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), clothes[1],
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), clothes[1],
                                                                    (0, 0), acc[1])
                                                )
                                                )
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, acc[0], mod_dist[dist], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), acc[1])
                                                )
                                                )
                                if 'emo' and 'acc' in sprite_folders:
                                    for emotion in emo_l:
                                        for acc in acc_l:
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, emotion[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), emotion[1])
                                                )
                                                )
                                            if WRITE_IN_FILE:
                                                autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, emotion[0], acc[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], acc[1], mod_size[dist], file_body, emotion[1], acc[1], mod_size[dist], file_body, emotion[1], acc[1]))
                                            else:
                                                renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                            ConditionSwitch(
                                                                "persistent.sprite_time=='sunset'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1],
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.94, 0.82, 1.0)
                                                    ),

                                                                "persistent.sprite_time=='night'",
                                                    im.MatrixColor(im.Composite(mod_size[dist],
                                                                                (0, 0), file_body,
                                                                                (0, 0), emotion[1],
                                                                                (0, 0), acc[1]),
                                                                    im.matrix.tint(
                                                        0.63, 0.78, 0.82)
                                                    ),

                                                                True,
                                                    im.Composite(mod_size[dist],
                                                                    (0, 0), file_body,
                                                                    (0, 0), emotion[1],
                                                                    (0, 0), acc[1])
                                                )
                                                )
                                        if WRITE_IN_FILE:
                                            autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, acc[0], mod_dist[dist], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1]))
                                        else:
                                            renpy.image(who + mod_prefix + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                        ConditionSwitch(
                                                            "persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), acc[1]),
                                                                im.matrix.tint(
                                                    0.94, 0.82, 1.0)
                                                ),

                                                            "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), acc[1]),
                                                                im.matrix.tint(
                                                    0.63, 0.78, 0.82)
                                                ),

                                                            True,
                                                im.Composite(mod_size[dist],
                                                                (0, 0), file_body,
                                                                (0, 0), acc[1])
                                            )
                                            )
                                if 'clothes' in sprite_folders:
                                    for clothes in clothes_l:
                                        if WRITE_IN_FILE:
                                            autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, clothes[0], mod_dist[dist], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1], mod_size[dist], file_body, clothes[1]))
                                        else:
                                            renpy.image(who + mod_prefix + ' ' + clothes[0] + ' ' + mod_dist[dist],
                                                        ConditionSwitch(
                                                            "persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), clothes[1]),
                                                                im.matrix.tint(
                                                    0.94, 0.82, 1.0)
                                                ),

                                                            "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), clothes[1]),
                                                                im.matrix.tint(
                                                    0.63, 0.78, 0.82)
                                                ),

                                                            True,
                                                im.Composite(mod_size[dist],
                                                                (0, 0), file_body,
                                                                (0, 0), clothes[1])
                                            )
                                            )
                                if 'acc' in sprite_folders:
                                    for acc in acc_l:
                                        if WRITE_IN_FILE:
                                            autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),
                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, acc[0], mod_dist[dist], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1], mod_size[dist], file_body, acc[1]))
                                        else:
                                            renpy.image(who + mod_prefix + ' ' + acc[0] + ' ' + mod_dist[dist],
                                                        ConditionSwitch(
                                                            "persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), acc[1]),
                                                                im.matrix.tint(
                                                    0.94, 0.82, 1.0)
                                                ),

                                                            "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), acc[1]),
                                                                im.matrix.tint(
                                                    0.63, 0.78, 0.82)
                                                ),
                                                            True,
                                                im.Composite(mod_size[dist],
                                                                (0, 0), file_body,
                                                                (0, 0), acc[1])
                                            )
                                            )
                                if 'emo' in sprite_folders:
                                    for emotion in emo_l:
                                        if WRITE_IN_FILE:
                                            autoinitialized_img_dict.append("""$ renpy.image(\"{}{} {} {}\",
            ConditionSwitch(
                "persistent.sprite_time=='sunset'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.94, 0.82, 1.0)
    ),

                "persistent.sprite_time=='night'",
    im.MatrixColor(im.Composite({},
                                (0, 0), \"{}\",
                                (0, 0), \"{}\"),
                    im.matrix.tint(
        0.63, 0.78, 0.82)
    ),

                True,
    im.Composite({},
                    (0, 0), \"{}\",
                    (0, 0), \"{}\")
)
)""".format(who, mod_prefix, emotion[0], mod_dist[dist], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1], mod_size[dist], file_body, emotion[1]))
                                        else:
                                            renpy.image(who + mod_prefix + ' ' + emotion[0] + ' ' + mod_dist[dist],
                                                        ConditionSwitch(
                                                            "persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), emotion[1]),
                                                                im.matrix.tint(
                                                    0.94, 0.82, 1.0)
                                                ),

                                                            "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite(mod_size[dist],
                                                                            (0, 0), file_body,
                                                                            (0, 0), emotion[1]),
                                                                im.matrix.tint(
                                                    0.63, 0.78, 0.82)
                                                ),

                                                            True,
                                                im.Composite(mod_size[dist],
                                                                (0, 0), file_body,
                                                                (0, 0), emotion[1])
                                            )
                                            )

    if WRITE_IN_FILE:
        with open('autoinitialized_images.txt', 'w') as opt:
            for i in autoinitialized_img_dict:
                opt.write(i + '\n')