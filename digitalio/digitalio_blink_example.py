# SPDX-FileCopyrightText: Tim Cocks 2020
#
# SPDX-License-Identifier: MIT

"""
`digitalio_blink_example`
====================================================

CircuitPython LED blink example.

* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""
import time
import board
from digitalio import DigitalInOut, Direction

# LED setup.
led = DigitalInOut(board.LED)
# For QT Py M0. QT Py M0 does not have a D13 LED, so you can connect an external LED instead.
# led = DigitalInOut(board.SCK)
led.direction = Direction.OUTPUT


while True:
    led.value = not led.value
    time.sleep(0.25)
