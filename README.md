# Multicoaster-Semaphore
5.8 The roller coaster problem This problem is from Andrews’s Concurrent Programming [1],
but he attributes it to J. S. Herman’s Master’s thesis. Suppose there are n passenger threads and a car thread. 
The passengers repeatedly wait to take rides in the car, which can hold C passengers, where C &lt; n. 
The car can go around the tracks only when it is full. Here are some additional details: 
• Passengers should invoke board and unboard. • The car should invoke load, run and unload. 
• Passengers cannot board until the car has invoked load • The car cannot depart until C passengers have boarded. 
• Passengers cannot unboard until the car has invoked unload. 
Puzzle: Write code for the passengers and car that enforces these constraints.

5.8.3 Multi-car Roller Coaster problem
This solution does not generalize to the case where there is more than one car.
In order to do that, we have to satisfy some additional constraints:
• Only one car can be boarding at a time.
• Multiple cars can be on the track concurrently.
• Since cars can’t pass each other, they have to unload in the same order
they boarded.
• All the threads from one carload must disembark before any of the threads
from subsequent carloads.
Puzzle: modify the previous solution to handle the additional constraints.
You can assume that there are m cars, and that each car has a local variable
named i that contains an identifier between 0 and m − 1.
