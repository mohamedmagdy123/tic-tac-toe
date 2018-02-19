def tic_tac_toe():
    b=[0,1,2,3,4,5,6,7,8,9]
    end=False
    win=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9))
    def draw():
        print ("|",b[7],"|",b[8],"|",b[9],"|")
        print ("-------------")
        print ("|",b[4],"|",b[5],"|",b[6],"|")
        print ("-------------")
        print ("|",b[1],"|",b[2],"|",b[3],"|")
    def choose_number():
        while True:
            while True:
                a=input()
                a=int(a)
                if a in range(10):
                    return a
                else:
                    print("\nplease choose a number from 1 to 9 ")
    def p1():
        n= choose_number()
        if b[n]== "X" or b[n]=="O":
            print ("\n select another number")
            draw()
            p1()
        else:
            b[n]="X"
    def p2():
        n=choose_number()
        if b[n]=="X" or b[n]=="O":
            print ("\n select another number")
            draw()
            p2() 
        else:
            b[n]="O"
    def board():
        count = 0
        for a in win:
            if b[a[0]] == b[a[1]] == b[a[2]] == "X":
                print("Player 1 Wins!\n")
                return True
            if b[a[0]] == b[a[1]] == b[a[2]] == "O":
                print("Player 2 Wins!\n")
                return True
        for a in range(10):
            if b[a] == "X" or b[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True
    while not end:
        draw()
        end=board
        if end==True:
            break
        print("player1,choose where to place X")
        p1()
        draw()
        end=board()
        if end==True:
            break
        print("player2,choose where to place O")
        p2()
    yes="yes"
    no="no"
    if input("play again (yes/no)\n")==yes:
        tic_tac_toe()
    else:
        return False
tic_tac_toe()

        
