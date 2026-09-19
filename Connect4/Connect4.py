import turtle
import math
import random

screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)
t = turtle.Turtle()
t.up()
#score.hideturtle()

def draw_rectangle():
  t.goto(-350, -100)
  t.fillcolor('blue')
  t.pendown()
  t.begin_fill()
  t.goto(-350, 500)
  t.goto(250, 500)
  t.goto(250, -100)
  t.goto(-350, -100)
  t.end_fill()
  t.up()

# 4 rows and 4 columns. This is a tiny, mathematically optimal size. forced Draw, ai normally wins against me.
global Nrows
global Ncols
Nrows = 4   
Ncols = 4

def draw_circle(x, y, r, fillcolor):
  t.goto(x, y)
  t.setheading(-90)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(r)
  t.end_fill()

def draw_board():
  draw_rectangle()

  for i in range(Nrows):
    for j in range(Ncols):
      if board[i][j] == 0:
        draw_circle(-340 + j*100, 450 - i*100, 40, 'white')
      if board[i][j] == 1:
        draw_circle(-340 + j*100, 450 - i*100, 40, 'red')
      if board[i][j] == 2:
        draw_circle(-340 + j*100, 450 - i*100, 40, 'yellow')

def display_board():
    for i in range(Nrows):
        print(board[i])
    print()

def display_board_other(board):
    for i in range(len(board)):
        print(board[i])
    print()

def lowest_row(col):
    r = -1
    for i in range(Nrows - 1, -1, -1):
        if board[i][col] == 0:
            r = i
            return r
    return - 1

def lowest_row_other(col, board):
    r = -1
    for i in range(Nrows - 1, -1, -1):
        if board[i][col] == 0:
            r = i
            return r
    return - 1

def findBlocked():
    blocked = []
    boardTransposed = []
    for i in range(len(board)):
       boardTransposed.extend([[]])
       for j in range(len(board[0])):
          boardTransposed[i].append(board[j][i])
    for i in range(len(boardTransposed)):
        if not 0 in boardTransposed[i]:
           blocked.append(i)
    return blocked

def findBlockedother(board):
    blocked = []
    boardTransposed = []
    for i in range(len(board)):
       boardTransposed.extend([[]])
       for j in range(len(board[0])):
          boardTransposed[i].append(board[j][i])
    for i in range(len(boardTransposed)):
        if not 0 in boardTransposed[i]:
           blocked.append(i)
    return blocked

def choose(row, col):
    def minmax(state, mover, movec, t, alpha, beta):
            #print(f"running. Board = {board}, State = {state}, movec={movec}, mover={mover} t={t}")
            #time.sleep(2)
            turn = t % 2
            if t > 0:
                prevturn = (t - 1)%2
                prevtile = (0 - prevturn) + 2
                won = FullStateFind(state, prevtile)
                if won is not None and won != 0:
                    pass
                if won is not None:
                    if prevtile == 1:
                        won = -1
                    return won, movec

            blocked = findBlockedother(state)
            #print(f"blocked: {blocked} state[0]: {state[0]}")
            val = []
            cols = []
            for i in range(len(state[0])):
                #print(f"i={i} blocked={blocked}")
                if i in blocked:
                    continue
                else:
                    row = lowest_row_other(i, state)
                    ns = []
                    for m in state:
                        ns.append(m[::])
                    #print(f"Row = {row} NS = {ns}")
                    ns[row][i] = (0-turn) + 2
    
                    item = minmax(ns, row, i, t + 1, alpha, beta)
                    #print(f"Item = {item}")
                    val.append(item[0])
                    cols.append(i)
                    if turn == 0:
                        alpha = max(alpha, item[0])
                    elif turn == 1:
                        beta = min(beta, item[0])
                    if alpha >= beta:
                        break

            if t <= 2:
                pass
                #print(f"turn={t} state={state} val={val} cols={cols}")
            if not len(val) <= 0:
                if turn == 0:
                    final = max(val)
                else:
                    final = min(val)
                col = cols[val.index(final)]
            else:
                final = 0
                col = None
            return final, col
    btemp = []
    for i in board:
        btemp.append(i[::])
    alpha = -math.inf
    beta = math.inf
    v = minmax(btemp,row,col,0, alpha, beta)
    #v = (0,random.randint(0, 3))
    return v[1]

def Computer(pr, pc):
   global gameOver
   blocked = findBlocked()
   if len(blocked) < Ncols:
      col = choose(pr, pc)
      while col in blocked:
        col = choose(pr, pc)
      lrow = lowest_row(col)
      board[lrow][col] = 2
   draw_board()
   print(Checkover(lrow,pr,col,pc,board))
   if Checkover(lrow,pr,col,pc,board):
        gameOver = True
        print("Game Over")



def CheckIfAllSame(list, val):
    for i in list:
       if not i == val:
          return False
    return True

def Search(list, val, rangedist):
    for i in range(len(list)):
        nl = list[i:i+rangedist:1]
        if len(nl) == rangedist:
            #print(nl)
            if CheckIfAllSame(nl, val) == True:
                return True
    return False

def ConvertRC(grid):
    il = []
    ret = []
    rows = len(grid)    
    cols = len(grid[0])
    for i in grid:
       for j in i:
          il.append(j)
    for i in range(rows):
        newrow = []
        for j in range(i, len(il), rows):
            newrow.append(il[j])
        ret.extend([newrow])
    return ret

def Checkover(row1, row2, col1, col2, board):
    def check(row, col):
        val = board[row][col]
        rows = board
        cols = ConvertRC(board)
        rowlist = rows[row]
        collist = cols[col]
        d1 = []
        d2 = []
        vdp1 = [(0, 0), (1, 1), (2, 2), (3, 3)]
        vdp2 = [(3, 0), (2, 1), (1, 2), (0, 3)]
            
        try:
            if (row, col) in vdp1:
                for i in range(9):
                    v = i - 4
                    try:
                        if not(row + v < 0 or col + v < 0):
                            d1.append(board[row + v][col + v])
                    except:
                        continue
        except:
            pass
        try:
            if (row, col) in vdp2:
                for i in range(9):
                    v = i - 4
                    try:
                        if not(row + v < 0 or col - v < 0):
                            d2.append(board[row + v][col - v])
                    except:
                        continue
        except:
            pass

        if Search(rowlist, val, 4):
            return 1
        if Search(collist, val, 4):
            return 1
        elif Search(d1, val, 4):
            return 1
        elif Search(d2, val, 4):
            return 1
        else:
            return 0
    cl = []
    for i in board:
        if not 0 in i: 
            cl.append(1)
        else: 
            cl.append(0)
    c = 0
    if not 0 in cl:
        c = 1
    else:
        c = 0
    return check(row1, col1) | check(row2, col2) | c


def TerminalState2(row, col, board, val): #Error in returning or error in inputs
    def check(row, col, val):
        rows = board
        cols = ConvertRC(board)
        rowlist = rows[row]
        collist = cols[col]
        d1 = []
        d2 = []
        vdp1 = [(0, 0), (1, 1), (2, 2), (3, 3)]
        vdp2 = [(3, 0), (2, 1), (1, 2), (0, 3)]
        try:
            if (row, col) in vdp1:
                for i in range(9):
                    v = i - 4
                    try:
                        if not(row + v < 0 or col + v < 0):
                            d1.append(board[row + v][col + v])
                    except: 
                        continue
        except:
            pass

        try:
            if (row, col) in vdp2:
                for i in range(9):
                    v = i - 4
                    try:
                        if not(row + v < 0 or col - v < 0):
                            d2.append(board[row + v][col - v])
                    except:
                        continue
        except:
            pass

        if Search(rowlist, val, 4):
            return 1
        elif Search(collist, val, 4):
            return 1
        elif Search(d1, val, 4):
            return 1
        elif Search(d2, val, 4):
            return 1
        else:
            return 0
    if check(row, col, val) == 1:
        return 1
    else:
        for i in board:
            if 0 in i:
                return None
        return 0
    

def is_full(board) -> bool:
    """Returns true if the board is full."""
    for row in board:
        if 0 in row:
            return False
    return True

def FullStateFind(state, color):
    for i in range(len(state)):
        for j in range(len(state[0])):
            v = TerminalState2(i, j, state, color)
            if v is not None and v != 0:
                return v
    if is_full(state) == True:
        return 0
    else:
        return None

def Play(x, y):
    global gameOver
    global turn

    if gameOver == True:
        return

    col = int((x + 350)//100)
    if col < 0:
        col = 0
    if col > Ncols - 1:
        col = Ncols - 1
    blocked = findBlocked()
    if col in blocked:
       display_board()
       return
    else:
       lrow = lowest_row(col)
       board[lrow][col] = 1
       print(blocked)
       display_board()   
    display_board()
    if Checkover(lrow,lrow,col,col,board):
        draw_board()
        gameOver = True
        print("Game Over")

    else:
        Computer(lrow, col)
    return


board = [[0 for _ in range(Ncols)] for _ in range(Nrows)]

gameOver = False
turn = 1

display_board()

blocked = findBlocked()
print(blocked)
draw_board()

screen.onclick(Play)
import tkinter as tk
tk.mainloop()
