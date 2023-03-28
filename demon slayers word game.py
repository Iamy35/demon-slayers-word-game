
import random
demon_slayers_chars_names = ["shinobu", "tanjiro", "zenitsu", "nezuko", "inosuke", "giyu", "sabito", "makomo", "kyojuro"]
game_find_list = []
game_points = 0 # bu sum gibi hepsi toplanacaktır.
correct_letter_point = 2 # bu sürekli sayı yazılmasının önüne geçilmesi içindir.
incorrect_letter_point = -4
the_menu_choice = 0
the_old_number = 999
while the_menu_choice != 2:
    game_number_char_choice = random.randint(0, len(demon_slayers_chars_names) - 1)
    the_old_number = game_number_char_choice
    char_length = demon_slayers_chars_names[game_number_char_choice]
    your_char = demon_slayers_chars_names[game_number_char_choice] # bu yukardan cıkan karakter.
    error_count = len(your_char) // 2 # bu oyun hakkımız.
    print("--------------------")
    print("1-- Start game")
    print("2 - exit ")
    print("-------------------")
    the_menu_choice = int(input("please type what you want."))
    if the_menu_choice == 1:
        for j in char_length:
            game_find_list.append("_") # bu oyunda gosterilecek bilinmeyen kelime olusturma yeri.
        for j in range(len(game_find_list)):
            print(game_find_list[j])
        print("This is your word, player.")
        print("You have to type a letter on your keyboard (excluded Turkish unique letters)")
        print("When it is in your word, the letters will show you up.")
        print("Unless, you lose your points.")
        print("Your point will multipy with your correct answers.")
        print("Good luck, player. :D")
        while error_count != 0:
            print("your rest quess--->{0}".format(error_count))
            one_letter = input("Type a letter")
            one_letter = one_letter.lower()
            if "_" not in game_find_list:
                print("Your game word has already found.")
                print("your points ---> {0}, your rest guess --->{1}".format(game_points, error_count))
                game_points = 0
                game_find_list = []
                break
            elif one_letter in your_char:
                print("You found a letter.")
                game_points = game_points + correct_letter_point
                if one_letter in "aeuio":
                    game_points = game_points + 1 # sesli harf ise 1 eklendi.
                for word in range(len(your_char)):
                    if one_letter == your_char[word]:
                        game_find_list[word] = one_letter
                    else:
                        continue
                for new in range(len(game_find_list)):
                    print(game_find_list[new])
                print("your points ---->{0}, your rest quess --->{1}".format(game_points, error_count))
            else:
                print("This letter is not in your game word, player.")
                print("Try again please.")
                game_points = game_points + incorrect_letter_point
                error_count = error_count - 1
                print("your points ---->{0}, your rest quess --->{1}".format(game_points, error_count))
    elif the_menu_choice == 2:
        the_menu_choice = 2
        print("Exiting...")
        break
    else:
        print("please type it correctly")
        continue








