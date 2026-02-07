import threading
import time

# ----- Shared Resources -----
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()   # mutex lock


account1 = Account("Account 1", 1000)
account2 = Account("Account 2", 1000)


# ----- Transfer Function (CAUSES DEADLOCK) -----
def transfer(from_acc, to_acc, amount):
    print(f"{threading.current_thread().name} locking {from_acc.name}...")
    from_acc.lock.acquire()
    print(f"{threading.current_thread().name} locked {from_acc.name}")

    time.sleep(1)   # wait so both threads lock opposite accounts

    print(f"{threading.current_thread().name} locking {to_acc.name}...")
    to_acc.lock.acquire()   # ← DEADLOCK HAPPENS HERE
    print(f"{threading.current_thread().name} locked {to_acc.name}")

    # Critical section (never reached in deadlock)
    from_acc.balance -= amount
    to_acc.balance += amount

    to_acc.lock.release()
    from_acc.lock.release()


# ----- Thread functions -----
def thread1():
    transfer(account1, account2, 100)

def thread2():
    transfer(account2, account1, 200)

# ----- Run Threads -----
t1 = threading.Thread(target=thread1, name="Thread-1")
t2 = threading.Thread(target=thread2, name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")