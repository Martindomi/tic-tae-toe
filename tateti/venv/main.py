#TA TE TI game in pyhton

board = [' ' for  x in range(10)]

def initialiceBoard(aBoard):
    for x in range(0,len(aBoard)):
        insertLetter(" ", x)

def insertLetter(letter, pos):
    board[pos] = letter;

def spaceIsFree(pos):
    return board[pos] == " "

def printBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def isWinner(currentBoard, letter):
    return (threeEqualPosition(currentBoard, 7, 8, 9, letter) or # horizontal inferior
            threeEqualPosition(currentBoard, 4, 5, 6, letter) or # horizontal medio
            threeEqualPosition(currentBoard, 1, 2, 3, letter) or # horizontal superior
            threeEqualPosition(currentBoard, 1, 4, 7, letter) or # vertical izq
            threeEqualPosition(currentBoard, 2, 5, 8, letter) or # vertical medio
            threeEqualPosition(currentBoard, 3, 6, 9, letter) or # vertical der
            threeEqualPosition(currentBoard, 1, 5, 9, letter) or # diagonal
            threeEqualPosition(currentBoard, 7, 5, 3, letter) )  #diagonal


def threeEqualPosition(aBoard, pos1, pos2, pos3, letter):
    return (aBoard[pos1] == letter and aBoard[pos2] == letter and aBoard[pos3] == letter and letter != ' ')

def isBoardFull(board):
    if (board.count(' ') == 1):
        return True
    else:
        return False

def playerMove(letter):
    run = True
    while run:
        move = input("Elija una posicion para insertar \'"+letter+"\' (1-9): ")
        try:
            move = int(move)
            if (move >= 1 and move <= 9):
                if( spaceIsFree(move)):
                    run = False
                    insertLetter(letter, move)
                else:
                    print("Ups, ese lugar ya esta ocupado :(")
            else:
                print("Ups, no existe esa posición :( . Elija una posicion para insertar \'"+letter+"\' (1-9):  ")
        except:
            print("Ups, debes ingresar un numero del 1 al 9 :)")



def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter ==' ' and x != 0]
    move = 0
    print("turno de la maquina")
    for let in['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:] #  [:] hago copia, sin eso es solo una referencia
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move= 5
        return  move

    resto = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            cornersOpen.append(i)
    if len(resto) > 0:
        move = selectRandom(resto)
        return move

def selectRandom(lista):
    import random
    largoLista = len(lista)
    r = random.randrange(0,largoLista)
    return  lista[r]

def gameMode():
    mode = input(" 1 Jugador: presione 1 | 2 Jugadores: presione 2 => ")
    mode = int(mode)
    try:
        if(mode == 1):
            print("1 Jugador ")
            onePlayer()
        if(mode == 2):
            print("2 Jugadores")
            twoPlayer()
    except:
        print("valor invalido ingresado")
        gameMode()


def onePlayer():
    while not (isBoardFull(board)):

        if not (isWinner(board, 'O')):
            playerMove('X')
            printBoard(board)
        else:
            print('O es el ganador!!!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("EMPATE :|")
            else:
                insertLetter("O",move)
                printBoard(board)
        else:
            print('X es el ganador!!!')
            break

    if(isBoardFull(board) and (not isWinner(board,"O") or not isWinner(board,"X"))):
        print('EMPATE :|')

def twoPlayer():
    while not (isBoardFull(board)):

        if not (isWinner(board, 'O')):
            playerMove('X')
            printBoard(board)
        else:
            print('O es el ganador!!!')
            break

        if not (isWinner(board, 'X')):
            playerMove('O')
            printBoard(board)
        else:
            print('X es el ganador!!!')
            break

    if(isBoardFull(board)):
        print('EMPATE :|')




def main():
    match = True
    while match:
        print("TA TE TI!")
        gameMode()
        initialiceBoard(board)
        match = input("Presiona \'Y\' para una nueva partida =>  ")
        if(match != 'y' and match != 'Y'):
            match = False


main()

