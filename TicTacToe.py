row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']


def display():
    print(" {} | {} | {} ".format(row1[0],row1[1],row1[2]))
    print("-----------")
    print(" {} | {} | {} ".format(row2[0],row2[1],row2[2]))
    print("-----------")
    print(" {} | {} | {} ".format(row3[0],row3[1],row3[2]))
    print("")

def checkWinner(xOrO):
    #rows
    if row1[0] == xOrO and row1[1]==xOrO and row1[2]==xOrO:
        return True

    if row2[0] == xOrO and row2[1]==xOrO and row2[2]==xOrO:
        return True
    
    if row3[0] == xOrO and row3[1]==xOrO and row3[2]==xOrO:
        return True

    #columns
    if row1[0] == xOrO and row2[0]==xOrO and row3[0]==xOrO:
        return True
    
    if row1[1] == xOrO and row2[1]==xOrO and row3[1]==xOrO:
        return True

    if row1[2] == xOrO and row2[2]==xOrO and row3[2]==xOrO:
        return True
    
    #diagonals
    if row1[0] == xOrO and row2[1]==xOrO and row3[2]==xOrO:
        return True

    if row1[2] == xOrO and row2[1]==xOrO and row3[0]==xOrO:
        return True
    return False

def insertInto(location, xOrO):

    #Checking top row
    if 0< location <4:
        location = location -1
        if row1[location] != ' ':
            return False
        row1[location] = xOrO
        return True

    #Checking Middle row
    elif 3< location <7:
        location = location -4
        if row2[location] != ' ':
            return False
        row2[location] = xOrO
        return True

    #Checking bottom row
    else:
        location = location -7
        if row3[location] != ' ':
            return False
        row3[location] = xOrO
        return True

def getInput(xOrO):
    check = False
    first = True
    errorMessage = ""
    while not check:
        
        #Checking if this is first input
        if first:
            ans = input("Please Enter a value between 1-9:\n")
            first = False
        else:
            ans = input(errorMessage)

        #Checking if input value is an int
        if ans.isdigit()==False:
            errorMessage ="Please enter an integer value:\n"
            continue
        ans = int(ans)

        #Checking if value is from 1-9
        if not(0<ans<10):
            errorMessage="Please Enter a Value from 1-9:\n"
            continue

        #Checking to see if spot is taken
        if not insertInto(ans, xOrO):
            errorMessage ="This position is already taken. Please Enter another:\n"
            continue
        break

    


def playerOne():
   getInput("X")

def playerTwo():
   getInput("O")

def gameLoop():
    count =0
    while True:
        display()
        playerOne()
        count=count+1
        if count ==9:
            print("Cats game\n")
            break
        display()
        if checkWinner("X"):
            print("Player 1 Wins!\n")
            break
        playerTwo()
        count=count+1
        display()
        if checkWinner("O"):
            print("Player 2 Wins!\n")
            break
        if count ==9:
            print("Cats game\n")
            break

while True:
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    print("New Game:")
    print("Player one will be X and Player 2 will be 0")
    print("Enter a number from 1-3 for first row, 4-6 for second row, and 7-9 for third row\n")
    gameLoop()
