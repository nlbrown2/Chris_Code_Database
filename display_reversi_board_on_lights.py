def display_reversi_board_on_lights(board):

    
    import Adafruit_WS2801
    import Adafruit_GPIO.SPI as SPI
    import RPi.GPIO as GPIO
    PIXEL_COUNT = 160
    PIXEL_CLOCK = 11
    PIXEL_DOUT = 10
    pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT,clk=PIXEL_CLOCK,do=PIXEL_DOUT)
    pixels.clear()
    pixels.show()

    black_color = Adafruit_WS2801.RGB_to_color(0,0,255) #green
    white_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red

    for i in range(8):
        for j in range(8):
            if board[i,j] == 1:
                pixels.set_pixel((10*i)+j,white_color)
            if board[i,j] == 2:
                pixels.set_pixel((10*i)+j,black_color)
