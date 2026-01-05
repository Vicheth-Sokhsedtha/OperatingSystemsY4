import threading

a = threading.Semaphore(1)
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def process1():
    a.acquire()
    print("H", end="")
    print("E", end="")
    b.release()

def process2():
    b.acquire()
    print("L", end="")
    c.release()

def process3():
    c.acquire()
    print("L", end="")
    print("O")

t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
