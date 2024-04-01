import time
import sys
from datetime import datetime

print(sys.version)

while True:
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  Docker is working!")
    time.sleep(5)