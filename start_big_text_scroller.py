def start_big_text_scroller(input_string = "Go Blue!", rainbow_bool = False, lights_bool = False, text_color = "Yellow"):
    import numpy as np
    import time
    import os

    ##rainbow_bool = False
    ##lights_bool = False
    ##text_color = "Yellow"
    ##input_string = "Go Blue!"l
    etter_color = []

    try:

        import Adafruit_WS2801
        import Adafruit_GPIO.SPI as SPI
        import RPi.GPIO as GPIO
        PIXEL_COUNT = 160
        PIXEL_CLOCK = 11
        PIXEL_DOUT = 10
        pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT,clk=PIXEL_CLOCK,do=PIXEL_DOUT)
        pixels.clear()
        pixels.show()

    except:
        print("Problem loading the Adafruit library stuff")

    try: #TODO: add more colors
        if text_color == "Blue":
            letter_color = Adafruit_WS2801.RGB_to_color(0,255,0) #blue
        elif text_color == "Red":
            letter_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red
        elif text_color == "Yellow":
            letter_color = Adafruit_WS2801.RGB_to_color(255,50,255) #yellow
        elif text_color == "Green":
            letter_color = Adafruit_WS2801.RGB_to_color(0,0,255) #green
        elif text_color == "Purple":
            letter_color = Adafruit_WS2801.RGB_to_color(255,50,255) #purple/pink
        else:
            letter_color = Adafruit_WS2801.RGB_to_color(0,0,255) #green
    except:
        print("Error assigning letter_color")


    #TODO: FOR EVERY POSSIBLE CHARACTER (68 characters as of 7/2), ASSIGN A LETTER_COLOR

    #input_string = 'Here is a lot of text to test how well this works!'
    character_list = []
    letter_count_list = list(range(len(input_string)))
    letter_count_list[0] = 15


    for character_select in input_string:

    ########### Letters ###########
        if character_select == 'a' or character_select == 'A':
            letter = [[9,0],[8,0],[7,0],[6,0],[5,0],[4,0],[3,0],[2,0],[1,1],[0,2],[0,3],[1,4],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[3,1],[3,2],[3,3],[3,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(212,102,218)
        elif character_select == 'b' or character_select == 'B':
            letter = [[9,0],[8,0],[7,0],[6,0],[5,0],[4,0],[3,0],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[9,1],[9,2],[9,3],[9,4],[9,5],[8,5],[7,5],[6,4],[5,3],[5,2],[5,1],[1,5],[2,5],[3,5],[4,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(242,195,198)
        elif character_select == 'c' or character_select == 'C':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[0,4],[0,5],[9,1],[9,2],[9,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(31,192,193)
        elif character_select == 'd' or character_select == 'D':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[1,3],[2,4],[3,5],[4,5],[5,5],[6,5],[9,1],[9,2],[8,3],[7,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(225,152,54)
        elif character_select == 'e' or character_select == 'E':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[0,4],[0,5],[9,1],[9,2],[9,3],[9,4],[9,5],[4,1],[4,2],[4,3],[4,4],[4,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(28,131,28)
        elif character_select == 'f' or character_select == 'F':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[0,4],[0,5], [4,1],[4,2],[4,3],[4,4],[4,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(32,87,31)
        elif character_select == 'g' or character_select == 'G':
            letter = [[0,0],[0,2],[0,3],[0,4],[0,5],[1,5],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[9,2],[9,3],[9,4],[8,4],[7,4],[6,4],[6,3],[6,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(155,230,196)
        elif character_select == 'h' or character_select == 'H':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0], [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[4,1],[4,2],[4,3],[4,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(110,249,244)
        elif character_select == 'i' or character_select == 'I':
            letter = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[9,0],[9,1],[9,2],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(14,195,89)
        elif character_select == 'j' or character_select == 'J':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,4],[9,3],[9,2],[8,1],[7,0],[6,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(206,172,165)
        elif character_select == 'k' or character_select == 'K':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[4,1],[3,2],[2,3],[1,4],[0,5],[5,1],[6,2],[7,3],[8,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(50,169,141)
        elif character_select == 'l' or character_select == 'L':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[9,2],[9,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(139,197,39)
        elif character_select == 'm' or character_select == 'M':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[1,1],[2,2],[1,4],[2,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(125,246,9)
        elif character_select == 'n' or character_select == 'N':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[1,1],[2,2],[3,2],[4,2],[8,4],[7,3],[6,3],[5,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(46,218,89)
        elif character_select == 'o' or character_select == 'O':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[0,1],[0,2],[0,3],[0,4],[9,1],[9,2],[9,3],[9,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(203,175,77)
        elif character_select == 'p' or character_select == 'P':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[4,4],[4,3],[4,2],[4,1]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(113,128,219)
        elif character_select == 'q' or character_select == 'Q':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[0,1],[0,2],[0,3],[0,4],[8,1],[8,2],[8,3],[9,5],[7,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(221,70,208)
        elif character_select == 'r' or character_select =='R':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[4,4],[4,3],[4,2],[4,1],[5,1],[6,2],[7,3],[8,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(237,27,5)
        elif character_select == 's' or character_select =='S':
            letter = [[0,5],[0,4],[0,3],[0,2],[0,1],[0,0],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[9,4],[9,3],[9,2],[9,1],[9,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(190,181,41)
        elif character_select == 't' or character_select == 'T':
            letter = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[0,0],[0,1],[0,2],[0,4],[0,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(234,128,60)
        elif character_select == 'u' or character_select == 'U':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[9,1],[9,2],[9,3],[9,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(197,98,102)
        elif character_select == 'v' or character_select == 'V':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,1],[5,1],[6,1],[7,2],[8,2],[9,2],[0,5],[1,5],[2,5],[3,5],[4,4],[5,4],[6,4],[7,3],[8,3],[9,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(33,193,153)
        elif character_select == 'w' or character_select == 'W':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[8,1],[8,4],[7,2],[7,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(178,128,113)
        elif character_select == 'x' or character_select == 'X':
            letter = [[0,0],[1,0],[2,1],[3,1],[4,2],[5,3],[6,4],[7,4],[8,5],[9,5],[9,0],[8,0],[7,1],[6,1],[5,2],[4,3],[3,4],[2,4],[1,5],[0,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(90,224,85)
        elif character_select == 'y' or character_select == 'Y':
            letter = [[9,2],[8,2],[7,2],[6,2],[5,2],[4,2],[3,1],[2,1],[1,0],[0,0],[3,3],[2,4],[1,5],[0,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(247,90,58)
        elif character_select == 'z' or character_select == 'Z':
            letter = [[9,0],[8,0],[7,1],[6,1],[5,2],[4,3],[3,4],[2,4],[1,5],[0,5],[0,4],[0,3],[0,2],[0,1],[0,0],[9,1],[9,2],[9,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(26,155,206)

    ########### Special Characters ###########
        elif character_select == ' ':
            letter = [[4,0],[4,1],[4,2]] #write this in as a space holder, but never display it (not sure if the write-in is necessary)
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(80,13,22)
        elif character_select == '.':
            letter = [[8,-1],[8,0],[9,-1],[9,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(208,230,28)
        elif character_select == ',':
            letter = [[8,0],[9,-1]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(189,49,17)
        elif character_select == '/':
            letter = [[9,0],[8,0],[7,1],[6,1],[5,2],[4,3],[3,4],[2,4],[1,5],[0,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(30,174,96)
        elif character_select == '\\':
            letter = [[0,0],[1,0],[2,1],[3,1],[4,2],[5,3],[6,4],[7,4],[8,5],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(99,4,21)
        elif character_select == '?':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[3,4],[3,3],[3,2],[4,2],[5,2],[6,2],[7,2],[9,2]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(62,76,113)
        elif character_select == '!':
            letter = [[0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[8,2],[9,2],[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[8,3],[9,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(47,50,86)
        elif character_select == ';':
            letter = [[3,2],[3,3],[4,2],[4,3],[9,1],[8,2],[7,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(165,1,146)
        elif character_select == '\'':
            letter = [[0,5],[1,5],[2,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(116,146,191)
        elif character_select == '\"':
            letter = [[0,0],[0,5],[1,0],[1,5],[2,0],[2,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(70,50,242)
        elif character_select == '[':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,1],[0,2],[0,3],[9,1],[9,2],[9,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(223,130,65)
        elif character_select == ']':
            letter = [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[0,4],[0,3],[0,2],[9,4],[9,3],[9,2]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(40,21,248)
        elif character_select == '{':
            letter = [[0,3],[0,2],[1,1],[2,1],[3,1],[4,1],[5,0],[6,1],[7,1],[8,1],[9,2],[9,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(251,68,28)
        elif character_select == '}':
            letter = [[0,2],[0,3],[1,4],[2,4],[3,4],[4,4],[5,5],[6,4],[7,4],[8,4],[9,3],[9,2]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(243,126,164)
        elif character_select == '|':
            letter = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(248,1,44)
        elif character_select == '-':
            letter = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(177,244,204)
        elif character_select == '_':
            letter = [[9,0],[9,1],[9,2],[9,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(130,186,198)
        elif character_select == '=':
            letter = [[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(116,30,87)
        elif character_select == '+':
            letter = [[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[4,0],[4,1],[4,2],[4,4],[4,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(95,183,155)
        elif character_select == '<':
            letter = [[1,5],[2,4],[3,3],[4,2],[5,1],[6,2],[7,3],[8,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(16,239,202)
        elif character_select == '>':
            letter = [[1,0],[2,1],[3,2],[4,3],[5,4],[6,3],[7,2],[8,1],[9,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(2,89,221)
        elif character_select == ':':
            letter = [[2,2],[2,3],[3,2],[3,3],[6,2],[6,3],[7,2],[7,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(74,25,127)
        elif character_select == '#':
            letter = [[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[4,0],[4,2],[4,3],[4,5],[6,0],[6,2],[6,3],[6,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(124,241,210)
        elif character_select == '$':
            letter = [[0,5],[0,4],[0,3],[0,2],[0,1],[1,0],[2,0],[3,0],[4,1],[4,2],[4,3],[4,4],[5,5],[6,5],[7,5],[8,5],[9,4],[9,3],[9,2],[9,1],[9,0],[1,3],[2,3],[3,3],[5,3],[6,3],[7,3],[8,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(11,47,146)
        elif character_select == '%':
            letter = [[9,0],[8,0],[7,1],[6,1],[5,2],[4,3],[3,4],[2,4],[1,5],[0,5],[0,0],[0,1],[1,0],[1,1],[9,5],[9,4],[8,5],[8,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(252,80,101)
        elif character_select == '^':
            letter = [[0,3],[1,4],[2,5],[3,5],[1,2],[2,1],[3,1]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(186,172,197)
        elif character_select == '&':
            letter = [[1,0],[2,1],[3,1],[4,2],[5,3],[6,4],[7,4],[8,5],[9,5],[0,1],[0,2],[0,3],[0,4],[1,5],[2,4],[3,3],[3,2],[3,1],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[8,2],[7,3],[6,4],[5,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(235,111,152)
        elif character_select == '*':
            letter = [[0,2],[0,3],[1,2],[1,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(212,234,48)
        elif character_select == '(':
            letter = [[0,5],[0,4],[1,3],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(114,105,188)
        elif character_select == ')':
            letter = [[0,0],[0,1],[1,2],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,2],[9,1],[9,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(90,186,236)
        elif character_select == '~':
            letter = [[5,1],[4,2],[5,3],[4,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(1,152,52)
        elif character_select == '`':
            letter = [[0,1],[1,2],[2,3]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(112,184,51)

    ######## Numbers #####
        elif character_select == '1':
            letter = [[0,1],[0,2],[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],[9,0],[9,1],[9,2],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(147,163,42)
        elif character_select == '2':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[4,4],[4,3],[4,2],[4,1],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[9,2],[9,3],[9,4],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(225,199,151)
        elif character_select == '3':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[9,4],[9,3],[9,2],[9,1],[9,0],[4,4],[4,3],[4,2],[4,1],[4,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(231,77,91)
        elif character_select == '4':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(87,154,169)
        elif character_select == '5':
            letter = [[0,5],[0,4],[0,3],[0,2],[0,1],[0,0],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[9,4],[9,3],[9,2],[9,1],[9,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(18,166,55)
        elif character_select == '6':
            letter = [[0,5],[0,4],[0,3],[0,2],[0,1],[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[8,5],[7,5],[6,5],[5,5],[4,5],[4,4],[4,3],[4,2],[4,1]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(24,102,205)
        elif character_select == '7':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(201,3,83)
        elif character_select == '8':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[8,5],[7,5],[6,5],[5,5],[4,5],[3,5],[2,5],[1,5],[4,1],[4,2],[4,3],[4,4]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(172,0,126)
        elif character_select == '9':
            letter = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[9,4],[9,3],[9,2],[9,1],[9,0],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[8,0]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(232,198,151)
        elif character_select == '0':
            letter = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[0,1],[0,2],[0,3],[0,4],[9,1],[9,2],[9,3],[9,4],[1,0],[2,1],[3,1],[4,2],[5,3],[6,4],[7,4],[8,5]]
            if  rainbow_bool and lights_bool:
                letter_color = Adafruit_WS2801.RGB_to_color(97,84,100)

        else:
            letter = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2],[4,0],[4,1],[4,2]]

        character_list.append(letter)
        if lights_bool:
            if letter_color != []:
                display_color_list.append(letter_color)

            
    for letter_number in range(len(input_string)): #Creates all of the letter starting positions on an infinitely big grid
        if letter_number >= 0 and (input_string[letter_number-1] == ',' or input_string[letter_number-1] == '.' or input_string[letter_number-1] == '!'): #These characters will have a default field size of 4 (in the else below), but we don't need that much to display, so we can start the next character early by reducing its field size from 4 to 0
            field_size = 2
            #This only works because it is assumed that , and . are followed by a space. If that is false, then the comma/period overlaps other characters (bad!)
        elif letter_number >= 0 and (input_string[letter_number-1] == ' '): #The space will default to four frames (in the else immediately below this), but we don't want it that wide, so we start the next character early by reducing its frame from 4 to 2
            field_size = 4
        elif letter_number >= 0 and (input_string[letter_number-1] == '#' or input_string[letter_number-1] == '~'):
            field_size = 8
        else:
            field_size = 8
        if letter_number > 0:
            letter_count_list[letter_number] = letter_count_list[letter_number-1]+field_size #The field size is usually four to indicate the letter width of 3 plus 1 space. Spaces following special characters are reduced. Also accounts for spaces

    grid = np.zeros([10,16]) #defines grid so the while statement doesn't break on first iteration


    while np.sum(grid) > 0 or letter_count_list[0] == 15:
        grid = np.zeros([10,16])

        break_bool = False

        for letter_number in range(len(input_string)): #For every letter we eventually want to display
            #print("Letter under examination is", input_string[letter_number])
            if break_bool:
                #print("For character", input_string[letter_number-1], ", breaking")
                #print("No longer on grid. Breaking from letter iterator") #Avoids too much pre-processing for stuff that doesn't even get displayed
                break
            if lights_bool:
                display_color = display_color_list[letter_number]

            for position in character_list[letter_number]: #For every pixel we want to display
                if position[1] + letter_count_list[letter_number] >= 0 and position[1] + letter_count_list[letter_number] < 16 and input_string[letter_number] != ' ': #If the pixel actually exists on our finitely sized grid
                    #print("Updating grid top")
                    grid[position[0]][position[1]+letter_count_list[letter_number]] = 1 #display
                    if lights_bool:
                        pixels.set_pixel((10*(15-position[1]) + position[0]), display_color) #TODO: CHECK THIS! ASSUMES ROTATE THE 16X10 CLOCKWISE 90 DEGREES TO GET A 10X16
                elif position[1] + letter_count_list[letter_number] >= 16: #don't want to break if it goes off left end of screen; only right
                    break_bool = True


        print(grid,'\n')
        if lights_bool:
            pixels.show()
        for i in range(len(letter_count_list)):
            letter_count_list[i] = letter_count_list[i] - 1
        time.sleep(0.1)
        os.system('cls')
        if lights_bool:
            pixels.clear()

    print("Done!")
