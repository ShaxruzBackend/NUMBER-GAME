from random import randint

level = input("""Salom! Son top o'yiniga xush kelibsiz\n
Bosqichni tanlang!\n
1. Easy
2. Normal
3. Hard
4. Expert
Kiriting: """).lower()

if level == "1" or level == "easy":
    bot_choice = randint(1, 5)

    for i in range(1, 4):
        user_choice = int(input("Bot 1 dan 5 gacha son o'yladi\n"
                                "Ushani toping: "))

        if user_choice == bot_choice:
            print("Ofarin\nSiz yutdingiz")
            break
        else:
            print(f"Topolmadiz {i}/3")

elif level == "2" or level == "normal":
    bot_choice = randint(1, 10)

    for i in range(1, 5):
        user = int(input("bot 1 dan 10 gacha son oylagan \n"
                         "oshani toping"))
        if user == bot_choice:
            print("ofarin \n Siz yutdingiz ")
            break

        else:
            print(f"topolmadiz {i}/4")

elif level == "3" or level == "hard":
    bot = randint(1, 15)

    for i in range(1, 7):
        user = int(input("bor 1 dan 15 gacha son tanlaydi \n"
                         "oshani toping"))
        if user == bot:
            print("ofarin siz yutdingiz")
            break
        else:
            if user > bot:
                print("kichikroq son tanlang")
            elif bot > user:
                print("kattaroq son tanlang")


elif level == "4" or level == "expert":
    boy = randint(1, 60)

    for i in range(1, 50):
        use = int(input("Bot 1 dAN 60 GACHA SON TANLAYDI \n"
                        "oshani tanland "))
        if use == boy:
            print("ofarin")
            break
        else:
            if use > boy:
                print("Kichikroq son tanlang")
            elif boy > use:
                print("Kattroq son tanlang")

else:
    print("Notugri tanlangi!")
