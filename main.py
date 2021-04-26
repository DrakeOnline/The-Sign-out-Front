# |========================================================|
# |    Title:       The Sign out Front                     |
# |    Author:      Drake G. Cummings                      |
# |    Purpose:     Simulate advertisement efficiency      |
# |    Date:        April 25th, 2021                       |
# |    Time Spent:  6 h(s), 24 m(s)                        |
# |========================================================|

from LinkedList import LinkedList
from Student import Student
from os import system
import time
import math


# |=========================TIME CONVERSIONS===============================|
# |  Sign cycle:                   20 s        ->  20,000 ms               |
# |  Student visibility time:      60 s        ->  60,000 ms               |
# |  Simulation period (1 week):   604,800 s   ->  604,800,000 ms          |
# |=========================AFTER COMPRESSION==============================|
# |  Sign cycle:                   20,000 ms       ->  20 ms               |
# |  Student visibility time:      60,000 ms       ->  60 ms               |
# |  First class (8 hours):        28,800,000 ms   ->  28,800 ms           |
# |  Classes after (24 hours):     86,400,000 ms   ->  86,400 ms           |
# |  Simulation period (1 week):   604,800,000 ms  ->  604,800 ms          |
# |==============================RESULTS===================================|
# |  Maximum simulation time: 604.8 seconds ~ 10 minutes                   |
# |========================================================================|

# Thoughts:
#   My instinct on approaching this project was similar to management games
# where you can fast-forward time and watch everything happen in a short and
# relative manner. So, although not efficiently using math, the use of time
# compression yields an accurate and fun result!
#   - Drake Cummings


# Conversions
signTime = 20
studentTime = 60

# |=========================MAKE SIGNS===============================|
# Create circular list for signs
signs = LinkedList("Ad 1")

# Fill linkedlist with 20 ads
for x in range(2, 21):
    signs.append_right(f"Ad {x}")

# Make circular
signs.get_tail().next = signs.head


# |=========================SIGN TIMER===============================|
Drake = Student()
startTime = int(round(time.time() * 1000))
prevTime = 0
elapsedTime = 0
currentSign = signs.head

# Notify user it's working
print("Running...")
# Counts down a week's simulated time
while elapsedTime < Drake.schedule[-1]:

    # Millisecond timer
    now = int(round(time.time() * 1000))
    # How much time has passed
    elapsedTime = (now - startTime)
    # Check if 2 milliseconds has passed
    # To change sign every 2 milliseconds
    if elapsedTime - prevTime > signTime:
        # If it had already run this cycle
        prevTime = elapsedTime
        currentSign = currentSign.next

    # Check the ad at the time the student shows up, and add it to
    #     the student's list of seen ads
    for classTime in Drake.schedule:
        # Check if time is between when student arrives, and student can't
        #    see the sign anymore
        if (elapsedTime - classTime >= 0
                and elapsedTime <= classTime + studentTime):
            # Don't add if already seen
            if currentSign.value not in Drake.adsSeen:
                Drake.adsSeen.append(currentSign.value)

# Calculate percentage of ads seen by student
print()
print(Drake.adsSeen)
print(f"{math.ceil((len(Drake.adsSeen)/20)*100)}% of signs were seen by the")
print("student on a four day schedule assuming they enter and leave")
print("the school once per day.")
