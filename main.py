from gpiozero import RGBLED, Button
from signal import pause
import itertools

# --- Pin-Konfiguration (BCM-Nummerierung) ---
PIN_RED = 17
PIN_GREEN = 27
PIN_BLUE = 22
PIN_BUTTON = 26

# --- Zustandsdefinitionen ---
# Farben als (R, G, B) Tupel, wobei die Werte von 0.0 bis 1.0 reichen.
# gpiozero kümmert sich um die Umrechnung für Common-Anode-LEDs.
STATE_COLORS = {
    "NO_CONNECTION": (0.5, 0.75, 0.0),  # Amber
    "BLUETOOTH_CONNECTED": (0.0, 0.0, 1.0),  # Blue
    "WIFI_CONNECTED": (0.0, 1.0, 0.0),  # Green
    "ERROR": (1.0, 0.0, 0.0),  # Red
}
# Erstellt einen unendlichen Iterator, der durch die Zustände wechselt
STATES = itertools.cycle(STATE_COLORS.keys())


# --- Initialisierung ---
# Initialisiert die LED und den Button.
# Im Simulationsmodus werden hier Mock-Objekte anstelle von echten GPIO-Objekten erstellt.
led = RGBLED(red=PIN_RED, green=PIN_GREEN, blue=PIN_BLUE, active_high=False)
button = Button(PIN_BUTTON, pull_up=True)


# --- Logik ---
def set_next_state():
    """Wechselt zum nächsten Zustand und setzt die entsprechende LED-Farbe."""
    current_state = next(STATES)
    color = STATE_COLORS[current_state]
    
    print(f"Button gedrückt! Neuer Zustand: {current_state}")
    led.color = color
    
    # Spezielle Logik für den Fehlerzustand: Blinken
    if current_state == "ERROR":
        print("Fehlerzustand: LED blinkt.")
        led.blink(on_time=0.5, off_time=0.5, on_color=color, off_color=(0,0,0))
    else:
        # Sicherstellen, dass das Blinken bei anderen Zuständen aufhört.
        led.off()
        led.color = color


# --- Event-Handler ---
# Die Funktion 'set_next_state' wird aufgerufen, wenn der Button gedrückt wird.
button.when_pressed = set_next_state


# --- Hauptprogramm ---
print("Programm gestartet!")
print("Drücke den Button, um den Verbindungsstatus zu simulieren.")
print("Drücke Strg+C, um das Programm zu beenden.")

# Startzustand setzen
set_next_state()

# Das Programm anhalten und auf Events warten.
pause()
