import { version, Chip, Line } from 'node-libgpiod';

// --- Pin-Konfiguration (BCM-Nummerierung) ---
const LED_PIN = 17; // Rote LED
const BLINK_COUNT = 20; // Anzahl der Zustandswechsel (10-maliges Blinken)
const BLINK_INTERVAL = 500; // Intervall in Millisekunden

// --- Globale Referenzen, um Garbage Collection zu verhindern ---
// Die libgpiod-Objekte müssen im globalen Gültigkeitsbereich bleiben,
// solange sie verwendet werden, um zu verhindern, dass der Garbage Collector
// sie vorzeitig bereinigt.
const gpios = {
    chip: new Chip(0),
    line: null as Line | null,
};

function cleanup() {
    console.log("\nBeende und räume auf...");
    if (gpios.line) {
        gpios.line.setValue(0); // LED ausschalten (Annahme: Active High)
        gpios.line.release();
    }
    console.log("GPIOs freigegeben. Auf Wiedersehen!");
    process.exit(0);
}

try {
    console.log(`Verwende node-libgpiod Version: ${version}`);

    // LED-Leitung initialisieren
    gpios.line = new Line(gpios.chip, LED_PIN);
    gpios.line.requestOutputMode();

    console.log(`GPIO ${LED_PIN} ist bereit. Starte Blinken...`);

    let count = BLINK_COUNT;

    const blink = () => {
        if (count <= 0) {
            cleanup();
            return;
        }

        // Wert umschalten (0 oder 1)
        const value = count % 2;
        gpios.line?.setValue(value);
        console.log(`LED ${value === 1 ? 'AN' : 'AUS'}`);

        count--;
        setTimeout(blink, BLINK_INTERVAL);
    };

    // Blinken starten
    blink();

    // --- Aufräumen beim Beenden (Strg+C) ---
    process.on('SIGINT', cleanup);
    process.on('SIGTERM', cleanup);

} catch (error) {
    console.error("Ein Fehler ist aufgetreten:", error);
    process.exit(1);
}