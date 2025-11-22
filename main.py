from gpiozero import RGBLED, Button
from signal import pause
import itertools

# --- Helper Function for 0-255 conversion ---
def rgb(r, g, b):
    return (r/255.0, g/255.0, b/255.0)

# --- Pin-Konfiguration ---
PIN_RED = 17
PIN_GREEN = 27
PIN_BLUE = 22
PIN_BUTTON = 26

# --- Zustandsdefinitionen (Updated with 0-255 values) ---
STATE_COLORS = {
    # Amber (Adjusted for common LED physics)
    # Note: Pure (255, 191, 0) might look too green on an LED.
    # I lowered Green to 100 here for a better "Amber" look.
    "NO_CONNECTION":       rgb(255, 100, 0),  
    
    "BLUETOOTH_CONNECTED": rgb(0, 0, 255),    
    "WIFI_CONNECTED":      rgb(0, 255, 0),    
    "ERROR":               rgb(255, 0, 0),    
}

STATES = itertools.cycle(STATE_COLORS.keys())

# --- Initialisierung ---
led = RGBLED(red=PIN_RED, green=PIN_GREEN, blue=PIN_BLUE, active_high=False)
button = Button(PIN_BUTTON, pull_up=True)

# --- Logik ---
def set_next_state():
    current_state = next(STATES)
    color = STATE_COLORS[current_state]
    
    print(f"Button gedrückt! Neuer Zustand: {current_state}")
    
    # Reset blink state
    led.source = None
    
    if current_state == "ERROR":
        print("Fehlerzustand: LED blinkt.")
        # Explicitly defining Off as Black (0,0,0)
        led.blink(on_time=0.5, off_time=0.5, on_color=color, off_color=rgb(0,0,0))
    else:
        led.color = color

button.when_pressed = set_next_state

# --- Hauptprogramm ---
print("Programm gestartet mit RGB (0-255) Werten.")
set_next_state()
pause()