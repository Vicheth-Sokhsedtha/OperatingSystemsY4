import threading
import time

BUFFER_SIZE = 100
buffer = []

# Semaphores
emptyPairs = threading.Semaphore(50)   # 50 particle pairs max
fullPairs = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer(pid):
    while True:
        # Produce two particles
        P1, P2 = f"P{pid}-1", f"P{pid}-2"

        emptyPairs.acquire()    # wait for 2 spaces (1 pair)
        mutex.acquire()

        buffer.append(P1)
        buffer.append(P2)
        print(f"Producer {pid} produced {P1}, {P2}")

        mutex.release()
        fullPairs.release(2)     # signal 1 pair (2 particles) available

        time.sleep(1)

def consumer():
    while True:
        fullPairs.acquire()     # wait until at least 1 pair exists
        mutex.acquire()

        P1 = buffer.pop(0)
        P2 = buffer.pop(0)
        print(f"Consumer packaged {P1}, {P2}")

        mutex.release()
        emptyPairs.release(2)    # free space for 1 pair (2 particles)

        time.sleep(2)

# Threads
for i in range(3):  # multiple producers
    threading.Thread(target=producer, args=(i,), daemon=True).start()

threading.Thread(target=consumer, daemon=True).start()

time.sleep(10)

