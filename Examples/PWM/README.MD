The analogue-to-digital converter in your Pico only works one way: it takes an analogue signal
and converts it to a digital signal the microcontroller can understand. If you want to go the
other way, and have your digital microcontroller create an analogue output, you’d normally need
a digital-to-analogue converter (DAC) – but there’s a way to ‘fake’ an analogue signal, using
something called pulse-width modulation or PWM.

A microcontroller’s digital output can only ever be on or off, 0 or 1. Turning a digital output on
and off is known as a pulse and by altering how quickly the pin turns on and off you can change,
or modulate, the width of these pulses – hence ‘pulse-width modulation’.

Every GPIO pin on your Pico is capable of pulse-width modulation, but the microcontroller’s
pulse-width modulation block is made up of eight slices, each with two outputs
