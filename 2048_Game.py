import random
#Initialize final state
final=False

def start():
    #initialize empty grid
    grid=[['-' for i in range(4)] for j in range(4)]

    #Add 2 at two random locations.
    for k in range(2):
            n1 = random.randint(0, 3)
            n2 = random.randint(0, 3)
            grid[n1][n2]=str(2)
    print("Initial Grid\n")
    printgrid(grid)
    movedirection=['1','2','3','4','5']
    points=0
    while True:
        print("Enter 1 for Left\nEnter 2 for Bottom\nEnter 3 for rigjt\nEnter 4 for Top\nEnter 5 for Quit\n")
        currentmovedirection=input()

        #Check for the Valid Input
        if currentmovedirection in movedirection:
            if currentmovedirection!='5':
                grid,points=currentmove(grid,int(currentmovedirection)-1,points)
                grid,currentstate1=addnewnumber(grid)
                printgrid(grid)
                if final:
                    print("!!Congratulations!! You Won\nTotal points", points)
                    break
                if not currentstate1:
                    print("Game Over There are No empty Locations\nTotal points",points)
                    break

                print("Current Points ",points)
            else:
                print("Total Points",points)
                break
        else:
            print("Enter vaild character!")

#print the grid at current state.
def printgrid(grid):
    for i in range(len(grid)):
        print("\t",end=" ")
        for j in range(len(grid[0])):
            print(grid[i][j]," "*(8-len(grid[i][j])),end=" ")
        print("\n\n")



#find the empty location in grid and also return currentstate.
def findemptylocation(grid):
    #Traverse over the grid and find empty location.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='-':
                return (i,j,True)
    return (-1,-1,False)


#Add 2 at random location in grid.
def addnewnumber(grid):
    n1=random.randint(0,3)
    n2=random.randint(0,3)
    currentstate=True
    if grid[n1][n2]!="-":
        n1,n2,currentstate=findemptylocation(grid)
    #Add 2 to grid if currentstate if True.
    if currentstate:
        grid[n1][n2]=str(2)

    return grid,currentstate


#Rotate the grid in clockwise direction
def rotategrid(grid):
    return list(map(list, zip(*grid[::-1])))


#update the grid according to the direction of move.
def currentmove(grid,direction,points):

    #global element for calculating the points.

    #first Rotate the grid.
    for i in range(direction):
        grid=rotategrid(grid)


    for i in range(len(grid)):
        tempgrid=[]
        countofemptylocation=0

        #moving all elements to a current direction
        for j in grid[i]:
            if j!='-':
                tempgrid.append(j)
            else:
                countofemptylocation+=1
        grid[i]=tempgrid+['-']*countofemptylocation
        #print(grid[i])


        #Add the two elements in grid if they are continous and equal
        for j in range(len(grid[i])-1):
            if grid[i][j]==grid[i][j+1] and grid[i][j]!='-' and grid[i][j+1]!='-':
                grid[i][j]=str(int(grid[i][j])+int(grid[i][j+1]))
                grid[i][j+1]='-'
                points+=int(grid[i][j])
                #update the final value if we get 2048 element in grid
                if grid[i][j]=='2048':
                    final=True
        #moving all elements to a current direction
        tempgrid = []
        countofemptylocation = 0
        for j in grid[i]:
            if j != '-':
                tempgrid.append(j)
            else:
                countofemptylocation+=1
        grid[i]=tempgrid+['-']*countofemptylocation


    #Rotate back the grif in original state.
    for i in range(len(grid)-direction):
        grid=rotategrid(grid)
    return grid,points






start()
while True:
    print("Enter 1 for Replay\nEnter 2 for Exit")
    c=input()
    if c in ['1','2']:
        if c=='2':
            print("Thank you!")
            break
        else:
            start()
    else:
        print("Enter vaild character!")




