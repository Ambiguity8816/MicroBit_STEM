def on_button_pressed_a():
    global Colour
    if Colour == 0 or Colour == 3:
        Colour = 1
        basic.show_string("Cyan")
    elif Colour == 1:
        Colour = 2
        basic.show_string("Magenta")
    elif Colour == 2:
        Colour = 3
        basic.show_string("Yellow")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if Colour == 1:
        basic.show_icon(IconNames.YES)
        pins.digital_write_pin(DigitalPin.P12, 1)
        basic.pause(20000)
        basic.show_icon(IconNames.NO)
        pins.digital_write_pin(DigitalPin.P12, 0)
        basic.show_string("Cyan")
    elif Colour == 2:
        basic.show_icon(IconNames.YES)
        pins.digital_write_pin(DigitalPin.P12, 1)
        basic.pause(20000)
        basic.show_icon(IconNames.NO)
        pins.digital_write_pin(DigitalPin.P12, 0)
        basic.show_string("Magenta")
    elif Colour == 3:
        basic.show_icon(IconNames.YES)
        pins.digital_write_pin(DigitalPin.P12, 1)
        basic.pause(20000)
        basic.show_icon(IconNames.NO)
        pins.digital_write_pin(DigitalPin.P12, 0)
        basic.show_string("Yellow")
    else:
        basic.show_string("X")
input.on_button_pressed(Button.B, on_button_pressed_b)

Colour = 0
Colour = 0
basic.show_string("X")