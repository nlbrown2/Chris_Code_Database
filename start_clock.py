def start_clock(orientation, display_on_lights_bool, timer_value, timer_unit):
    from digital_clock_vertical import digital_clock_vertical
    from digital_clock_horizontal import digital_clock_horizontal
    if orientation == 'vertical':
        digital_clock_vertical(display_on_lights_bool)
    if orientation == 'horizontal':
        digital_clock_horizontal(timer_value, timer_unit, display_on_lights_bool)
        
