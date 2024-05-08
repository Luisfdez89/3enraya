CELDAS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

X, O, BLANCO = 'X', 'O', ' '


def main():
    print('Benvingut a 4 en ratlla!')
    tableroJuego = obtenerTableroVacio()  # Crea el tablero vacío de 4 en ratlla
    jugadorActual, jugadorSiguiente = X, O  # X primer, O següent

    while True:  # Bucle principal del joc
        # Mostra el tauler a la pantalla:
        print(obtenerStrTablero(tableroJuego))

        # Pregunta mentre l'usuari no introdueixi una cel·la vàlida
        movimiento = None
        while not esCeldaValida(tableroJuego, movimiento):
            print('')
            print('Quin és el moviment de {}? (1-D)'.format(jugadorActual))
            movimiento = input('> ')

        tableroJuego[movimiento] = jugadorActual

        # Comprova si el joc ha acabat
        if esGanador(tableroJuego, jugadorActual):  # Comprova si hi ha guanyador
            print(obtenerStrTablero(tableroJuego))
            print('')
            print(jugadorActual + ' ha guanyat la partida!')
            break
        elif tableroLleno(tableroJuego):  # Comprova si hi ha empat
            print(obtenerStrTablero(tableroJuego))
            print('')
            print('Empat!')
            break

        # Canvi de torn entre jugadors:
        jugadorActual, jugadorSiguiente = jugadorSiguiente, jugadorActual

    print('Gràcies per jugar!')


def obtenerTableroVacio():
    """Crea un tauler buit per al joc de 4 en ratlla."""
    # Mapeig: 1|2|3|4
    #         -+-+-
    #         5|6|7|8
    #         -+-+-
    #         9|A|B|C
    #         -+-+-
    #         D|E|F|G
    tablero = {}
    for celda in CELDAS:
        tablero[celda] = BLANCO  # Totes les cel·les del tauler s'inicialitzen a BLANCO
    return tablero


def obtenerStrTablero(tablero):
    """Retorna el tauler formatat com a cadena de text."""
    return '''
      {}|{}|{}|{}  1 2 3 4
      -+-+-
      {}|{}|{}|{}  5 6 7 8
      -+-+-
      {}|{}|{}|{}  9 A B C
      -+-+-
      {}|{}|{}|{}  D E F G'''.format(tablero['1'], tablero['2'], tablero['3'], tablero['4'],
                                     tablero['5'], tablero['6'], tablero['7'], tablero['8'],
                                     tablero['9'], tablero['A'], tablero['B'], tablero['C'],
                                     tablero['D'], tablero['E'], tablero['F'], tablero['G'])


def esCeldaValida(tablero, celda):
    """Retorna True si la cel·la és vàlida i està en BLANCO."""
    return celda in CELDAS and tablero[celda] == BLANCO


def esGanador(tablero, jugador):
    """Retorna True si el jugador és guanyador."""
    # S'utilitzen variables curtes per millorar la llegibilitat
    b, p = tablero, jugador
    # Cerca el 4 en ratlla a les 4 files, 4 columnes i les 2 diagonals
    return ((b['1'] == b['2'] == b['3'] == b['4'] == p) or  # Horitzontal amunt
            (b['5'] == b['6'] == b['7'] == b['8'] == p) or  # Horitzontal mig
            (b['9'] == b['A'] == b['B'] == b['C'] == p) or  # Horitzontal baix
            (b['D'] == b['E'] == b['F'] == b['G'] == p) or  # Horitzontal extrem
            (b['1'] == b['5'] == b['9'] == b['D'] == p) or  # Diagonal
            (b['4'] == b['7'] == b['A'] == b['D'] == p) or  # Diagonal inversa
            (b['1'] == b['6'] == b['B'] == b['G'] == p) or  # Diagonal secundària
            (b['4'] == b['5'] == b['6'] == b['7'] == p) or  # Vertical esquerra
            (b['2'] == b['6'] == b['A'] == b['E'] == p) or  # Vertical centre
            (b['3'] == b['7'] == b['B'] == b['F'] == p) or  # Vertical dreta
            (b['8'] == b['B'] == b['C'] == b['F'] == p))  # Vertical extrem


def tableroLleno(tablero):
    """Retorna True si totes les cel·les estan ocupades."""
    for celda in CELDAS:
        if tablero[celda] == BLANCO:
            return False  # Hi ha almenys una cel·la que no està en blanc, per tant, retorna False
    return True  # Cap espai en BLANCO, per tant, retorna True


if __name__ == '__main__':
    main()
