import { Gpio } from 'onoff';

// --- Konfiguration der Pins (BCM Nummerierung) ---
const PIN_RED = 17;
const PIN_GREEN = 27;
const PIN_BLUE = 22;
const PIN_BUTTON = 26;

// --- Initialisierung ---

// LEDs als Ausgang ('out')
// Wir setzen sie initial auf 1 (HIGH), damit sie AUS sind (wegen Common Anode)
const ledRed = new Gpio(PIN_RED, 'out');
const ledGreen = new Gpio(PIN_GREEN, 'out');
const ledBlue = new Gpio(PIN_BLUE, 'out');

// Button als Eingang ('in')
// 'falling' bedeutet: Wir horchen auf den Moment, wenn der Knopf gedrückt wird (Verbindung zu GND)
// debounceTimeout: Verhindert, dass ein Druck als 10x Drücken erkannt wird (Entprellen)
const button = new Gpio(PIN_BUTTON, 'in', 'falling', { debounceTimeout: 50 });

// Alle LEDs ausschalten (auf HIGH setzen)
function turnOffLeds() {
    ledRed.writeSync(1);
    ledGreen.writeSync(1);
    ledBlue.writeSync(1);
}

// Eine Farbe setzen (r, g, b sind entweder 0 für AN oder 1 für AUS)
function setColor(r: 0 | 1, g: 0 | 1, b: 0 | 1) {
    ledRed.writeSync(r);
    ledGreen.writeSync(g);
    ledBlue.writeSync(b);
}

// Zufällige Farbe generieren
function randomColor() {
    // Math.random() < 0.5 gibt true/false. 
    // Da wir "Active Low" haben: 
    // true -> 0 (AN)
    // false -> 1 (AUS)
    const r = Math.random() < 0.5 ? 0 : 1;
    const g = Math.random() < 0.5 ? 0 : 1;
    const b = Math.random() < 0.5 ? 0 : 1;

    console.log(`Neue Farbe (Active Low): R=${r}, G=${g}, B=${b}`);
    setColor(r, g, b);
}

console.log("Programm gestartet! Drücke den Button...");
turnOffLeds(); // Startzustand: Aus

// --- Event Listener ---

button.watch((err, value) => {
    if (err) {
        console.error('Es gab einen Fehler beim Button:', err);
        return;
    }

    // value ist 0, wenn der Button gedrückt ist (Verbindung zu GND)
    console.log('Button wurde gedrückt!');
    randomColor();
});

// --- Aufräumen beim Beenden (Strg+C) ---
process.on('SIGINT', () => {
    console.log('\nBeende Programm und gebe Pins frei...');
    ledRed.unexport();
    ledGreen.unexport();
    ledBlue.unexport();
    button.unexport();
    process.exit();
});