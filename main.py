from utime import sleep
from display import Display
from pico_temperature import PicoTemperature
from scheduler import Scheduler
from clock import Clock
from christmas import Christmas
from apps import Apps, App
from pomodoro import Pomodoro
from temperature import Temperature
from time_set import TimeSet
from wifi import WLAN
from mqtt import MQTT
from configuration import Configuration
import machine
import uasyncio
import _thread
import neopixel

machine.freq(250_000_000)

APP_CLASSES = [
    Clock,
    Pomodoro,
    TimeSet
]

# Setup NeoPixel on GPIO 0 with 1 LED
np = neopixel.NeoPixel(machine.Pin(0), 1)

def wheel(pos):
    """Convert 0–255 to a rainbow color (R, G, B)."""
    if pos < 85:
        return (int(pos * 3), int(255 - pos * 3), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))

async def rainbow(delay=0.02):
    """Continuously cycle the NeoPixel through rainbow colors."""
    pos = 0
    while True:
        color = wheel(pos)
        np[0] = color
        np.write()
        pos = (pos + 1) % 256  # loop 0–255
        await uasyncio.sleep(delay)

print("-" * 10)
print("PICO CLOCK")
print("-" * 10)

print("Configuring...")
config = Configuration()

scheduler = Scheduler()
wlan = WLAN(scheduler)
mqtt = MQTT(scheduler)
display = Display(scheduler)
pico_temperature = PicoTemperature(scheduler, mqtt)
temperature = Temperature(mqtt)
apps = Apps(scheduler)

# register apps
for App in APP_CLASSES:
    apps.add(App(scheduler))


async def start():
    print("STARTING...")

    # start async scheduler
    scheduler.start()

    # create thread for UI updates.
    _thread.start_new_thread(display.enable_leds, ())

    # start apps
    await apps.start()
    # start neopixel rainbow colour change
    await rainbow()

uasyncio.run(start())
loop = uasyncio.get_event_loop()
loop.run_forever()
