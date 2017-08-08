def digital_clock_horizontal(timer_value = 1, timer_unit = "minutes", display_on_lights_bool = 0):

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
        second_color = Adafruit_WS2801.RGB_to_color(255,255,0) #magenta
        if timer_unit == "seconds":
            timer_color = Adafruit_WS2801.RGB_to_color(50,0,255) #green
        elif timer_unit == "minutes":
            timer_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red
        elif timer_unit == "hours":
            timer_color = Adafruit_WS2801.RGB_to_color(200,255,0) #purple
        else:
            print("Error getting timer color")
            exit()
        


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

    def print_timer(grid, seconds_remaining, timer_unit):

         #Get the timer value

            
        if timer_unit == "seconds":
            timer = math.ceil(seconds_remaining)
        elif timer_unit == "minutes":
            timer = math.ceil(seconds_remaining/60)
        elif timer_unit == "hours":
            timer = math.ceil(seconds_remaining/(60*24))
        else:
            print("Error getting timer")
            exit()

        ## Check if timer entered new unit (e.g. minutes -> seconds), then change the unit and the value. Like going from 1 minute to 59 seconds.
        if timer_unit == "hours" and (seconds_remaining/(60*24)) < 1:
            timer = math.ceil(seconds_remaining/60)
            timer_unit = "minutes"
            if display_on_lights_bool == 1:
                timer_color = Adafruit_WS2801.RGB_to_color(255,0,0) #red
        if timer_unit == "minutes" and  (seconds_remaining/60) < 1:
            timer = math.ceil(seconds_remaining)
            timer_unit = "seconds"
            if display_on_lights_bool == 1:
                timer_color = Adafruit_WS2801.RGB_to_color(50,0,255) #green

        if timer > 9:
            digit_seven = math.floor(timer/10)
        else:
            digit_seven = math.floor(timer/10)

        digit_eight = timer%10

        digit_list = [digit_seven, digit_eight]
        
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

        for index in digit_list[0]: #digit 7  (timer)
            index = [index[0] + 5, index[1] + 9]
            grid[index[0], index[1]] = 4
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), timer_color)
        for index in digit_list[1]:
            index = [index[0] + 5, index[1] + 13]
            grid[index[0], index[1]] = 4
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), timer_color)

        
        return(grid, timer, timer_unit)

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
            index = [index[0] + 0, index[1] + 0] #shift the upper left corner of the first hour digit to [0,0]
            grid[index[0], index[1]] = 1
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), hour_color)
        for index in digit_list[1]: #digit two
            index = [index[0] + 0, index[1] + 4] #shift the upper left corner of the second hour digit to [0,4], leaving a column between the digits
            grid[index[0], index[1]] = 1
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), hour_color)
        for index in digit_list[2]: #digit three
            index = [index[0] + 0, index[1] + 9] #shift the upper left corner of the first minute digit to [0,9], leaving two columns between the minute and hour
            grid[index[0], index[1]] = 2
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), minute_color)
        for index in digit_list[3]: #digit four
            index = [index[0] + 0, index[1] + 13]
            grid[index[0], index[1]] = 2
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), minute_color)
        for index in digit_list[4]: #digit 5 (seconds)
            index = [index[0] + 5, index[1] + 0]
            grid[index[0], index[1]] = 3
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), second_color)
        for index in digit_list[5]:
            index = [index[0] + 5, index[1] + 4]
            grid[index[0], index[1]] = 3
            if display_on_lights_bool == 1:
                pixels.set_pixel(index[1] + (16*index[0]), second_color)


        return(grid, hour, minute, second)


    [old_grid, hour, minute, second] = print_big_clock(np.zeros([10,16]))

    if timer_value > 99 and timer_unit == "seconds":
        print("Invalid timer entry")
        exit()

    if timer_unit == "seconds":
        timer_end = time.time() + timer_value
    elif timer_unit == "minutes":
        timer_end = time.time() + (60*timer_value)
    elif timer_unit == "hours":
        timer_end = time.time() + (24*60*timer_value)
    else:
        print("Error getting timer_end")
        exit()
        
    while 1:


        [new_grid, hour, minute, second] = print_big_clock(np.zeros([10,16])) #Get the clock board state so we can check if it's changed

        seconds_remaining = timer_end - time.time()
        if seconds_remaining > 0: #Check if the timer is done   
            [new_grid, time_remaining, timer_unit] = print_timer(new_grid, seconds_remaining, timer_unit)
        elif seconds_remaining < 0 and ((seconds_remaining > -0.5) or (seconds_remaining > -1.5 and seconds_remaining < -1) or (seconds_remaining > -2.5 and seconds_remaining < -2) or (seconds_remaining > -3.5 and seconds_remaining < -3) or (seconds_remaining > -4.5 and seconds_remaining < -4)):
            for i in range(5,10):
                for j in range(8,16):
                    new_grid[i,j] = 8
                    if display_on_lights_bool == 1:
                        pixels.set_pixel(j + (16*i), second_color)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(16, GPIO.HIGH)
        else:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        
        if (new_grid != old_grid).any(): #If it's true that new_grid != old_grid for any elements in the arrays (i.e. if the two arrays are different)...
            if display_on_lights_bool == 1:
                pixels.clear()

            [new_grid, hour, minute, second] = print_big_clock(np.zeros([10,16]))
            if seconds_remaining > 0: #redundant lines, but it resets the pixels after the clear
                [new_grid, time_remaining, timer_unit] = print_timer(new_grid, seconds_remaining, timer_unit) 

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
            if seconds_remaining > 0:
                print("Timer value is: ", time_remaining, timer_unit)
            else:
                print("Timer done")

            #os.system('cls')
            print(new_grid)
            if display_on_lights_bool == 1:
                pixels.show()
    
        
