#Student Grading System

def showGradings():
    print("_______________________________\nSTUDENT GRADING SYSTEM DETAILS:\n-------------------------------")

    print("96 --- 100 (A1) -> Excellent")
    print("86 --- 95  (B2) -> Very Good")
    print("76 --- 85  (B3) -> Good")
    print("66 --- 75  (C4) -> Credit")
    print("56 --- 65  (C5) -> Credit")
    print("46 --- 55  (C6) -> Credit")
    print("36 --- 45  (D7) -> Pass")
    print("26 --- 35  (E8) -> Pass")
    print("0  --- 25  (F9) -> Fail")

showGradings()

def mygrades():
        try:
                name = input("\nEnter your full name: ")
                yourclass = input("Enter your class: ")
                score = int(input("Enter your score: "))
                
                print("------------------------------")
                print("\nWelcome: ",name)
                print("Your class is: ",yourclass)
                print("Your Score is: ",score)
                       
                if score <= 25: print("(F9) - Fail")
                elif score >= 101: print("Invalid Score! Your score should be between 1 to 100")

                elif score == 26 or score <= 35: print("Your Grade is: (E8) - Pass")
                elif score == 36 or score <= 45: print("Your Grade is: (D7) - Pass")
                elif score == 46 or score <= 55: print("Your Grade is: (C6) - Credit")
                elif score == 56 or score <= 65: print("Your Grade is: (C5) - Credit")
                elif score == 66 or score <= 75: print("Your Grade is: (C4) - Credit")
                elif score == 76 or score <= 85: print("Your Grade is: (B3) - Good")
                elif score == 86 or score <= 95: print("Your Grade is: (B2) - Very Good")
                elif score == 96 or score <= 100: print("Your Grade is: (A1) - Excellent")
                else: print("Error occured!")
        except: 
                
                print("--------------------------------------------------------------------")
                print("Something went wrong! Make sure you fill in all the correct details.")
                print("--------------------------------------------------------------------")

mygrades()
