import time
from datetime import datetime

while True:
    now=datetime.now()
    print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}", end="\r")
    time.sleep(1)