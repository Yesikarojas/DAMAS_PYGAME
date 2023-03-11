import order
from colorama import init, Fore, Back, Style
##### VENTANA DEL PROGRAMA #####

imagenes = {}
gs= order.Order()

##### BOTONESINICIO #####
##### FUNCIONES #####

#vector que guarda los posibles movimientos
moves = []
#Dtecta si alguno de los jugadores se quedo sin fichas y de ser asi cambia a true y genera un nuevo ganador
win = False

first_move = []
#variable que detecta alguna captura de ficha
mato = False
#Validador de turnos
turno =True
#muestra los posibles movimientos graficamente
auxDis =[]

def posibleMov(moves):

    global turno, win
    filas=[' ','F','I','L','A','S',' ',' ']
    print("            C O L U M N A S")
    print(" 0   1    2    3    4    5    6    7")
    print("__________________________________________")
    reinas()
    board_size = 8
    aux = False
    for row in range(board_size):
        for col in range(board_size):
                
                for move in moves:
                    if row==move[0] and col==move[1]:
                        print(Fore.YELLOW + "○○  ", end=" ")
                        aux = True
                                   
                if aux==True:
                    aux=False
                   
                else:
                    if gs.piece[row][col]=="--":
                        print(Fore.WHITE + gs.piece[row][col], "  ", end="")
                    elif gs.piece[row][col]=="fa" or gs.piece[row][col]=="ra":
                        print(Fore.BLUE + gs.piece[row][col],"  ", end="")
                    elif gs.piece[row][col]=="fr" or gs.piece[row][col]=="rr":
                        print(Fore.RED + gs.piece[row][col],"  ", end="")
                

        print( " ", Fore.WHITE+"{}".format(row)," ",filas[row])



# metodo para verificar movimientos validos
def sel_piece(row, col):
    global first_move, moves, mato
    muertox =0
    muertoy =0
    first_move = [row, col]

    if gs.piece[row][col] == "fa":
        if row > 0: # para verificar el borde
            if col < 7:
                if gs.piece[row-1][col+1] == "fr" or gs.piece[row-1][col+1] == "rr": # Para saber si puede matar
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fr"or gs.piece[row-1][col-1] == "rr":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")

        for move in moves:
            print("*(",move[0],"      ",move[1],")")
            auxDis.append([move[0], move[1]])
        posibleMov(auxDis)
        auxDis.clear()

    elif gs.piece[row][col] == "fr":
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fa" or gs.piece[row+1][col+1] == "ra":
                    if row+2 < 8 and col+2 < 8:
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fa" or gs.piece[row+1][col-1] == "ra":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
            auxDis.append([move[0], move[1]])
        posibleMov(auxDis)
        auxDis.clear()

    elif gs.piece[row][col] == "ra":
        if row > 0:
            if col < 7:
                if gs.piece[row-1][col+1] == "fr" or gs.piece[row-1][col+1] == "rr":
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fr"or gs.piece[row-1][col-1] == "rr":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fr" or gs.piece[row+1][col+1] == "rr":
                    if row+2 < 8 and col+2 < 8:
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fr" or gs.piece[row+1][col-1] == "rr":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
            auxDis.append([move[0], move[1]])
        posibleMov(auxDis)
        auxDis.clear()

    elif gs.piece[row][col] == "rr":
        if row > 0:
            if col < 7:
                if gs.piece[row-1][col+1] == "fa" or gs.piece[row-1][col+1] == "ra":
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                            #ARREGLANDO QUE NO SE SALGA
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fa" or gs.piece[row-1][col-1] == "ra":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fa" or gs.piece[row+1][col+1] == "ra":
                    if row+2 < 8 and col+2 < 8:    
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fa" or gs.piece[row+1][col-1] == "ra":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
            auxDis.append([move[0], move[1]])
        posibleMov(auxDis)
        auxDis.clear()
    else:
        print("No hay ficha en ese campo")
        viewTable()


    x1 = input("Indique la fila del campoal cual desea mover su ficha")
    if(x1!="" and x1.isdigit()):
        y1 = input("Indique la fila del campoal cual desea mover su ficha")
        if(y1!="" and y1.isdigit()):
            x1 = int(x1)
            y1 = int(y1)
            move_piece(first_move[0], first_move[1], x1, y1, muertox, muertoy)
    else:
        print("Por favor selecciona un espacio valido")
        auxDis.clear()
        moves.clear()
        sel_piece(row, col)
    moves.clear()
    mato = False
    muertoy, muertox = 0,0


def move_piece(row, col, row2, col2, muertox, muertoy):
    global moves, turno
    #print("oreigen:",row, col," destino: ", row2, col2)

    if[row2, col2, 0] in moves:
        gs.piece[row2][col2] = gs.piece[row][col]
        gs.piece[row][col] = "--"
        turno = not turno
    elif[row2, col2, 1] in moves:
        gs.piece[row2][col2] = gs.piece[row][col]
        gs.piece[row][col] = "--"
        gs.piece[muertox][muertoy] = "--"
        turno = not turno
    else:
        if row==row2 and col==col2:
            viewTable()
        else:
            print("Movimiento inválido")


def reinas():
    #para convertir en reina azul
    if gs.piece[0][1] == "fa":
        gs.piece[0][1] = "ra"
    if gs.piece[0][3] == "fa":
        gs.piece[0][3] = "ra"
    if gs.piece[0][5] == "fa":
        gs.piece[0][5] = "ra"
    if gs.piece[0][7] == "fa":
        gs.piece[0][7] = "ra"

    #para convertir en reina roja

    if gs.piece[7][0] == "fr":
        gs.piece[7][0] = "rr"
    if gs.piece[7][2] == "fr":
        gs.piece[7][2] = "rr"
    if gs.piece[7][4] == "fr":
        gs.piece[7][4] = "rr"
    if gs.piece[7][6] == "fr":
        gs.piece[7][6] = "rr"

#MOSTRAR TABLERO
def instructions():
    print("*******************************************")
    print("    BIENVENIDO AL JUEGO DE DAMAS INGLESAS")
    print("*******************************************")
    print("  Para tener en cuenta las fichas de los ")
    print("  jugadores están identificadas así: 'fr'")
    print("  significa ficha roja, 'fa' siganifica ")
    print("  ficha azul, 'rr' significa reina roja,")
    print("  'ra' significa reina azul")
    print("******************************************")
    print("")
    print("************************************************")
    print("                    TABLERO")
    print("************************************************")
    print("")


def viewTable():
    global turno, win
    filas=[' ','F','I','L','A','S',' ',' ']
    print("            C O L U M N A S")
    print(" 0   1    2    3    4    5    6    7")
    print("__________________________________________")
    reinas()
    board_size = 8
    for row in range(board_size):
        for col in range(board_size):
            if gs.piece[row][col]=="--":
                print(Fore.WHITE + gs.piece[row][col], "  ", end="")
            elif gs.piece[row][col]=="fa" or gs.piece[row][col]=="ra":
                print(Fore.BLUE + gs.piece[row][col],"  ", end="")
            elif gs.piece[row][col]=="fr" or gs.piece[row][col]=="rr":
                print(Fore.RED + gs.piece[row][col],"  ", end="")
        print( " ", Fore.WHITE+"{}".format(row)," ",filas[row])
    if turno:
        print("Juega Azul")
        x = input("Indique la fila de la ficha que desea mover")
        if(x!="" and x.isdigit()):
            y = input("Indique la columna de la ficha que desea mover")


            if (y!="" and y.isdigit()):
                x = int(x)
                y = int(y)
                if x>8:
                    print("no existe fila  ", x)
                    viewTable()
                elif y > 8:
                    print("no existe columna  ", y)
                    viewTable()
                else:
                    #importa
                    if(gs.piece[x][y]=="fr" or gs.piece[x][y]=="rr"):
                        print("No es turno de Rojo")
                        viewTable()
                    else:
                        sel_piece(x,y)
            else:
                print("Por favor digite un valor ")
                viewTable()
        else:
            print("Por favor ingrese un valor")
            viewTable()
    else:
        print("Juega Rojo")
        x = input("Indique la fila de la ficha que desea mover")
        if(x!="" and x.isdigit()):
            y = input("Indique la columna de la ficha que desea mover")
            if (y!="" and y.isdigit()):
                x = int(x)
                y = int(y)
                if x>8:
                    print("no existe fila  ", x)
                    viewTable()
                elif y > 8:
                    print("no existe columna  ", y)
                    viewTable()
                else:
                    if(gs.piece[x][y]=="fa" or gs.piece[x][y]=="ra"):
                        print("No es turno de Azul")
                        viewTable()
                    else:
                        sel_piece(x,y)
            else:
                print("Por favor digite un valor ")
                viewTable()
        else:
            print("Por favor ingrese un valor")
            viewTable()
    
    contW = 0
    contB = 0
    for row in gs.piece:
        for elemento in row:
            if elemento == "fa":
                contW+=1
            elif elemento == "fr" or elemento =="rr":
                contB+=1
    if contB == 0:
        print("Azul ha ganado")
        win= True
    elif contW == 0:
        print("Rojo ha ganado")
        win= True

##### BUCLE PRINCIPAL PROGRAMA #####

instructions()
while not win:
    viewTable()

