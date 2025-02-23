"This code is for the CircuitPython running on the Adafruit CLUE"

import time
import displayio
from adafruit_clue import clue
from adafruit_display_text import label
import terminalio


previous_mode = None

clue_display = clue.display
clue_group = displayio.Group()
clue_display.root_group = clue_group  

temp_label = label.Label(terminalio.FONT, text="Temp: --°C", color=0xFFFFFF, x=10, y=40, scale=2)
humidity_label = label.Label(terminalio.FONT, text="Humidity: --%", color=0xFFFFFF, x=10, y=100, scale=2)  
mode_label1 = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=10, y=150, scale=2)
mode_label2 = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=10, y=170, scale=2)

clue_group.append(temp_label)
clue_group.append(humidity_label)
clue_group.append(mode_label1)
clue_group.append(mode_label2)

# Track alarm state
alarm_active = False

# Use `time.monotonic()` for fast button checks
last_button_check = time.monotonic()
last_temp_check = time.monotonic()

while True:
    current_time = time.monotonic()

    if current_time - last_button_check > 0.1:
        last_button_check = current_time
        if clue.button_a and alarm_active:
            print("pause_alarm")
            alarm_active = False  

    # Read temp every 3 seconds (not blocking button check)
    if current_time - last_temp_check > 3:
        last_temp_check = current_time
        temperature = clue.temperature  # Read temperature
        humidity = clue.humidity  # Read humidity

        temp_label.text = f"Temp: {temperature:.1f}°C"
        humidity_label.text = f"Humidity: {humidity:.1f}%"

        if 25 < temperature < 30:
            mode = "day"
            mode_text1 = "Day Time!"
            mode_text2 = "Playing Tunes.."
            text_color = 0xFFFF00  
            clue.white_leds = False  
            alarm_active = False  

        elif temperature >= 30:  
            mode = "warning"
            mode_text1 = "Extreme Heat!"
            mode_text2 = "A to Stop Alarm"
            text_color = 0xFF0000  

            if not alarm_active:  
                alarm_active = True  

                # Flash LED and play tone
                for _ in range(3):  
                    clue.white_leds = True  
                    time.sleep(0.2)
                    clue.white_leds = False  
                    time.sleep(0.2)

        else:
            mode = "night"
            mode_text1 = "Night Time!"
            mode_text2 = "Playing Tunes.."
            text_color = 0x0000FF  
            clue.white_leds = False  
            alarm_active = False 

        # Send mode only when it changes
        if mode != previous_mode:
            mode_label1.text = mode_text1
            mode_label1.color = text_color  
            mode_label2.text = mode_text2  
            mode_label2.color = text_color
            previous_mode = mode 
            print(mode)
