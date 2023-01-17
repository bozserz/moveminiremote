def on_button_pressed_a():
    Pixel_Array.range(0, 2).show_color(neopixel.colors(NeoPixelColors.RED))
    Pixel_Array.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
    Pixel_Array.range(3, 2).show_color(neopixel.colors(NeoPixelColors.BLUE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Pixel_Array.clear()
    Pixel_Array.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

Pixel_Array: neopixel.Strip = None
Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)

def on_forever():
    pass
basic.forever(on_forever)
