from chess.constants import *
from chess import Chess

if __name__ == '__main__':
    game = Chess()

    game.draw_board()

    try:
        while not game.in_checkmate():
            movement = input('\nDigite o movimento: ')

            moved = game.move(movement)

            game.draw_board()

            if not moved:
                if game.in_check():
                    print('\nMovimento inválido, pois ele não tira o rei de xeque.')

                else:
                    print('\nMovimento inválido.')

            if game.in_checkmate():
                if game.turn == WHITE:
                    print('\nJogo finalizado com xeque-mate! Vitória das pretas.\n')

                else:
                    print('\nJogo finalizado com xeque-mate! Vitória das brancas.\n')

    except KeyboardInterrupt:
        if game.turn == WHITE:
            print('\n\nPartida abandonada pelas brancas. Vitória das pretas.\n')

        else:
            print('\n\nPartida abandonada pelas pretas. Vitória das brancas.\n')
