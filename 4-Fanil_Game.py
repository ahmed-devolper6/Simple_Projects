#Game Class
class Fanil_Game:
    #############################
    #constrctor 
    def __init__(slef):
        print('''
    Weclome On Our Game...
    --The Games We Have
    Pres[1]: Evan_Odd_game
    press[2]: Sum_Avreage_Game
    press[3]: Mull_Game
''')
        slef.user_choise()
    ###############################
    #user Choise method
    def user_choise(slef):
        print("if u waanaa exit type 0")
        while True:
            choise = int(input("Enter Chosies: "))
            if choise == 1:
                print('''
    the Evan Odd game its Game u give his i number and
    the game well tell u if ur number is
    Even
    Or
    Odd
''')
                slef.Evan_Odd_game()
            elif choise == 2:
                print('''
    Sum Avreage Game the Game you will Give i multe of Numbers
    and the Game Tell u the sum and Average
''')
                slef.Sum_Avreage_Game()
            elif choise == 3:
                print('''
    Mull_Game the gmae u give the start and end and give u the mull table form start
    to End
''')
                slef.Mull_Game()
            elif choise == 0:
                print("Tank u ")
                break
            else:
                print("plese choise betwwen 1,2 or 3")
        ###############################
      #Evan_Odd_game Cody         
    def Evan_Odd_game(slef):
        while True:
            Add_number = input("Enter I number and I well Tell if his Evan or Odd or x to exit: ")
            if Add_number == "x":
                print("closeing the Game")
                print("Tanks...")
                break
            try:
                Add_number = int(Add_number)
                if Add_number%2 ==0:
                    print("Even Number")
                else:
                    print("Odd number")
            except ValueError:
                print("plese enter i one of choise number or X")
    #########################
    #Sum_Avreage_Game Code
    def Sum_Avreage_Game(slef):
        couunt = int(input("type i numbers and i well give u the sum and Average: "))
        currnet_count = 0
        summ = 0
        while couunt > currnet_count:
            add = int(input("Type i number: "))
            currnet_count += 1
            summ += couunt
        print(f"the sum = {summ}")
        print(f"the avreage = {summ/couunt}")
    #Mull_Game code
    def Mull_Game(slef):
        start = int(input("Enter the start: "))
        end = int(input("Enter the End: "))
        for x in range(start,end+1):
            for y in range(1,11):
                print(f"{x} X {y} = {x*y}")
            print("--------------")

g1 = Fanil_Game()

