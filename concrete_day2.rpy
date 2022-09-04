label concrete_day2:
    $ day_time()
    $ backdrop = "days"
    $ new_chapter(2, mod_name+u"День 2")


    scene bg black
    jump concrete_day2_before_dinner

label concrete_createvars_day2:
    $ dined_with_gays = False
    $ dined_with_zhenya = False
    $ dined_with_miku = False

    $ time_left = 5
    $ visited_libray = False
    $ visited_musclub = False
    $ visited_gayclub = False
    $ visited_shithole = False
    $ visited_aidpost = False
    $ joined_libray = False
    $ joined_musclub = False
    $ joined_gayclub = False
    $ played_for_miku = False

    $ refused_the_pioneer = False

    jump concrete_createvars_day3

label amogus:
    window show
    play music music_list["no_tresspassing"] fadein 5
    "amogus"
    window hide
    jump amogus

label debug_window:


label concrete_day2_before_dinner:
    $ persistent.sprite_time = "day"
    window show
    "..."
    play ambience ambience_int_cabin_day fadein 4
    "Я проснулся."
    scene bg int_house_of_mt_day with dissolve
    show blinking with flash
    "Солнечные лучи били в глаза."
    "Потянувшись, я вылез из постели, взял любезно оставленные Ольгой умывальные принадлежности и вышел из домика."
    scene bg ext_house_of_mt_day with dissolve
    "На улице стояла обычная для Совенка погода."
    show mt smile pioneer
    mt "Доброе утро, Семен! {w}Я уже хотела тебя будить."
    me "Доброе, Ольга Дмитриевна."
    show mt normal pioneer
    mt "Семен, ты знаешь, где умывальники?"
    me "Да, я вчера успел изучить лагерь."
    mt "Хорошо."
    mt "Смотри, не опоздай на линейку!"
    me "Так точно!"
    "Я отправился умываться."
    window hide

    scene bg ext_washstand_day with dissolve
    play ambience ambience_forest_day fadein 4
    window show
    th "Вода. Вода – это то, без чего мы не сможем существовать."
    th "За множество циклов я так и не привык к этому кусочку Антарктиды в Совенке."
    scene bg ext_washstand2_day with dissolve
    play sound sfx_open_water_sink
    play sound sfx_water_sink_stream loop
    "Осторожно подставив ладони под сверкающую струю воды, я ощутил приятную прохладу."
    play music music_list["no_tresspassing"] fadein 3
    "Приятную. Не обжигающе холодную..."
    stop music fadeout 10
    th "Ладно, наверное, я чуть задержался, и солнце успело нагреть трубу."
    play sound sfx_close_water_sink
    "Кто-то быстро шёл, даже бежал в мою сторону."
    play sound sfx_slavya_run
    th "Славя с пробежки."
    sl "Физкульт-привет!"
    scene bg ext_washstand_day with dissolve
    show sl normal sport far
    me "Шаббат шалом!"
    sl "Как спалось?"
    me "Нормально."
    "Ответил я буднично."
    show sl smile sport far
    sl "Это хорошо. Не забудь про линейку!"
    me "Не беспокойся, не забуду."
    sl "Я побежала, не опаздывай!"
    me "Бывай."
    hide sl
    play sound sfx_slavya_run

    "Умывание окончено."
    th "Линейка. {w}Есть ли смысл на нее идти? Я же и так знаю, что на ней будет."
    th "Хотя, это же моя \"первая\" линейка, меня, как минимум, представить должны."

    "С этой мыслью я отправился на площадь."
    window hide
    
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    $ renpy.pause(1)

    scene cg d2_lineup with dissolve
    play ambience ambience_medium_crowd_outdoors fadein 4
    window show
    "Ольга толкала уже до боли знакомую речь, поэтому я на время выпал из реальности."
    window hide
    $ renpy.pause(2)

    window show
    scene bg ext_square_day with dissolve
    "Из мира грёз меня вырвала Ольга Дмитриевна."
    show mt angry panama pioneer far
    mt "Семен!"
    me "A?"
    mt "Не спать на линейке!"
    me "Есть!"
    show mt normal panama pioneer far
    th "Тело здесь, а душа далеко."
    th "Плюну я в полупьяный конвой."
    mt "Семен, запомни: пионер должен серьезно относиться к мероприятиям!"
    th "Должен, должен, должен... Бедные пионеры всем всё должны. {w}Будто микрозаймов набрали, а коллектор в лице Ольги каждый день напоминает о задолженности."
    mt "Товарищ новоприбывший, соизвольте по форме представиться лагерю!"
    hide mt
    show dv normal pioneer far at left
    show us normal pioneer far at cleft
    show mz normal glasses pioneer far
    show un normal pioneer far at cright
    show sl normal pioneer far at right
    "Я вышел из строя и встал рядом с вожатой."
    me "Меня зовут Персунов Семён Семёнович. Будем знакомы."
    th "Сотый раз будем знакомы."
    me "С некоторыми людьми я уже познакомился, с остальными, я думаю, тоже познакомлюсь, и, надеюсь, мы все найдем общий язык."
    th "Да, за столько циклов я уже успел придумать неплохой способ представиться."
    mt "Хорошо, Семён. Уже начинаешь вливаться в коллектив."
    mt "А теперь торжественное поднятие флага!"
    mt "Славя!"
    hide sl
    "Активистка кивнула Ольге и направилась к флагштоку."
    hide mz
    hide un
    hide dv
    hide us
    show mt normal panama pioneer far
    "Пока Славя поднимала флаг, я вернулся в строй."
    "Довольно быстро над статуей Генды зареял советский флаг."
    "Славя вернулась в строй."
    play sound sfx_dinner_horn_processed
    "Над лагерем разнесся звук горна."
    mt "А теперь в столовую. Шагом – марш!"
    play music music_list["no_tresspassing"] fadein 4
    th "А как же обходной?"
    th "Ладно, потом даст, наверное."
    th "Хотя раньше такой забывчивости за ней не наблюдалось."
    stop music fadeout 6
    "Мы дружно направились к месту приема пищи."
    window hide

    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_entrance_day_people
    window show
    th "\"Без сигарет и строем на обед"
    th "Одет как все и настроения нет."
    th "А на дворе сменился прошлый век,"
    th "Как будто живу уже сто лет.\""
    scene bg ext_dining_hall_near_day with dissolve
    "На деле, конечно, курево у меня было. Я же взял сигареты из автобуса."

    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 4
    "Наш заградотряд уже успел взять порции и занять места. А я нет: передо мной внаглую вклинилось несколько человек."
    th "С кем сесть?"
    "Похоже, свободных мест осталось не так много."
    play music music_list["no_tresspassing"] fadein 5
    "Те места, которые обычно пустовали, были заняты..."
    stop music fadeout 10
    "Внимательно оглядевшись я увидел несколько свободных мест в разных концах столовой."
    "У окна пустовал стул напротив Лены, у колонны одиноко сидела Мику, в центре было пустое место рядом с парочкой робототехников и в отдалении, в углу, можно было сесть рядом с местной библиотекаршей – Женей."
    "Внезапно лагерь подкидывает мне неожиданные ситуации с новыми выборами."
    window hide
    jump concrete_day2_dinner_choice

label concrete_day2_dinner_choice:
    $ day_time()
    $ persistent.sprite_time = "day"
    menu:
        "Подсесть к Лене":
            jump concrete_day2_dining_lena
        "Подсесть к Мику":
            $ dined_with_miku = True
            jump amogus
        "Подсесть к Робототехникам":
            $ dined_with_gays = True
            jump concrete_day2_dining_gays
        "Подсесть к Библиотекарше":
            $ dined_with_zhenya = True
            jump amogus





label concrete_day2_dining_lena:
    $ day_time()
    $ persistent.sprite_time = "day"
    window show
    "Подсяду к Лене, с ней поесть можно спокойно."
    "Я подошел к столику у окна."
    show un normal pioneer
    me "Привет, я подсяду?"
    un "Привет, садись."
    "Без привычного смущения, ответила Лена и вернулась к еде."
    me "Как дела?"
    un "Хорошо. {w}Правда, чуть линейку не проспала."
    me "Ольга за посещаемостью сильно следит?"
    un "Я бы так не сказала. На линейке отряд был в полном составе только в первый день и сегодня."
    me "Понял."
    window hide
    $ renpy.pause(1)

    window show
    "Я быстро покончил с завтраком."
    me "Ладно, до встречи. {w}Мне еще обходной заполнить надо."
    th "Если Ольга таки вспомнит."
    show un smile pioneer
    un "Пока."
    window hide
    jump concrete_day2_after_dining

label concrete_day2_dining_gays:
    $ day_time()
    $ persistent.sprite_time = "day"
    window show
    "Ага! {w}Гей обнаружен!"
    show gp_concrete body
    "Это ты кстати."
    window hide
    jump amogus

label concrete_day2_after_dining:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day with dissolve2
    window show
    "На крыльце меня уже ждала Ольга Дмитриевна."
    th "Вспомнишь черта – он и явится."
    show mt normal pioneer far
    show mt normal pioneer with dissolve
    me "Обходной?"
    show mt surprise pioneer far
    mt "Верно, угадал. {w}Постарайся заполнить до обеда."
    show mt normal pioneer far
    play sound sfx_paper_bag
    "Ответила Ольга Дмитриевна, протягивая мне лист бумаги."
    me "Хорошо."
    window hide
    scene ext_houses_day with dissolve
    window show
    "Обходной ничем не отличался от тех, что были в других циклах. {w}Отметиться надо было всё в тех же пунктах."
    th "С чего бы начать?"
    window hide

    $ disable_all_zones()

    $ set_zone("music_club","concrete_day2_musclub")
    $ set_zone("clubs","concrete_day2_gays")
    $ set_zone("library","concrete_day2_library")
    $ set_zone("medic_house","concrete_day2_aidpost")
    $ set_zone("forest","concrete_day2_forest")
    $ set_zone("camp_entrance", "concrete_day2_walk")
    $ set_zone("beach", "concrete_day2_beach")
    $ set_zone("sport_area", "concrete_day2_sports")


label concrete_day2_visitsheet_map:
    $ day_time()
    $ persistent.sprite_time = "day"
    stop ambience 
    if time_left <= 0:
        jump concrete_day2_after_visitsheet
    if time_left == 3:
        $ set_zone("dining_hall","concrete_day2_dinner")
    if time_left <= 2:
        $ reset_zone("dining_hall")
    if time_left <= 1:
        $ sunset_time()
        $ persistent.sprite_time = "sunset"
        $ reset_zone("medic_house")

    $ show_map()

label concrete_day2_musclub:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    play ambience ambience_ext_road_day fadein 4
    window show

    th "Пойду в музыкальный клуб."
    scene ext_musclub_day with dissolve2
    "Я постучался."
    "Ответа ждать, очевидно, не следовало – Мику же под роялем."
    scene int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 4
    "Я вошел."
    me "Есть кто живой?"
    play sound sfx_piano_head_bump
    "Из под рояля раздался стук."
    "Мику в очередной раз ударилась об него головой."
    show mi normal pioneer far
    mi "О, новенький! {w}Семен, да?0 {w}С чем пожаловал?"
    me "Да вот, обходной заполнить надо. {w}Ты Мику, да?"
    play sound sfx_paper_bag
    "Мику взяла обходной."
    mi "Верно, я Мику. {w}Наполовину японка. {w}У меня мама из Японии, а папа русский инженер."
    "Размеренно говорила Мику, опустив взгляд на обходной."
    mi "В кружок не запишешься?"
    if joined_libray:
        "А оно мне надо? {w}Я же думал в библиотеке посидеть, вместо концерта."
    elif joined_gayclub:
        "А оно мне надо? {w}Я же думал с робототехниками развлекаться."
    menu:
        "Согласиться":
            $ joined_musclub = True
            $ lp_miku += 1
            me "Да, записывай. {w}Я на гитаре играть умею. {w}Можем даже прощальный концерт в конце смены устроить."
            "На деле, запись мне нужна, чтобы иметь доступ к гитаре. {w}Люблю иногда побренчать на лодочной станции."
            show mi smile pioneer far
            mi "Замечательно! Сыграешь что-нибудь?"
            if time_left <= 0:
                me "Сейчас не могу, давай потом. Сама видишь – поздно уже."
                mi "Хорошо, буду ждать. Завтра зайдешь?"
                me "Посмотрим. {w}Пока!"
            elif not (visited_libray and visited_aidpost and visited_gayclub):
                me "Сейчас не могу, давай потом. Мне надо в остальных местах по обходному отметиться."
                mi "Хорошо, буду ждать."
                me "До связи."
            else:
                th "А почему бы и нет? {w}Я же уже отметился везде, где надо."
                me "Отчего не сыграть? Давай гитару."
                "Не дожидаясь ответа, я сам подошел к дальнему углу и взял акустическую гитару."
                "Сев на стул с гитарой наперевес, я на секунду задумался, что сыграть."
                th "Точно! Стоит сыграть музыку к ее же песне, которую я уже давно идеально выучил."
                "Я ударил по струнам..."
                play sound sfx_miku_song_learn1
                window hide
                $ renpy.pause(2)
                window show
                $ lp_miku += 1
                $ played_for_miku = True
                show mi cry_smile pioneer far
                mi "Ты услышал, как я репетирую, и сразу же настолько хорошо запомнил мелодию?"
                mi "Да ты гений! {w}Спасибо тебе большое, что согласился вступить в клуб. {w}Из нас выйдет отличный дуэт!"
                show mi smile pioneer far
                "Я смущенно посмеялся от обилия комплиментов."
                th "Уже который раз с ней разговаирваю, а все смущаюсь..."
                me "Ну ладно, у меня еще одно дело осталось. {w}Как нибудь еще зайду. {w}Пока!"
                show mi surprise pioneer far
                mi "До свидания."
                $ time_left -= 1
    
        "Отказать":
            $ joined_musclub = False
            me "Извиняй, у меня уже другие планы."
            show mi sad pioneer far
            mi "Ну ладно..."
            "Расстроилась Мику."
            me "Так, что с обходным?"
            show mi angry pioneer far
            mi "Подписала. {w}Что-то еще?"
            "Недовольно ответила она."
            me "Нет, я пойду."
            play sound sfx_paper_bag
            "Я схватил листок и быстро вышел из здания музыкального клуба."
    scene ext_musclub_day with dissolve
    play ambience ambience_ext_road_day fadein 4
    play music music_list["no_tresspassing"] fadein 4
    "На крыльце я задумался."
    if joined_musclub:
        th "Мику не \"стреляет\" пулеметными очередями из слов. {w}Лена не смущается и ведет себя более открыто."
    else:
        th "Мику не \"стреляет\" пулеметными очередями из слов, и на отказ вступить в клуб не просто расстроилась, а разозлилась... {w}Лена не смущается и ведет себя более открыто."
    th "Лагерь решил поменять характеры персонажей?"
    stop music fadeout 10
    th "Ладно, идем дальше."
    window hide

    if time_left > 0:
        jump concrete_day2_visitsheet_map
    else:
        jump concrete_day2_after_visitsheet

label concrete_day2_gays:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    $ visited_gayclub = True
    jump concrete_day2_visitsheet_map

label concrete_day2_library:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    $ visited_libray = True
    jump concrete_day2_visitsheet_map

label concrete_day2_aidpost:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    $ visited_aidpost = True
    $ reset_zone("medic_house")
    if visited_libray or visited_gayclub or visited_musclub:
        th "Теперь в медпункт."
    else:
        th "Зайду сначала в медпункт."
    scene ext_aidpost_day with dissolve2
    play ambience ambience_ext_road_day fadein 4
    "Передо мной из медпункта выскочила какая-то рыжая девочка из другого отряда."
    th "Странно, раньше никого из других отрядов в медпункте не появлялось."
    th "Ладно, не суть важно..."
    "Я постучал в дверь."
    cs "Войдите."
    scene int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 4
    show cs normal far
    me "Здравствуйте. {w}Мне бы обходной подписать."
    cs "Давай."
    cs "Меня зовут Виолетта Церновна, но пионеры обычно зовут меня Виолой. {w}Ты тоже можешь меня так звать."
    "Объясняла медсестра, выводя подпись на листке."
    play sound sfx_paper_bag
    "Она отдала мне бегунок."
    me "А осмотр никакой проходить не надо?"
    play music music_list["no_tresspassing"] fadein 4
    cs "А тебя что-то беспокоит?"
    me "Нет."
    cs "Значит не надо."
    th "Всегда же был!"
    me "Ладно... {w}Разрешите откланяться."
    cs "Заходи, если что будет беспокоить."
    scene ext_aidpost_day with dissolve
    play ambience ambience_ext_road_day fadein 4
    th "Так, становится еще интереснее..."
    stop music fadeout 10
    th "Но ладно, идем дальше."
    window hide

    if time_left > 0:
        jump concrete_day2_visitsheet_map
    else:
        jump concrete_day2_after_visitsheet

label concrete_day2_dinner:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    jump concrete_day2_visitsheet_map

label concrete_day2_forest:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    jump concrete_day2_visitsheet_map

label concrete_day2_walk:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    jump concrete_day2_visitsheet_map

label concrete_day2_beach:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    jump concrete_day2_visitsheet_map

label concrete_day2_sports:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ time_left -= 1
    jump concrete_day2_visitsheet_map

label concrete_day2_after_visitsheet:
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    window show
    "Честно говоря, я был сильно удивлен происходящим."
    th "Надо все это обдумать..."
    "Я направился в лес."
    window hide
    scene ext_path_day with dissolve2
    play ambience ambience_forest_day
    window show
    th "Что происходит с лагерем? {w}Я прожил тут уже не один виток, но ни в одном из лагерей не было столь серьезных изменений в поведении его обитателей."


    

