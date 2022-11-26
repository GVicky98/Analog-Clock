#This program is to calculate the placements of numbers inside the clock
#This is found by locating the point on the circumference of a circle
"""The formula to calculate the poinr is (rcosx,rsinx),
where r and x are radius and angle with x-axis respectively"""

import math
r = 150
for i in range(0,360,30):
    print(r * (math.sin(math.radians(i))), r * (math.cos(math.radians(i))))