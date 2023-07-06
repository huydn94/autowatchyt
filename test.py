import threading
import time

def worker(thread_id):
    print(f"Thread {thread_id} started.")
    # Simulating some work
    time.sleep(10)
    print(f"Thread {thread_id} completed.")

# Create and start the threads
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()

print("All threads started.")

# Main program continues while threads are running

print("Main program completed. Exiting.")