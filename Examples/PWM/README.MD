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

![PWM Pins](https://github.com/RahulP5/RaspberryPico/blob/main/Documents/img/PWMpin.png)

## PWM CONFLICTS
You’ll know if you accidentally use the same PWM output twice, because every time you alter the PWM values on
one pin it will affect the conflicting pin as well. If that happens, take a look at the pinout diagram in above Figure
and your circuit and find a PWM output you haven’t used yet.

If that sounds confusing, don’t worry: all it means is that you need to make sure you keep
track of the PWM slices and outputs you’re using, making sure to only connect to pins with a
letter and number combination you haven’t already used. If you’re using PWM_A[0] on pin GP0
and PWM_B[0] on pin GP1, things will work fine, and will continue to work if you add PWM_A[1]
on pin GP2; if you try to use the PWM channel on pin GP0 and pin GP16, though, you’d run into
problems as they’re both connected to PWM_A[0].
