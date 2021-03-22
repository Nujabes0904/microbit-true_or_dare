let arrow = 0
input.onButtonPressed(Button.A, function () {
    basic.pause(randint(2000, 10000))
    if (arrow == 1) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(5000)
    } else if (arrow == 2) {
        basic.showLeds(`
            . . # . .
            . . # # .
            # # # # #
            . . # # .
            . . # . .
            `)
        basic.pause(5000)
    } else if (arrow == 3) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . # # # .
            . . # . .
            `)
        basic.pause(5000)
    } else if (arrow == 4) {
        basic.showLeds(`
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            `)
        basic.pause(5000)
    } else {
    	
    }
})
basic.forever(function () {
    arrow = 1
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        `)
    arrow = 2
    basic.showLeds(`
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        `)
    arrow = 3
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
        `)
    arrow = 4
    basic.showLeds(`
        . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
        `)
})
