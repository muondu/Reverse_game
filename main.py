import datetime as time
import sqlite3

conn = sqlite3.connect('points.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS points(point INTEGER)')
now = time.datetime.now()

hour = now.hour

if hour < 12:
    print("Good morning")
elif hour > 11 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')

def input1_fuc():
    global input1
    input1 = input("Enter your name:  ")
input1_fuc()
if len(input1) > 3 or len(input1) == 3:
    def gender_input():
        global gender
        gender = input("What is your gender. Male(m) or Female(f) or Other(c):  ")
    gender_input()
    if gender == "m" or gender == "M" or gender == "male" or gender == "Male":
        def continue_game():
            global continue_gme
            continue_gme = input("Enter e to continue or enter any other key to exit the game:  ")
        continue_game()
        if continue_gme == "e" or continue_gme == "E":
            print("Welcome ",input1)
            
            def options():
                option = input("""
                Do you want to 
                a Play the game
                b See the rules
                : 
                """)
                if option == "a" or option == "A" or option == "Play the game" or option == "play the game":
                    def reverse_func(s):
                        return s == s[::-1]
                    s = input("Enter the word to check its reverse:  ")

                    answer = reverse_func(s)

                    if answer:
                        print("You get a point")

                        c.execute('INSERT INTO points VALUES(1)')
                        conn.commit()
                        
                    else:
                        print("You don't get a point")
                elif option == "b" or option == "B" or option == "See the rules" or option == "see the rules":
                    print("These are the rules.")
                    print("""
                    1. Enter the word that you think can be read forwards and backwards
                    2. if it is correct you will score 1 point.
                    3. If it is wrong you get 0 points.
                    """)
                    options()
                else:
                    print("I did not understand you. Please try again.")
                    options()
            options()
        else:
            print("Bye")
    elif gender == "f" or gender == "F" or gender == "female" or gender == "Female":
        def continue_game():
            global continue_gme
            continue_gme = input("Enter e to continue or enter any other key to exit the game:  ")
        continue_game()
        if continue_gme == "e":
            print("Welcome ",input1)
            #points = 0
            def options():
                option = input("""
                Do you want to 
                a Play the game
                b See the rules
                : 
                """)
                if option == "a" or option == "A" or option == "Play the game" or option == "play the game":
                    def reverse_func(s):
                        return s == s[::-1]
                    s = input("Enter a word:  ")

                    answer = reverse_func(s)

                    if answer:
                        print("You get a point")

                        c.execute('INSERT INTO points VALUES(1)')
                        conn.commit()
                        
                    else:
                        print("You don't get a point")
                elif option == "b" or option == "B" or option == "See the rules" or option == "see the rules":
                    print("These are the rules.")
                    print("""
                    1. Enter the word that you think can be read forwards and backwards
                    2. if it is correct you will score 1 point.
                    3. If it is wrong you get 0 points.
                    """)
                    options()
                else:
                    print("I did not understand you. Please try again.")
                    options()
            options()
        else:
            print("Bye")
            
    elif gender == "c" or gender == "C" or gender == "other" or gender == "Other":
        def continue_game():
            global continue_gme
            continue_gme = input("Enter e to continue or enter any other key to exit the game:  ")
        continue_game()
        if continue_gme == "e":
            print("Welcome ",input1)
            #points = 0
            def options():
                option = input("""
                Do you want to 
                a Play the game
                b See the rules
                : 
                """)
                if option == "a" or option == "A" or option == "Play the game" or option == "play the game":
                    def reverse_func(s):
                        return s == s[::-1]
                    s = input("Enter a word:  ")

                    answer = reverse_func(s)

                    if answer:
                        print("You get a point")

                        point = 1
                        c.execute('INSERT INTO points VALUES(?)',point)
                        conn.commit()
                        
                    else:
                        print("You don't get a point")
                elif option == "b" or option == "B" or option == "See the rules" or option == "see the rules":
                    print("These are the rules.")
                    print("""
                    1. Enter the word that you think can be read forwards and backwards
                    2. if it is correct you will score 1 point.
                    3. If it is wrong you get 0 points.
                    """)
                    options()
                else:
                    print("I did not understand you. Please try again.")
                    options()
            options()
        else:
            print("Bye")
    else:
        print("I did not understand you. Please try again.")
        gender_input()
    
else:
    print("I did not understand you. Please try again")
    input1_fuc()

