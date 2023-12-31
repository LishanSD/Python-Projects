# ---------------------------------------------
#   Written by: Lishan Dissanayake
#   Date: 01.01.2024
#   Title: Lab_10a
# ---------------------------------------------


# The "Cell" class which represents a cell in the maze
class Cell:
    # Initializing the "Cell" class
    def __init__(self, y, x, entered_at):
        self.walls = maze[y][x]       # Walls of the cell
        self.y = y                    # y coordination of the cell
        self.x = x                    # x coordination of the cell
        self.entered_at = entered_at  # Side that entered the cell


# Function to navigate through the maze
def navigate(current_cell):
    global left_maze
    #path.push(current_cell)

    for k in range(4):
        if (left_maze == True):
            break
        elif(current_cell.y == 11 and current_cell.x == 13 and k == 1):
            left_maze = True
            print("Leaving at (%i,%i)" %(current_cell.y,current_cell.x)) 
            break
        elif ((current_cell.walls[k] == 1) or (k == current_cell.entered_at)):
            continue
        else:
            if (k == 0):
                print("North", end = " ")
                y = current_cell.y - 1
                x = current_cell.x 
                entered_at = 2
            elif (k == 1):
                print("East", end = " ")
                y = current_cell.y
                x = current_cell.x + 1
                entered_at = 3
            elif (k == 2):
                print("South", end = " ")
                y = current_cell.y + 1
                x = current_cell.x 
                entered_at = 0
            elif (k == 3):
                print("West", end = " ")
                y = current_cell.y
                x = current_cell.x - 1
                entered_at = 1
            
            next_cell = Cell(y, x, entered_at)
            navigate(next_cell)
            if (left_maze == False):
                print("Back to (%i,%i)" %(current_cell.y,current_cell.x))
        
    if (left_maze == False): 
        print("Stuck at (%i,%i)" %(current_cell.y,current_cell.x))   
        #path.pop()


# Implementing the maze
        
#            0         1         2         3         4         5         6         7         8         9         10        11        12        13          
maze = [[[1,0,0,1],[1,0,1,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[1,0,1,0],[1,1,0,0],[1,0,1,1],[1,0,0,0],[1,0,1,0],[1,1,1,0],[1,0,0,1],[1,0,1,0],[1,1,0,0]],
        [[0,1,0,1],[1,0,1,1],[0,0,1,0],[1,1,1,0],[0,1,0,1],[1,0,1,1],[0,0,1,0],[1,0,0,0],[0,1,0,0],[1,0,1,1],[1,0,1,0],[0,0,1,0],[1,1,1,0],[0,1,0,1]],
        [[0,0,0,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[0,1,1,0],[1,0,0,1],[1,1,1,0],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,0,1,0],[1,1,0,0],[1,0,0,1],[0,1,0,0]],
        [[0,1,0,1],[0,1,0,1],[1,0,0,1],[0,0,0,0],[1,0,1,0],[0,1,1,0],[1,0,1,1],[0,0,1,0],[1,1,1,0],[1,0,0,1],[1,0,1,0],[0,1,1,0],[0,1,0,1],[0,1,0,1]],
        [[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,1,0],[1,1,0,0],[1,0,0,1],[0,1,1,0],[1,0,0,1],[1,0,1,0],[0,1,1,0],[0,1,0,1]],
        [[0,1,0,1],[0,1,0,1],[0,1,1,1],[0,1,0,1],[0,1,0,1],[1,0,0,1],[1,1,1,0],[0,1,0,1],[0,1,0,1],[1,0,0,1],[0,1,0,0],[1,0,0,1],[1,1,0,0],[0,1,1,1]],
        [[0,1,1,1],[0,0,0,1],[1,1,0,0],[0,1,0,1],[0,1,0,1],[0,1,0,1],[1,0,0,1],[0,0,1,0],[0,1,1,0],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[1,1,0,1]],
        [[1,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,0,0,1],[1,1,1,0],[1,1,0,1],[0,1,1,1],[0,0,0,1],[0,1,1,0],[0,1,0,1],[0,1,0,1]],
        [[0,1,0,1],[0,1,1,1],[0,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[0,1,1,0],[1,0,0,1],[0,1,1,0],[1,1,0,1],[0,1,0,1],[1,0,0,1],[0,0,1,0],[0,1,0,0]],
        [[0,0,0,1],[1,0,1,0],[0,0,1,0],[1,1,1,0],[0,0,1,1],[1,0,1,0],[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,0,1,0],[0,1,0,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]],
        [[0,1,1,1],[1,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,1,0],[1,1,0,0],[0,0,0,1],[1,1,0,0],[1,0,0,1],[1,0,1,0],[0,1,1,0],[0,1,0,1],[0,1,0,1],[0,1,0,1]],
        [[1,0,0,1],[0,1,0,0],[0,1,0,1],[1,0,0,1],[1,1,0,0],[0,0,1,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,0,1,1],[0,0,1,0]],
        [[0,1,0,1],[0,0,1,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[1,0,0,0],[1,1,1,0],[0,1,1,1],[1,0,0,1],[1,0,1,0],[0,1,1,0],[0,0,1,1],[1,1,1,0],[1,1,0,1]],
        [[0,0,1,1],[1,0,1,0],[1,0,1,0],[0,0,1,0],[1,1,1,0],[0,0,1,1],[1,0,1,0],[1,0,1,0],[0,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0],[0,1,1,0]]]



left_maze = False    # Falg to indicate whether left the maze

y = 2
x = 0
entered_at = 3

#path = Stack()
current_cell = Cell(y, x, entered_at)

print("Start at (%i,%i)" %(current_cell.y,current_cell.x))
navigate(current_cell)