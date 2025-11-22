from gpiozero import RGBLED, Button
from signal import pause
import random

# --- Konfiguration der Pins (BCM Nummerierung) ---
# Make sure to install gpiozero first:
# sudo apt update
# sudo apt install python3-gpiozero
PIN_RED = 17
PIN_GREEN = 27
PIN_BLUE = 22
PIN_BUTTON = 26

# --- Initialisierung ---

# RGB-LED als Common-Anode-Typ initialisieren.
# active_high=False bedeutet, dass ein LOW-Signal (0) die LED einschaltet.
# gpiozero abstrahiert die (0,1)-Logik, wir können Farbwerte von 0 bis 1 setzen.
led = RGBLED(red=PIN_RED, green=PIN_GREEN, blue=PIN_BLUE, active_high=False)

# Button initialisieren.
# pull_up=True ist hier korrekt, da der Button gegen GND geschaltet ist.
# gpiozero kümmert sich intern um das Entprellen (Debouncing).
button = Button(PIN_BUTTON, pull_up=True)

# Zufällige Farbe generieren und setzen
def set_random_color():
    """Generiert eine zufällige Farbe und setzt sie auf der LED."""
    r = random.random() # Zufälliger Wert zwischen 0.0 und 1.0
    g = random.random()
    b = random.random()
    print(f"Neue Farbe: R={r:.2f}, G={g:.2f}, B={b:.2f}")
    led.color = (r, g, b)

# --- Event-Handler ---

# Die Funktion 'set_random_color' wird aufgerufen, wenn der Button gedrückt wird.
button.when_pressed = set_random_color

# --- Hauptprogramm ---

print("Programm gestartet! Drücke den Button, um die Farbe zu ändern.")
print("Drücke Strg+C, um das Programm zu beenden.")

# Startzustand: LED aus
led.off()

# Das Programm anhalten und auf Events warten.
# gpiozero gibt die Pins beim Beenden automatisch frei.
pause()