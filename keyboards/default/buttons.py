from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 O'zbek adabiyoti"),
            KeyboardButton(text="📚 Jahon adabiyoti")
        ],
        [
            KeyboardButton(text="📚 Bolalar adabiyoti"),
            KeyboardButton(text='📚 Mumtoz adabiyot')
        ],
        [
            KeyboardButton(text="🎧 Audio kitoblar"),
            KeyboardButton(text="💯 Top 100 kitoblar")
        ],
        [
            KeyboardButton(text="📚 Maktab darsliklari"),
            KeyboardButton(text="📚 Islomiy kitoblar")
        ],
        [
            KeyboardButton(text="🔍 Lug'atlar"),
            KeyboardButton(text="🔍 O'zbek tilining imlo lug'ati")
        ],
        [
            KeyboardButton(text="📝 She'riyat"),
            KeyboardButton(text="📜 Alisher Navoiy asarlari")
        ],
        [
            KeyboardButton(text="📜O'zbekiston Milliy Ensiklopediyasi"),
            KeyboardButton(text="📋 O'zbek tilining izohli lug'atlari")
        ],
        [
            KeyboardButton(text="Islom Karimov asarlari"),
            KeyboardButton(text="Shavkat Mirziyoyev asarlari")
        ],
        [
            KeyboardButton(text="📥 Kitob o'qish uchun dasturlar")
        ],
        [
            KeyboardButton(text="Wikipediyaga kirish")
        ],
        [
            KeyboardButton(text="🧑‍💻 Dasturchi"),
        ],

        [
            KeyboardButton(text="🤖 Botni guruhga qo'shish"),
            KeyboardButton(text="↗️ Botni do'stlarga ulashish")

        ],
    ],
    resize_keyboard=True,
)
wikipediya_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Chiqish"),
        ]
    ],
    resize_keyboard=True,
)
eng_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Grammatika"),
            KeyboardButton(text="📚 IELTS"),
        ],




        [
            KeyboardButton(text="📚 Vocabulary"),
            KeyboardButton(text="📚 Testlar"),
        ],



        [
            KeyboardButton(text="📚 Fiction Books")
        ],
        [
            KeyboardButton(text="🇬🇧 Ingliz tilidan foydali kanallar")
        ],




        [
            KeyboardButton(text="Go Back")
        ],



    ],
    resize_keyboard=True,
)
uzb_lit=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Abdulla Qodiriy"),
            KeyboardButton(text="👤 Cho'lpon"),
        ],
        [
            KeyboardButton(text="👤 Oybek"),
            KeyboardButton(text="👤 G'afur G'ulom"),
        ],
        [
            KeyboardButton(text="👤 Abdulla Qahhor"),
            KeyboardButton(text="👤 Said Ahmad"),
        ],
        [
            KeyboardButton(text="👤 O'tkir Hoshimov"),
            KeyboardButton(text="👤 Pirimqul Qodirov"),
        ],
        [
            KeyboardButton(text="👤 Asqad Muxtor"),
            KeyboardButton(text="👤 Odil Yoqubov"),
        ],
        [
            KeyboardButton(text="👤 Tog'ay Murod"),
            KeyboardButton(text="👤 Tohir Malik"),

        ],
        [
            KeyboardButton(text="👤 O'lmas Umarbekov")
        ],
        [
            KeyboardButton(text="Go Back"),
        ]
    ],
    resize_keyboard=True,
)

jahon_adabiyoti=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Lev Tolstoy"),
            KeyboardButton(text="👤 Aleksandr Pushkin")
        ],
        [
            KeyboardButton(text="👤 Fyodor Dostoyevskiy"),
            KeyboardButton(text="👤 Mixail Bulgakov")
        ],
        [
            KeyboardButton(text="👤 Chingiz Aytmatov"),
            KeyboardButton(text="👤 Nodar Dumbadze")

        ],
        [
            KeyboardButton(text="👤 Jek London"),
            KeyboardButton(text="👤 Gabriel Garsia Markes")
        ],
        [
            KeyboardButton(text="👤 Alber Kamyu"),
            KeyboardButton(text="👤 Kobo Abe")
        ],
        [
            KeyboardButton(text="👤 Lao She"),
            KeyboardButton(text="👤 Artur Konan Doyl")
        ],
        [
            KeyboardButton(text="👤 Agata Kristi"),
            KeyboardButton(text="👤 Gi De Mopassan")
        ],
        [
            KeyboardButton(text="👤 Onor De Balzak"),
            KeyboardButton(text="👤 Ernest Xeminguey")
        ],
        [
            KeyboardButton(text="👤 Jeyms Joys"),
            KeyboardButton(text="👤 Jonatan Svift")
        ],
        [
            KeyboardButton(text="👤 Jyul Vern"),
            KeyboardButton(text="👤 Somerset Moem")
        ],
        [
            KeyboardButton(text="👤 Robindranat Tagor")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ]
)
bolalar_adabiyoti=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Ertaklar")
        ],
        [
            KeyboardButton(text="🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)
mumtoz_adabiyot=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📓 Boburnoma")
        ],
        [
            KeyboardButton(text="📓 Shohnoma")
        ],
        [
            KeyboardButton(text="📓 Zarbulmasal")
        ],
        [
            KeyboardButton(text="📓 To'rt ulus tarixi")
        ],
        [
            KeyboardButton(text="📓 Devoni lug'otut turk")
        ],
        [
            KeyboardButton(text="📓 Qutadg'u bilig")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)

audio_kitob=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek adabiyoti")
        ],
        [
            KeyboardButton(text="🌐 Jahon adabiyoti")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)
uzb_audio=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Romanlar")
        ],
        [
            KeyboardButton(text="Qissalar")
        ],
        [
            KeyboardButton(text="Hikoyalar")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)
uzb_romanlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Abdulla Qodiriy - "O\'tkan kunlar"')
        ],
        [
            KeyboardButton(text='Abdulla Qodiriy - "Mehrobdan chayon"')

        ],
        [
            KeyboardButton(text='Oybek - "Navoiy"')
        ],
        [
            KeyboardButton(text='Pirimqul Qodirov - "Yulduzli tunlar"')
        ],
        [
            KeyboardButton(text='Said Ahmad - "Ufq"')
        ],
        [
            KeyboardButton(text='Tohir Malik - "Shaytanat"')
        ],
        [
            KeyboardButton(text='Cho\'lpon - "Kecha va kunduz"')
        ],
        [
            KeyboardButton(text="O'zbek adabiyotiga qaytish")
        ],

    ],
    resize_keyboard=True,
)

uzb_qissa_audio=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="""G'afur G'ulom - "Shum bola" .""")
        ],
        [
            KeyboardButton(text='Tog\'ay Murod - "Yulduzlar mangu yonadi"')

        ],
        [
            KeyboardButton(text='Tohir Malik - "Alvido bolalik"')
        ],
        [
            KeyboardButton(text='O\'tkir Hoshimov - "Dunyoning ishlari"')
        ],
        [
            KeyboardButton(text="O'zbek adabiyotiga qaytish")
        ],

    ],
    resize_keyboard=True,
)

uzb_qissa=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=""" G'afur G'ulom - "Shum bola" """)
        ],
        [
            KeyboardButton(text='Tog\'ay Murod - "Yulduzlar mangu yonadi"')

        ],
        [
            KeyboardButton(text='Tohir Malik - "Alvido bolalik"')
        ],
        [
            KeyboardButton(text='O\'tkir Hoshimov - "Dunyoning ishlari"')
        ],
        [
            KeyboardButton(text="Go Back")
        ],

    ],
    resize_keyboard=True,
)


jahon_adabiyoti_rus=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Romanlar")
        ],
        [
            KeyboardButton(text="🌐 Qissalar")
        ],
        [
            KeyboardButton(text="🌐 Hikoyalar")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)

jahon_roman_audio=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'nta negir bolasi")
        ],
        [
            KeyboardButton(text="Dengiz sarguzashtlari")
        ],
        [
            KeyboardButton(text="Graf Monte Kristo")
        ],
        [
            KeyboardButton(text="O'gay ona")
        ],
        [
            KeyboardButton(text="Jahon adabiyotiga qaytish")
        ]
    ],
    resize_keyboard=True,
)
jahon_qissa_audio=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Chingiz Aytmatov - "Jamila"')
        ],
        [
            KeyboardButton(text='Paulo Koelo - "Alkimyogar"')
        ],
        [
            KeyboardButton(text='Chingiz Aytmatov - "Chingizxonning oq buluti"')

        ],
        [
            KeyboardButton(text="Jahon adabiyotiga qaytish")
        ]
    ],
    resize_keyboard=True,
)


maktab_darsliklari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha")
        ],
        [
            KeyboardButton(text="🔄️ Yangi nashr")
        ],
        [
            KeyboardButton(text="🇷🇺 Ruscha")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)

uzb_maktab_darsliklari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔢 Sinflar bo'yicha")
        ],
        [
            KeyboardButton(text="📔 Fanlar bo'yicha")
        ],
        [
            KeyboardButton(text="Maktab darsliklariga qaytish")
        ]
    ],
    resize_keyboard=True,
)


uzb_maktab_darsliklari_sinflar_buyicha=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📗 1-sinf")
        ],
        [
            KeyboardButton(text="📗 2-sinf")
        ],
        [
            KeyboardButton(text="📗 3-sinf")
        ],
        [
            KeyboardButton(text="📗 4-sinf")
        ],
        [
            KeyboardButton(text="📗 5-sinf")
        ],
        [
            KeyboardButton(text="📗 7-sinf")
        ],
        [
            KeyboardButton(text="📗 8-sinf")
        ],
        [
            KeyboardButton(text="📗 9-sinf")
        ],
        [
            KeyboardButton(text="📗 10-sinf")
        ],
        [
            KeyboardButton(text="📗 11-sinf")
        ],
        [

            KeyboardButton(text="Orqaga")
        ],

    ],
    resize_keyboard=True,
)

uzb_maktab_darsliklari_fanlar_buyicha=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Ona tili")
        ],
        [
            KeyboardButton(text="📚 Adabiyot")
        ],
        [
            KeyboardButton(text="🇬🇧 Ingliz tili")
        ],
        [
            KeyboardButton(text="🇩🇪 Nemis tili")
        ],
        [
            KeyboardButton(text="🇫🇷 Fransuz tili")
        ],
        [
            KeyboardButton(text="🇷🇺 Rus tili")
        ],
        [
            KeyboardButton(text="🗺 Geografiya")
        ],
        [
            KeyboardButton(text="🔍 Tarix")
        ],
        [
            KeyboardButton(text="🔬 Fizika")
        ],
        [
            KeyboardButton(text="🔢 Matematika")
        ],
        [
            KeyboardButton(text="🩺 Biologiya")
        ],
        [
            KeyboardButton(text="🌡 Kimyo")
        ],
        [
            KeyboardButton(text="🏃‍♂ Jismoniy tarbiya")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True,
)
ru_maktab_darsliklari=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔢 Sinflar bo'yicha 🇷🇺")
        ],
        [
            KeyboardButton(text="Maktab darsliklariga qaytish")
        ]
    ],
    resize_keyboard=True,
)
ru_maktab_darsliklari_sinflar_buyicha=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📙 1-sinf")
        ],
        [
            KeyboardButton(text="📙 2-sinf")
        ],
        [
            KeyboardButton(text="📙 3-sinf")
        ],
        [
            KeyboardButton(text="📙 4-sinf")
        ],
        [
            KeyboardButton(text="📙 5-sinf")
        ],
        [
            KeyboardButton(text="📙 6-sinf")
        ],
        [
            KeyboardButton(text="📙 7-sinf")
        ],
        [
            KeyboardButton(text="📙 8-sinf")
        ],
        [
            KeyboardButton(text="📙 9-sinf")
        ],
        [
            KeyboardButton(text="📙 10-sinf")
        ],
        [
            KeyboardButton(text="📙 11-sinf")
        ],
        [

            KeyboardButton(text="Rus darsliklariga qaytish")
        ],

    ],
    resize_keyboard=True,
)


islomiy_kitoblar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tafsiri Hilol"),
            KeyboardButton(text="Jannat vasfi")
        ],
        [
            KeyboardButton(text="Keng rizq va baraka omillari")
        ],
        [
            KeyboardButton(text="Istig'forning 40 xosiyati | Salovotlar")
        ],
        [
            KeyboardButton(text="Qur'on - qalblar shifosi")
        ],
        [
            KeyboardButton(text="Baxtli hayot sari")
        ],
        [
            KeyboardButton(text="Payg'ambar uyida bir kun")
        ],
        [
            KeyboardButton(text="Shamoili Muhammadiy")
        ],
        [
            KeyboardButton(text="Abu Bakr Siddiq")
        ],
        [
            KeyboardButton(text="Sunani Termiziy")
        ],
        [
            KeyboardButton(text="Hazrati Umar ibn Xattob")
        ],
        [
            KeyboardButton(text="Musnad")
        ],
        [
            KeyboardButton(text="Mukoshafat-ul qulub")
        ],
        [
            KeyboardButton(text="Ramazon va taqvo")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)
lugatlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗂 Pdf lug'atlar"),
            KeyboardButton(text="📲 Apk lug'atlar")
        ],
        [
            KeyboardButton(text="🌐 Google tarjimon")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)

sheriyat=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Erkin Vohidov"),
            KeyboardButton(text="👤 Abdulla Oripov")
        ],
        [
            KeyboardButton(text="👤 Rauf Parfi"),
            KeyboardButton(text="👤 Shavkat Rahmon")
        ],
        [
            KeyboardButton(text="👤 Muhammad Yusuf")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,

)


kitob_uqish_uchun_dasturlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📒 Pdf kitoblar uchun")
        ],
        [
            KeyboardButton(text="📒 Djvu kitoblar uchun")
        ],
        [
            KeyboardButton(text="📒 Epub kitoblar uchun")
        ],
        [
            KeyboardButton(text="📒 Zip kitoblar uchun")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True,
)





baholash=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="""⭐️⭐️⭐️⭐️⭐️ | A'lo""")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️⭐️️ | Yaxshi")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️️️ | O'rtacha")
        ],
        [
            KeyboardButton(text="⭐️⭐️ | Qoniqarli")
        ],
        [
            KeyboardButton(text="⭐️ | Qoniqarsiz")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True,
)


taklif=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Done")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True,
)

wikipediya=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ]
)
yangi_nashr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-sinf 📗")
        ],
        [
            KeyboardButton(text="2-sinf 📗")
        ],
        [
            KeyboardButton(text="3-sinf 📗")
        ],
        [
            KeyboardButton(text="4-sinf 📗")
        ],
        [
            KeyboardButton(text="5-sinf 📗")
        ],
        [
            KeyboardButton(text="6-sinf 📗")
        ],
        [
            KeyboardButton(text="7-sinf 📗")
        ],
        [
            KeyboardButton(text="8-sinf 📗")
        ],
        [
            KeyboardButton(text="9-sinf 📗")
        ],
        [
            KeyboardButton(text="10-sinf 📗")
        ],
        [
            KeyboardButton(text="11-sinf 📗")
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)
