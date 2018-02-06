def tic_tac_toe():
    board=[9,8,7,6,5,4,3,2,1]
    end=False
    win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8))	
    def draw():
         print("|",b[0],"|",b[1],"|",b[2],"|")
         print("|",b[3],"|",b[4],"|",b[5],"|")
         print("|",b[6],"|",b[7],"|",b[8],"|")
         print()
    def p1():
        n=("choose a num from 1 to 9")
        if b[n]=="x" or b[n]=="o":
            print("choose another digit")
            p1()
        else:
            b[n]=="x"
    def p2():
         n=("choose a num from 1 to 9")
         if b[n]=="x" or b[n]=="o":
             print("choose another digit")
             p2()
         else:
             b[n]=="o"
            
print tic_tac_toe()  
