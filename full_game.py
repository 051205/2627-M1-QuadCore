"""Primer hito: carrera de dos tortugas.

La infraestructura gráfica ya está resuelta. Los TODO sólo requieren variables,
condicionales y bucles, que son los contenidos impartidos al anunciar M1.
"""

from __future__ import annotations

import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
START_X = -320
FINISH_X = 300

# TODO 1: asigna dos velocidades positivas. Predice quién ganará.
RED_SPEED = 5
BLUE_SPEED = 3


""" COMPROBACION 1:
Vemos en el TODO 1 que las velocidades son positivas. 
    Posivilidades:
        RED_SPEED = 5
        BLUE_SPEED = 3   --> gana el rojo   ----> COMPROBACIÓN 2: de esta forma la roja es más rápida que la azul 

        RED_SPEED = 5
        BLUE_SPEED = 8   ---> gana el azul ----> COMPROBACIÓN 3: de esta forma la tortuga azul es más rápida 

        RED_SPEED = 5
        BLUE_SPEED = 3   ---> empate 
"""


def prepare_game():
    """Prepara la ventana, la pista y las dos tortugas (código proporcionado)."""
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Carrera de tortugas")

    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    for y in (-80, 0, 80):
        painter.penup()
        painter.goto(START_X, y)
        painter.pendown()
        painter.forward(FINISH_X - START_X)

    red = turtle.Turtle(shape="turtle")
    red.color("red")
    red.penup()
    red.goto(START_X, 40)

    blue = turtle.Turtle(shape="turtle")
    blue.color("blue")
    blue.penup()
    blue.goto(START_X, -40)
    return screen, red, blue



def run_race(red, blue):
    """Mueve las tortugas hasta que una alcance la meta."""
    
    # TODO 2:
    if RED_SPEED <=0 or BLUE_SPEED <=0:
        print("Error: las velocidades deben ser positivas.")
        return ""
    ### COMPROBACION 1: en TODO 2 comprueba y lanza un error si las velocidades son negativas. 
  

    # TODO 3: bucle de la carrera
    while True:
        # Mueve ambas tortugas en el turno actual según sus velocidades
        red.forward(RED_SPEED)
        blue.forward(BLUE_SPEED)
        
        # Comprueba la posición xcor() de cada tortuga respecto a FINISH_X
        red_finished = red.xcor() >= FINISH_X
        blue_finished = blue.xcor() >= FINISH_X
        
        # Evalúa las condiciones de llegada a meta
        if red_finished and blue_finished:
            return "empate"
        elif red_finished:
            return "roja"
        elif blue_finished:
            return "azul"


def main():
    """Pone en marcha la carrera (código proporcionado)."""
    screen, red, blue = prepare_game()
    winner = run_race(red, blue)
    if winner == "empate":
        screen.title("¡Empate! Las dos tortugas llegan a la vez")
    elif winner:
        screen.title(f"¡Ha ganado la tortuga {winner}!")
    screen.mainloop()


if __name__ == "__main__":
    main()
