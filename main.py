arrow = 0

def on_button_pressed_a():
    basic.pause(randint(2000, 10000))
    if arrow == 1:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            """)
        basic.pause(5000)
    elif arrow == 2:
        basic.show_leds("""
            . . # . .
            . . # # .
            # # # # #
            . . # # .
            . . # . .
            """)
        basic.pause(5000)
    elif arrow == 3:
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.pause(5000)
    elif arrow == 4:
        basic.show_leds("""
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            """)
        basic.pause(5000)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global arrow
    arrow = 1
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        """)
    arrow = 2
    basic.show_leds("""
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        """)
    arrow = 3
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
        """)
    arrow = 4
    basic.show_leds("""
        . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
        """)
basic.forever(on_forever)
