def digital_clock_vertical(display_on_lights_bool = 0):
    import numpy as np
    import time
    import math
    import os

    if display_on_lights_bool == 1:
        import Adafruit_WS2801
        import Adafruit_GPIO.SPI as SPI
        import RPi.GPIO as GPIO

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    except Exception as ex:
        print(ex)
        print("Error Encountered")

    if display_on_lights_bool == 1:
        PIXEL_COUNT = 160
        PIXEL_CLOCK = 11
        PIXEL_DOUT = 10
        pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT,clk=PIXEL_CLOCK,do=PIXEL_DOUT)
        pixels.clear()
        pixels.show()

        #RBG
        hour_color = Adafruit_WS2801.RGB_to_color(0,255,0) #blue
        minute_color = Adafruit_WS2801.RGB_to_color(255,50,255) #yellow
        second_ten_color = Adafruit_WS2801.RGB_to_color(255,0,175) #orange
        second_twenty_color = Adafruit_WS2801.RGB_to_color(255,255,0) #magenta
        second_thirty_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red
        second_fourty_color = Adafruit_WS2801.RGB_to_color(0,290,255) #turqoise
        second_fifty_color = Adafruit_WS2801.RGB_to_color(200,255,0) #purple
        second_ones_color = Adafruit_WS2801.RGB_to_color(50,0,255) #green

    number_one = [[0,1],[1,0],[1,1],[2,1],[3,1],[4,0],[4,1],[4,2]]
    number_two = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,1],[2,2],[3,0],[4,0],[4,1],[4,2]]
    number_three = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,1],[2,2],[3,2],[4,0],[4,1],[4,2]]
    number_four = [[0,0],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2],[3,2],[4,2]]
    number_five = [[0,0],[0,1],[0,2],[1,0],[2,0],[2,1],[2,2],[3,2],[4,0],[4,1],[4,2]]
    number_six = [[0,0],[0,1],[0,2],[1,0],[2,0],[2,1],[2,2],[3,0],[3,2],[4,0],[4,1],[4,2]]
    number_seven = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,2],[3,2],[4,2]]
    number_eight = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2],[4,0],[4,1],[4,2]]
    number_nine = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2],[3,2],[4,2]]
    number_zero = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,2],[3,0],[3,2],[4,0],[4,1],[4,2]]


    def print_big_clock(grid):


        ## Get the time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec
        
        ## Get the numbers to print. Stored in digit_one, digit_two .... digit_six
        if hour > 9:
            digit_one = 1
        else:
            digit_one = 0
        digit_two = hour%10
        if minute > 9:
            digit_three = math.floor(minute/10)
        else:
            digit_three = 0
        digit_four = minute%10
        if second > 9:
            digit_five = math.floor(second/10)
        else:
            digit_five = 0
        digit_six = second%10

        digit_list = [digit_one, digit_two, digit_three, digit_four, digit_five, digit_six]
        
        for value in range(len(digit_list)):
            digit = digit_list[value]
            if digit == 1:
                digit_list[value] = number_one
            elif digit == 2:
                digit_list[value] = number_two
            elif digit == 3:
                digit_list[value] = number_three
            elif digit == 4:
                digit_list[value] = number_four
            elif digit == 5:
                digit_list[value] = number_five
            elif digit == 6:
                digit_list[value] = number_six
            elif digit == 7:
                digit_list[value] = number_seven
            elif digit == 8:
                digit_list[value] = number_eight
            elif digit == 9:
                digit_list[value]  = number_nine
            else:
                if value%2 != 0:
                    digit_list[value] = number_zero
                else:
                    digit_list[value] = [] #prevents us from printing a zero for the most significant digit

        for index in digit_list[0]: #digit one
            index = [index[0] + 1, index[1] + 1] #shift the upper left corner of the first hour digit to [1,1]
            grid[index[0], index[1]] = 1
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[0] + (16*index[1]), hour_color)
        for index in digit_list[1]: #digit two
            index = [index[0] + 1, index[1] + 5] #shift the upper left corner of the second hour digit to [1,5], leaving a column between the digits
            grid[index[0], index[1]] = 1
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[0] + (16*index[1]), hour_color)
        for index in digit_list[2]: #digit three
            index = [index[0] + 7, index[1] + 1] #shift the upper left corner of the first minute digit to [7,1], leaving a row between the minute and hour
            grid[index[0], index[1]] = 2
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[0] + (16*index[1]), minute_color)
        for index in digit_list[3]: #digit four
            index = [index[0] + 7, index[1] + 5]
            grid[index[0], index[1]] = 2
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[0] + (16*index[1]), minute_color)

        ## Seconds will be displayed using a counter system rather than displaying the actual value

        if digit_five > 0: #the tens place of the seconds. Must be at least 10 seconds. Light the first light
            grid[13,0] = 3
            if display_on_lights_bool == 1:
                pixels.set_pixel(13, second_ten_color)
        if digit_five > 1: #must be at least 20 seconds. Light the second light too
            grid[13,1] = 4
            if display_on_lights_bool == 1:
                pixels.set_pixel(29, second_twenty_color)
        if digit_five > 2:
            grid[13,2] = 5
            if display_on_lights_bool == 1:
                pixels.set_pixel(45, second_thirty_color)
        if digit_five > 3: 
            grid[13,3] = 6
            if display_on_lights_bool == 1:
                pixels.set_pixel(61, second_fourty_color)
        if digit_five > 4: #must be at least 50 seconds. Light the fifth light too.
            grid[13,4] = 7
            if display_on_lights_bool == 1:
                pixels.set_pixel(77, second_fifty_color)

        for i in range(digit_six):
            grid[14,i] = 8
            if display_on_lights_bool == 1:
                pixels.set_pixel(14 + (16*i), second_ones_color)

        return(grid, hour, minute, second)


    [old_grid, hour, minute, second] = print_big_clock(np.zeros([16,10]))
    while 1:
        
        [new_grid, hour, minute, second] = print_big_clock(np.zeros([16,10]))
        
        if (new_grid != old_grid).any(): #If it's true that new_grid != old_grid for any elements in the arrays (i.e. if the two arrays are different)...

            if display_on_lights_bool == 1:
                pixels.clear()
                
            [new_grid, hour, minute, second] = print_big_clock(np.zeros([16,10]))
            
            old_grid = new_grid
            
            if minute == 0: #Flash the light strands on the hour
                if display_on_lights_bool == 1:
                    GPIO.output(12, GPIO.HIGH)
                    GPIO.output(16, GPIO.HIGH)
                    time.sleep(1)        
                    GPIO.output(12, GPIO.LOW)
                    GPIO.output(16, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(12, GPIO.HIGH)
                    GPIO.output(16, GPIO.HIGH)
                    time.sleep(1)        
                    GPIO.output(12, GPIO.LOW)
                    GPIO.output(16, GPIO.LOW)
                    
            print("Time is ", hour, minute, second)

            #os.system('cls')
            print(new_grid)
            if display_on_lights_bool == 1:
                pixels.show()

        
