def simultaneous_hue_shift(wait, speed):
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(0, 255, math.floor(i*speed))
        for j in range(pixels.count()):
            pixels.set_pixel(j, color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(0, 255-math.floor(i*speed), 255)
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(math.floor(i*speed), 0, 255)
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
    for i in range(math.floor(256/speed)):
        color = Adafruit_WS2801.RGB_to_color(255, 0, 255-math.floor(i*speed))
        for j in range(pixels.count()):
            pixels.set_pixel(j,color)
        pixels.show()
        if wait > 0:
            time.sleep(wait)
