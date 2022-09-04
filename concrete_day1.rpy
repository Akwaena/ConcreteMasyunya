label concrete_createvars_day1:
    $ lp_aska = 0
    $ lp_zhenya = 0
    $ lp_miku = 0
    $ lp_gay = 0
    $ lp_hikka = 0
    jump concrete_createvars_day2

label concrete_day1:
    $ day_time()
    $ new_chapter(1, mod_name+u"День 1")
    if not vars_done:
        jump concrete_createvars_day1

    scene bg black
    $ renpy.pause(2)

    $ persistent.sprite_time = "day"
    scene bg int_bus with flash

    window show
    "Ночь.{w} Улица.{w} Фонарь.{w} Аптека."
    "Хотя в моем случае: \"Икарус. Сиденье. Остановка. Славя.\""
    "Который раз я уже здесь? Сам не знаю."
    "Впрочем, не все ли равно? Очередная неделя началась."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_center_day loop fadein 4

    "Я вышел из автобуса, прихватив из бардачка пачку Беломорканала."
    th "Скоро должна Славя подойти. Снова."
    "Я принялся ждать."
    show sl normal pioneer far
    "Через несколько минут из-за ворот показалась девочка, которую я ждал."
    show sl smile pioneer close
    sl "Привет, ты, наверное, только что приехал?"
    sl "Меня Славя зовут, вообще полное имя Славяна, но все меня Славей зовут."
    sl "И ты тоже зови!"
    me "Хорошо, а меня Семен зовут."
    sl "Приятно познакомиться."
    "Ничего не меняется. Каждый раз ее приветсятвие одно и то же."
    "Честно, лагерь, ты мог бы хоть какого-то разнообразия добавить!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day with dissolve
    show un scared pioneer far at left
    show us grin sport far at right
    $ renpy.pause(2)

    $ persistent.sprite_time = "day"
    scene bg ext_square_day with dissolve
    show sl normal pioneer far
    window show
    "Мы подошли к площади, оставив позади Ульяну и Лену. Славя объяснила мне уже давно известный маршрут до домика Ольги Дмитриевны, и я отправился отмечаться о прибытии."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day with dissolve

    window show
    "Правда, чтобы не наткнуться на ДваЧе, пришлось сделать небольшой крюк."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day with dissolve
    window show
    "Обождав, пока из домика уйдут Лена и Ульяна, я вошел."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day with dissolve
    play ambience ambience_int_cabin_day loop fadein 1
    show mt normal pioneer far
    $ renpy.pause(1)
    window show
    show mt normal pioneer close
    me "Здравствуйте, я вот только что приехал. Вы Ольга Дмитриевна?"
    show mt smile pioneer close
    mt "О, здравствуй, Семен. А мы тебя уже заждались."
    me "Да вот как-то опоздал на поезд, а следующий был только через несколько дней."
    "Эта отмазка всегда работала. Правда я не уверен, можно ли это назвать отмазкой, ведь за столько циклов я так и не смог понять, почему я приезжаю позже."
    mt "Так, жить будешь здесь, со мной, свободных домиков больше нет." 
    me "Да, без проблем. Мне не принципиально, с кем жить."
    th "Чуть не сказал, что это для меня не первый раз."
    show mt normal pioneer far
    mt "На завтрак и обед ты опоздал, но до ужина осталось еще время."
    mt "Можешь пока погулять, получить форму на складе. Tам сейчас, наверное, Славя."
    me "Принял."
    window hide

    $ persistent.sprite_time = "day"
    play ambience ambience_camp_center_day loop fadein 4
    scene bg ext_house_of_mt_day with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg ext_warehouse2_day_concrete with dissolve
    window show
    "Улица.{w} Склад.{w} Славяна.{w} Форма."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_warehouse_day_concrete with dissolve
    show sl normal pioneer
    window show
    "Зайдя на склад, я увидел Славю."
    show sl smile pioneer close
    me "Привет еще раз. Мне бы форму."
    sl "Да-да, сейчас."
    hide sl
    show sl smile pioneer close with dissolve2
    "Через минуту поисков по полкам она вернулась с комплектом."
    hide sl
    "Она вышла со склада, а я принялся надевать форму, заведомо зная, что она мне подойдет."
    window hide

    stop music
    window show
    play music music_list["no_tresspassing"]
    $ renpy.pause(1)
    "Что-то пошло не так, рубашка оказалась мне мала в плечах."
    stop music fadeout 5
    play ambience ambience_camp_center_day loop fadein 4

    th "Странно..."
    th "Лагерь иногда \"баговал\", но это было связано с происходящими событиями, но никак не с размером формы. Или это уже Славя \"багует\"?"
    "Славя тихо скользнула в комнату."
    show sl surprise pioneer
    sl "Что-то не так с формой?"
    me "Да, рубашка в плечах узкая."
    show sl smile pioneer
    sl "Ничего страшного, сейчас поменяем!"
    "Сказала она, направляясь к штапелю с формой."
    show blinking
    "Славя выдала новую, которая мне подошла."
    "Поблагодарив ее, я направился в столовую."
    th "Интересно. Ошибок с формой у меня еще не было. Да и вообще ошибки с одеждой – редкость."
    th "Ладно, не стоит на этом зацикливаться."
    window hide

    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_dining_hall_away_sunset with dissolve
    window show
    th "А вот и столовая. И Ульяна со своим розыгрышем. Опять. Хотя переиграть ее можно, в принципе, без проблем, бояться нечего."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full loop fadein 2
    window show
    "Минуя толпу, я вошел взял порцию и направился за стол к Алисе и Ульяне."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_people_day with dissolve
    show dv normal pioneer2 close at left
    show us smile pioneer close at right
    window show
    me "Я вас категорически приветствую! Разрешите присесть?"
    dv "О, новичок. Ну садись, раз пришел."
    "Я сел и специально отвернулся, дабы не затягивать шутку Ульяны."
    hide dv
    hide us
    "Немного подождав, повернулся назад."
    show dv normal pioneer2 close at left
    show us smile pioneer close at right
    "Обе девочки, казалось, были заняты поеданием ужина."
    window hide

    $ persistent.sprite_time = "sunset"
    scene cg d1_food_normal with dissolve
    window show
    "Котлета на месте. Ульяна сосредоточенно расправляется с пюре."
    "Так, давай по новой, Сёма."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Я отвернулся еще раз и принялся разглядывать столовую."
    window hide
    show dv grin pioneer2 close at left
    show us smile pioneer close at right
    dv "Эй, ты чего там так пристально высматриваешь?"
    me "А? Да, высматриваю местного вертухая."
    dv "Панамку, что ли? Зачем?"
    me "Знаешь, где враг – больше шансов на него не нарваться."
    dv "О, наш человек!"
    me "Я не наш, я собственный."
    show dv normal pioneer2 close at left
    "Алиса лишь хмыкнула и уткнулась в тарелку."
    window hide

    $ persistent.sprite_time = "sunset"
    scene cg d1_food_normal with dissolve
    window show
    "К слову, о тарелках: как с котлетой вопрос обстоит?"
    "На месте."
    "А под котлетой?"
    "Лишь одинокое пюре, к которому не пришла лучшая подруга – сороконожка."
    "Ну, может, это поблажка от лагеря какая-нибудь, не буду заморачиваться."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Мирно съев положеные поварихой и ГОСТом калории, я вышел из столовой."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening loop fadein 4
    window show
    "Так, и что делать? Бег за Мелкой уже не вариант."
    "Пляж? Вариант."
    "Я направился в домик за плавками."
    window hide


    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg ext_house_of_mt_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_day loop fadein 1
    scene bg int_house_of_mt_day with dissolve
    window show
    "Схватив плавки, я сразу развернулся и зашагал в сторону пляжа."
    window hide

    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_day loop fadein 4
    scene bg ext_house_of_mt_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg ext_beach_sunset with dissolve
    play ambience ambience_lake_shore_evening loop fadein 4
    window show
    "Через несколько минут я уже лежал на песке, прикрыв глаза, погруженный в свои мысли."
    window hide

    show blink
    $ persistent.sprite_time = "sunset"
    scene bg black with dissolve
    window show
    th "Вообще везет Ульянам из моих лагерей, ведь я на эту шутку с сороконожкой реагирую еще спокойно. Будь на моем месте Пионер, он бы устроил ей адские пытки, не снившиеся средневековым палачам."
    th "Да, Пионер вообще странный человек. Когда мы только познакомились, он только и делал, что пугал меня и ставил палки в колеса. Но сейчас считает меня своим единственным другом."
    th "Возможно, это потому, что я один из немногих Семенов, который не испугался его рассказов про пытки. Может, тогда он и стал считать меня своим другом."
    window hide

    play sound sfx_punch_medium
    window show
    "Внезапно, без объявления войны, меня окатило холодом."
    "Спустя несколько секунд оцепенения я открыл глаза и обнаружил довольных Алису и Ульяну."
    hide blink
    show unblink
    scene bg ext_beach_sunset with dissolve
    hide blink
    show dv grin swim at cright
    show us grin swim at cleft
    me "Это что такое?"
    us "Штрафная!"
    me "Не было штрафного, ты была в офсайде."
    show us surp2 swim at cleft
    us "Где я была?"
    me "Ладно, забей."
    show blink
    scene bg black with dissolve
    hide blink
    "Я опять лег на спину и закрыл глаза."
    window hide

    window show
    dv "М-да, я ожидала нечто более интересное... "
    dv"Что, девочку маленькую испугался?"
    me "Интересное? Хочешь пойти по пути Бисмарка?"
    dv "Это как?"
    me "На дно."
    dv "Полагаешь, несчастный, что меня сможет потопить такой как ты? Или ты думаешь, что я готова занять твое место?"
    me "Да."
    us "Не надо топиться, давайте лучше наперегонки плавать!"
    th "Идеальная возможность свалить."
    "Я открыл глаза."
    $ persistent.sprite_time = "sunset"
    scene bg ext_beach_sunset
    show dv grin swim at cleft
    show us grin swim at cright
    hide blink
    hide unblink
    show unblink
    window hide

    window show
    "И встал."
    me "А давайте. Заходим в воду и по команде плывем до буйков."
    dv "Заметано."
    hide dv
    hide us
    "Мы зашли в воду."
    me "Раз!"
    me "Два!"
    me "Старт!"
    "Алиса и Ульяна поплыли к импровизированному финишу, а я под шумок собрал свои вещи и ушел с пляжа."
    th "Лучший способ не проиграть в соревнованиях – не участвовать в них."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset with dissolve
    play ambience ambience_ext_road_night loop fadein 3
    window show
    "Я направился в свое привычное место обитания – зеленый домик с треугольной крышей."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset with dissolve
    window show
    "По пути я заметил пионерку вдалеке. Она выглядела потерянной, но точно разглядеть ее не удалось, потому что она быстро скрылась из виду."
    window hide


    $ persistent.sprite_time = "sunset"
    scene bg ext_house_of_mt_sunset with dissolve
    $ renpy.pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_sunset with dissolve
    play ambience ambience_int_cabin_day loop fadein 1
    window show
    "Без проблем добравшись до домика, я завалился на кровать."
    th "Вообще, сходить на пляж и не искупаться – это мощно. А ходил ли я на пляж в первый день? Да и случалось ли со мной когда-нибудь такое, чтобы меня обливали водой?"
    "Вопрос риторический."
    th "Поспать, что-ли?"
    show blinking
    "..."
    show blink
    scene bg black
    hide blink
    window hide
    $ renpy.pause(5)

    scene bg int_house_of_mt_night with flash
    $ night_time()
    hide unblink
    show unblink
    $ persistent.sprite_time = "night"
    window show
    "Проснулся я от яркого света, режущего глаза."
    "Стрелка часов приближалась к половине одиннадцатого."
    "Ольга сидела на соседней койке и спокойно читала книгу."
    th "Пройтись было бы неплохо."
    show mt grin pioneer far
    me "Ольга Дмитриевна, я немного погуляю перед сном?"
    mt "Иди, суслик, только недолго." 
    window hide

    scene ext_house_of_mt_night with dissolve
    play ambience ambience_ext_road_night
    window show
    "Я аккуратно вышел из домика."
    window hide

    scene ext_square_night with dissolve
    window show
    "Ноги сами вывели меня на площадь. Генда все также молча наблюдал за лагерем."
    me "Все хорошо, командующий Икари! Синдзи залез в робота!"
    "Вообще раньше я не замечал, но через некоторое количество витков понял, что партийный дятель, увековеченный в камне, это главнокомандующий NERV."
    un "Что?"
    "Честно, меня это напугало. Я как-то подзабыл о Лене, которая на ночь глядя любит почитать на площади."
    show un surprise pioneer
    me "Да ничего, мысли в слух. Ты Лена, да?"
    th "Ой, ну будто ты не знаешь."
    show un normal pioneer
    un "Все так."
    me "А я Семен. Только сегодня приехал."
    th "Угу, только сегодня."
    un "Да, я слышала."
    me "Что читаешь? \"Унесенные Ветром\"?"
    play music music_list["no_tresspassing"] fadein 5
    un "Нет, \"Двенадцать Стульев\"."
    th "Что? Всегда же \"Унесенные Ветром\" читала..."
    me "Хорошая книга, интересная. Ладно, бывай, я спать пойду. Да и тебе не советую засиживаться."
    show un normal pioneer far at left
    un "Спокойной ночи."
    window hide

    hide un
    window show
    th "Ладно, я, может, некоторые моменты стал забывать..."
    stop music fadeout 5
    th "А в целом, разве это что-то меняет? Ну книжка и книжка."
    window hide

    scene ext_house_of_mt_night_without_light with dissolve
    window show
    "В домике не горел свет."
    window hide

    scene int_house_of_mt_night2 with dissolve
    window show
    "Аккуратно, чтобы не разбудить Ольгу, я дошел до кровати и завалился спать."
    window hide
    show blink
    $ renpy.pause(1)

    jump concrete_day2










