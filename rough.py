import threading
import random

# Define a simple class
class Soldier:
    def __init__(self, soldierId, speed, position, status):
        self.soldierId = soldierId
        self.speed = speed
        self.position = position
        self.status = status


ctr = 0

# Function to create and initialize objects of MyClass
def create_objects():
    
    for i in range(10):
        my_object = Soldier(i, random.randint(0, 4), (random.randint(0,10), random.randint(0,10)), True)
        print(my_object.soldierId, my_object.speed, my_object.position, my_object.status)

# Create 10 threads to create objects concurrently
threads = []
for _ in range(10):
    thread = threading.Thread(target=create_objects)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished creating objects.")
