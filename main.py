# |========================================================|
# |    Title:      The Sign out Front                      |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Simulate advertisement efficiency       |
# |    Date:       April 25th, 2021                        |
# |========================================================|

from LinkedList import LinkedList
from os import system
import time
import math


# Create circular list for signs
signs = LinkedList("Ad 1")

# Fill linkedlist with 20 ads
for x in range(2,21):
    signs.append_right(f"Ad {x}")

# Make circular
signs.get_tail().next = signs.head

# Change sign every 20 seconds
startTime = math.floor(time.time())
prevTime = 0
currentSign = signs.head

# Continuous timer
while True:
    # Rund time down
    now = math.floor(time.time())

    # How much time has passed
    elapsedTime = now - startTime

    # check if 2 seconds has passed
    if elapsedTime % 1 == 0 and elapsedTime != prevTime:
        # If it had already run this cycle
        prevTime = elapsedTime
        system("cls")
        print(f"{currentSign.value}")
        currentSign = currentSign.next

    # Try to limit cycle count
    time.sleep(0.01)
