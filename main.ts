input.onButtonPressed(Button.A, function () {
    if (Colour == 0 || Colour == 3) {
        Colour = 1
        basic.showString("Cyan")
    } else if (Colour == 1) {
        Colour = 2
        basic.showString("Magenta")
    } else if (Colour == 2) {
        Colour = 3
        basic.showString("Yellow")
    }
})
input.onButtonPressed(Button.B, function () {
    if (Colour == 1) {
        basic.showIcon(IconNames.Yes)
        pins.digitalWritePin(DigitalPin.P12, 1)
        basic.pause(20000)
        basic.showIcon(IconNames.No)
        pins.digitalWritePin(DigitalPin.P12, 0)
        basic.showString("Cyan")
    } else if (Colour == 2) {
        basic.showIcon(IconNames.Yes)
        pins.digitalWritePin(DigitalPin.P13, 1)
        basic.pause(20000)
        basic.showIcon(IconNames.No)
        pins.digitalWritePin(DigitalPin.P13, 0)
        basic.showString("Magenta")
    } else if (Colour == 3) {
        basic.showIcon(IconNames.Yes)
        pins.digitalWritePin(DigitalPin.P14, 1)
        basic.pause(20000)
        basic.showIcon(IconNames.No)
        pins.digitalWritePin(DigitalPin.P14, 0)
        basic.showString("Yellow")
    } else {
        basic.showString("X")
    }
})
let Colour = 0
Colour = 0
basic.showString("X")
