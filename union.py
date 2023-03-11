import pygame
import sys

import order1

pygame.init()
width, height = 840, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Juego de damas')

board = order1.Order2()
player = 1
selected_piece = None


white_piece = pygame.image.load('fb.png')
black_piece = pygame.image.load('fn.png')
queen_black = pygame.image.load('rb.png')
queen_white = pygame.image.load('rn.png')

white_captured=0
black_captured=0
font = pygame.font.SysFont('Arial', 24)


#reglas import

imagenes = {}



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
second_click = True

text=""
text2=""
muertox =0
muertoy =0




def draw_board():
    global text, board
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 16)
    
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(col*80, row*80, 80, 80))
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 pygame.Rect(col*80, row*80, 80, 80))
            if board.piece[row][col] == 'fb':
                screen.blit(white_piece, (col*80+5, row*80+5))
            elif board.piece[row][col] == 'fn':
                screen.blit(black_piece, (col*80+5, row*80+5))
            elif board.piece[row][col] == 'rn':
                screen.blit(queen_black, (col*80+5, row*80+5))
            elif board.piece[row][col] == 'rb':
                screen.blit(queen_white, (col*80+5, row*80+5))
        # Valido los las fichas que llegaron hasta el fondo
            if board.piece[row][col] == 'fb' and row == 0:
                board.piece[row][col] = 'rb'
            elif board.piece[row][col] == 'fn' and row == 7:
                board.piece[row][col] = 'rn'


    white_captured_text = font.render('Pieces White: {}'.format(white_captured), True, (255, 255, 255))
    black_captured_text = font.render('Pieces Black: {}'.format(black_captured), True, (255, 255, 255))
    screen.blit(white_captured_text, (650, 100))
    screen.blit(black_captured_text, (650, 200))

    if turno:
        text = "Red Turn"
        # Renderiza el texto en una superficie de Pygame
        text_surface = font.render(text, True, (255, 255, 255))

        # Dibuja el texto en la pantalla utilizando la función blit()
        screen.blit(text_surface,(650, 400))
    

    else:
        text = "Purple Turn"
        # Renderiza el texto en una superficie de Pygame
        text_surface = font.render(text, True, (255, 255, 255))

        # Establece la posición del texto en la pantalla utilizando las coordenadas
        screen.blit(text_surface,(650, 400))

    
    # Renderiza el texto en una superficie de Pygame
    text_surface = font.render(text2, True, (255, 255, 255))

    # Dibuja el texto en la pantalla utilizando la función blit()
    screen.blit(text_surface,(650, 500))
    pygame.display.update() 
    


def move_piece(row, col, row2, col2, muertox, muertoy):
    global moves, turno, board

    if[row2, col2, 0] in moves:
        board.piece[row2][col2] = board.piece[row][col]
        board.piece[row][col] = "--"
        turno = not turno
    elif[row2, col2, 1] in moves:
        board.piece[row2][col2] = board.piece[row][col]
        board.piece[row][col] = "--"
        board.piece[muertox][muertoy] = "--"
        turno = not turno
    else:
        if row==row2 and col==col2:
            draw_board()
        else:
            print("Movimiento inválido")

def valid_turns():
    global text2, turno, board
    row, col= 0, 0
    x, y = pygame.mouse.get_pos()
    row = (y//80)
    col = (x//80)

    if turno:
        if row >= 8:
            draw_board()
        elif col >= 8:
            draw_board()
        else:
            #importa
            if(board.piece[row][col]=="fn" or board.piece[row][col]=="rn"):
                text2 = " Not is your turn"
            else:
                get_posi()
    else:
        if row>=8:
            draw_board()
        elif col >= 8:
            draw_board()
        else:
            #importa
            if(board.piece[row][col]=="fb" or board.piece[row][col]=="rb"):
                text2 = " Not is your turn"
            else:
                get_posi()

def get_posi():
    global second_click, moves, first_move, mato, turno, text, board, muertoy, muertox
    
    row, col= 0, 0
    x, y = pygame.mouse.get_pos()
    
    if second_click:
        row = (y//80)
        col = (x//80)
        first_move=[row, col]
        if board.piece[row][col] == "fb":
            if row > 0: # para verificar el borde
                if col < 7:
                    if board.piece[row-1][col+1] == "fn" or board.piece[row-1][col+1] == "rn": # Para saber si puede matar
                        if row-2 >= 0 and col+2 < 8:
                            if board.piece[row-2][col+2] == "--":
                                moves.append([row-2, col+2, 1])
                                muertox=row-1
                                muertoy=col+1
                    if board.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1, 0])
                        #move_piece(first_move[0], first_move[1], row, col, muertox, muertoy)
                if col > 0:
                    if board.piece[row-1][col-1] == "fn" or board.piece[row-1][col-1] == "rn":
                        if row-2 >= 0 and col-2 >= 0:
                            if board.piece[row-2][col-2] == "--":
                                moves.append([row-2, col-2, 1])
                                muertox=row-1
                                muertoy=col-1
                    if board.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1, 0])
        elif board.piece[row][col] == "fn":
            if row < 7:
                if col < 7:
                    if board.piece[row+1][col+1] == "fb" or board.piece[row+1][col+1] == "rb":
                        if row+2 < 8 and col+2 < 8:
                            if board.piece[row+2][col+2] == "--":
                                moves.append([row+2, col+2, 1])
                                muertox=row+1
                                muertoy=col+1
                    if board.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1, 0])
                if col > 0:
                    if board.piece[row+1][col-1] == "fb" or board.piece[row+1][col-1] == "rb":
                        if row+2 < 8 and col-2 >= 0:
                            if board.piece[row+2][col-2] == "--":
                                moves.append([row+2, col-2, 1])
                                muertox=row+1
                                muertoy=col-1
                    if board.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1, 0])
        elif board.piece[row][col] == "rb":
            if row > 0:
                if col < 7:
                    if board.piece[row-1][col+1] == "fn" or board.piece[row-1][col+1] == "rn":
                        if row-2 >= 0 and col+2 < 8:
                            if board.piece[row-2][col+2] == "--":
                                moves.append([row-2, col+2, 1])
                                muertox=row-1
                                muertoy=col+1
                    if board.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1, 0])
                if col > 0:
                    if board.piece[row-1][col-1] == "fn"or board.piece[row-1][col-1] == "rn":
                        if row-2 >= 0 and col-2 >= 0:
                            if board.piece[row-2][col-2] == "--":
                                moves.append([row-2, col-2, 1])
                                muertox=row-1
                                muertoy=col-1
                    if board.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1, 0])
            if row < 7:
                if col < 7:
                    if board.piece[row+1][col+1] == "fn" or board.piece[row+1][col+1] == "rn":
                        if row+2 < 8 and col+2 < 8:
                            if board.piece[row+2][col+2] == "--":
                                moves.append([row+2, col+2, 1])
                                muertox=row+1
                                muertoy=col+1
                    if board.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1, 0])
                if col > 0:
                    if board.piece[row+1][col-1] == "fn" or board.piece[row+1][col-1] == "rn":
                        if row+2 < 8 and col-2 >= 0:
                            if board.piece[row+2][col-2] == "--":
                                moves.append([row+2, col-2, 1])
                                muertox=row+1
                                muertoy=col-1
                    if board.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1, 0])
        elif board.piece[row][col] == "rn":
            if row > 0:
                if col < 7:
                    if board.piece[row-1][col+1] == "fb" or board.piece[row-1][col+1] == "rb":
                        if row-2 >= 0 and col+2 < 8:
                            if board.piece[row-2][col+2] == "--":
                                moves.append([row-2, col+2, 1])
                                muertox=row-1
                                muertoy=col+1
                                #ARREGLANDO QUE NO SE SALGA
                    if board.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1, 0])
                if col > 0:
                    if board.piece[row-1][col-1] == "fb" or board.piece[row-1][col-1] == "rb":
                        if row-2 >= 0 and col-2 >= 0:
                            if board.piece[row-2][col-2] == "--":
                                moves.append([row-2, col-2, 1])
                                muertox=row-1
                                muertoy=col-1
                    if board.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1, 0])
            if row < 7:
                if col < 7:
                    if board.piece[row+1][col+1] == "fb" or board.piece[row+1][col+1] == "rb":
                        if row+2 < 8 and col+2 < 8:    
                            if board.piece[row+2][col+2] == "--":
                                moves.append([row+2, col+2, 1])
                                muertox=row+1
                                muertoy=col+1
                    if board.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1, 0])
                if col > 0:
                    if board.piece[row+1][col-1] == "fb" or board.piece[row+1][col-1] == "rb":
                        if row+2 < 8 and col-2 >= 0:
                            if board.piece[row+2][col-2] == "--":
                                moves.append([row+2, col-2, 1])
                                muertox=row+1
                                muertoy=col-1
                    if board.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1, 0])
        for move in moves:
            print(move[0],move[1], "psibles movimientos")
            
            pygame.draw.rect(screen, (29, 165, 172),
                                 pygame.Rect(move[1]*80, move[0]*80, 80, 80))
            #no aparecen, o aparecen pero se borran#
        second_click = not second_click
        
    else:
        second_click = not second_click
        print("second click")
        row2 = (y//80)
        col2 = (x//80)
        print(row2, " destino ", col2)
        if (row2==first_move[0] and col2==first_move[1]):
            for move in moves:

                print("no cambia turno")
                #btnList[move[0]][move[1]].config(background="#2B2A2A")
        else:
            move_piece(first_move[0], first_move[1], row2, col2, muertox, muertoy)
        moves.clear()
        mato = False
        muertoy, muertox = 0,0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                valid_turns()

    draw_board()
      