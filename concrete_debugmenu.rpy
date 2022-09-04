label debug_start:
    $ prolog_time()
    # play music music_list["music_debug1_concrete", "music_debug2_concrete", "music_debug3_concrete", "music_debug4_concrete", "music_debug5_concrete", "music_debug6_concrete", "music_debug7_concrete", "music_debug8_concrete", "music_debug9_concrete", "music_debug10_concrete", "music_debug11_concrete"] loop fadein 4
    jump debug_control
label debug_control:
    scene bg black
    window show
    "ДЕБАГ МЕНЮ"
    menu:
        "Лавпоинты":
            jump debug_control_lp
        "Переменные":
            jump debug_control_ch
        "Телепорт":
            jump debug_control_tp
        "Нормальный запуск":
            $ debug_revars_check = False
            jump concrete_createvars_day1
label debug_control_lp:
    while True:
        menu:
                "Аска":
                    while True:
                        menu:
                            "+1":
                                $ lp_aska += 1
                            "-1":
                                $ lp_aska -= 1
                            "Назад":
                                jump debug_control_lp
                "Женя":
                    while True:
                        menu:
                            "+1":
                                $ lp_zhenya += 1
                            "-1":
                                $ lp_zhenya -= 1
                            "Назад":
                                jump debug_control_lp
                "Мику":
                    while True:
                        menu:
                            "+1":
                                $ lp_miku += 1
                            "-1":
                                $ lp_miku -= 1
                            "Назад":
                                jump debug_control_lp
                "Геи":
                    while True:
                        menu:
                            "+1":
                                $ lp_gay += 1
                            "-1":
                                $ lp_gay -= 1
                            "Назад":
                                jump debug_control_lp
                "Хикка":
                    while True:
                        menu:
                            "+1":
                                $ lp_hikka += 1
                            "-1":
                                $ lp_aska -= 1
                            "Назад":
                                jump debug_control_lp
                "Назад":
                    jump debug_control

label debug_control_ch:
    while True:
        menu:
                "Пересоздать переменные":
                    $ debug_revars_check = True
                    jump concrete_createvars_day1
                "День 1":
                    while True:
                        menu:
                            "Назад":
                                jump debug_control_ch
                "День 2":
                    while True:
                        menu:
                            "С кем поел за завтраком":
                                menu:
                                    "Поел с Женей":
                                        $ dined_with_gays = False
                                        $ dined_with_zhenya = True
                                        $ dined_with_miku = False
                                    "Поел с Мику":
                                        $ dined_with_gays = False
                                        $ dined_with_zhenya = False
                                        $ dined_with_miku = True
                                    "Поел с геями":
                                        $ dined_with_gays = True
                                        $ dined_with_zhenya = False
                                        $ dined_with_miku = False
                                    "Назад":
                                        jump debug_control_ch
                            "Вступление в клубы":
                                menu:
                                    "Библиотека":
                                        menu:
                                            "Вступил":
                                                $ joined_libray = True
                                            "Отказал":
                                                $ joined_libray = False
                                        jump debug_control_ch
                                    "Музыкальный клуб":
                                        menu:
                                            "Сыграл":
                                                $ joined_musclub = True
                                                $ played_for_miku = True
                                            "Вступил":
                                                $ joined_musclub = True
                                            "Отказал":
                                                $ joined_musclub = False
                                        jump debug_control_ch
                                    "Гейклуб":
                                        menu:
                                            "Вступил":
                                                $ joined_gays = True
                                            "Отказал":
                                                $ joined_gays = False
                                        jump debug_control_ch
                            "Хождение по лагерю":
                                while True:
                                    menu:
                                        "Побывать в библиотеке":
                                            $ visited_libray = True
                                        "Побывать в музклубе":
                                            $ visited_musclub = True
                                        "Побывать в гейклубе":
                                            $ visited_gayclub = True
                                        "Побывать в дыре":
                                            $ visited_shithole = True
                                        "Побывать в медпункте":
                                            $ visited_aidpost = True
                                        "Уйти отовсюду":
                                            $ visited_libray = False
                                            $ visited_musclub = False
                                            $ visited_gayclub = False
                                            $ visited_shithole = False
                                            $ visited_aidpost = False
                                        "Назад":
                                            jump debug_control_ch
                            "Вопрос пивонера":
                                menu:
                                    "Отказал":
                                        $ refused_the_pioneer = True
                                    "Согласился":
                                        $ refused_the_pioneer = False
                                jump debug_control_ch
                "Назад":
                    jump debug_control
label debug_control_tp:
    while True:
        menu:
                "День 1":
                    menu:
                        "Начало":
                            jump concrete_day1
                        "Назад":
                            jump debug_control_tp
                "День 2":
                    menu:
                        "Начало":
                            jump concrete_day2
                        "Завтрак":
                            jump concrete_day2_dinner_choice
                        "Обходной":
                            jump concrete_day2_after_dining
                        "Лес":
                            jump concrete_day2_after_visitsheet
                        "Назад":
                            jump debug_control_tp
                "Назад": 
                    jump debug_control