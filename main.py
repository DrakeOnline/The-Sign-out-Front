# |========================================================|
# |    Title:      The Sign out Front                      |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Simulate advertisement efficiency       |
# |    Date:       April 25th, 2021                        |
# |========================================================|

from LinkedList import LinkedList
from os import system
import time
import datetime
import math


# |=========================TIME CONVERSIONS===============================|
# |  Sign cycle:                   20 s        ->  20,000 ms               |
# |  Student visibility time:      60 s        ->  60,000 ms               |
# |  Simulation period (1 week):   604,800 s   ->  604,800,000 ms          |
# |=========================AFTER COMPRESSION==============================|
# |  Sign cycle:                   20,000 ms       ->  2 ms                |
# |  Student visibility time:      60,000 ms       ->  6 ms                |
# |  Simulation period (1 week):   604,800,000 ms  ->  60,480 ms           |
# |==============================RESULTS===================================|
# |  Maximum simulation time: 60.48 seconds ~ 1 minute                     |
# |========================================================================|


# |=========================MAKE SIGNS===============================|
# Create circular list for signs
signs = LinkedList("Ad 1")

# Fill linkedlist with 20 ads
for x in range(2, 21):
    signs.append_right(f"Ad {x}")

# Make circular
signs.get_tail().next = signs.head


# |=========================SIGN TIMER===============================|
startTime = int(round(time.time() * 1000))
prevTime = 0
elapsedTime = 0
currentSign = signs.head

# Counts down a week's simulated time
while elapsedTime < 60480:
    # Millisecond timer
    now = int(round(time.time() * 1000))

    # How much time has passed
    elapsedTime = (now - startTime)

    # Check if 2 milliseconds has passed
    # To change sign every 2 milliseconds
    if elapsedTime % 2 == 0 and elapsedTime != prevTime:
        # If it had already run this cycle
        prevTime = elapsedTime
        system("cls")
        print("")
        print(f"{currentSign.value}")
        currentSign = currentSign.next
