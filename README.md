# MicroPython Pico-Clock-Green

This is a fork built on excelletn work by the following.

Python port of the C code for the Waveshare [Pico-Clock-Green](https://www.waveshare.com/wiki/Pico-Clock-Green) product with support for MQTT (majority to be added) via the Pico W.

> The original Python code of this project written by Malcolm and contributors ([GitHub link](https://github.com/malcolmholmes/pico-clock-green-python)). This will be a maintained fork with lots of more features added.

## Development
I wanted the clock to be able to show messages instead of the temperature, to control a neopixel and to play a Christmas song.

This additional code is not as well written as it should be and I will try and add lines onto the end of config.json at a later date to control these features eg:
a) now many neopixels
b) a special user defined message

My code adds the ability to run a neopixel (this has been added to clock.py). This runs asyncronisly through the colours of the rainbow and does not affect the other functions. The data control pin fdr the neopixel / neopixel strip is connected to GPIO Pin 0 (Pin 1 of the PICO).

I have added additional code to clock.py to display a message instead of the temperature value on different occassions eg Christmas and Easter and St George's Day. In order to display lower case letters I have added these to the characters in display.py

I have connected a DFPlayer GPIO 1 (Pin 2) on the PICO

## Instructions (Windows)
a) Download the uf2 for your particular PICO.
b) Download the code from this repository
c) Extract this from the zip file to a folder
d) Run Thonny and use it to upload to the PICO attached to the PICO GREEN CLOCK






