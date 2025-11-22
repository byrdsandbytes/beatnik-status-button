# Beatnik Status Button

A simple Raspberry Pi project to change the color of an RGB LED by pressing a button. This project is written in Python and uses the `gpiozero` library.

## Features

*   Press a button to set a random color on an RGB LED.
*   Uses a common-anode RGB LED.
*   Simple and clean code thanks to the `gpiozero` library.

## Hardware Requirements

*   Raspberry Pi (any model with GPIO pins)
*   A common-anode RGB LED
*   A push button
*   Resistors for the LED (e.g., 3 x 220Ω)
*   A breadboard and jumper wires

## Wiring

1.  Connect the common anode pin of the LED to a 3.3V pin on the Raspberry Pi.
2.  Connect the Red, Green, and Blue cathode pins of the LED to the following GPIO pins through a resistor for each:
    *   **Red**: GPIO 17
    *   **Green**: GPIO 27
    *   **Blue**: GPIO 22
3.  Connect one leg of the push button to GPIO 26.
4.  Connect the other leg of the push button to a Ground (GND) pin.

## Software Setup & Usage

1.  **Install `gpiozero`**:
    If `gpiozero` is not already installed on your Raspberry Pi OS, you can install it with `pip`:
    ```bash
    pip install gpiozero
    ```
    Or using `apt`:
    ```bash
    sudo apt update
    sudo apt install python3-gpiozero
    ```

2.  **Download the code**:
    Make sure you have the `main.py` file on your Raspberry Pi.

3.  **Run the script**:
    Execute the script from your terminal:
    ```bash
    python3 main.py
    ```

4.  **Usage**:
    *   The program will start, and the LED will be off.
    *   Press the button to change the LED to a new random color.
    *   Press `Ctrl+C` in the terminal to stop the program.
