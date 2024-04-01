import time
import sys
import datetime 
now = datetime.datetime.now()

print(sys.version)
print(now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000)))

while True:
    print("Docker is working!")
    time.sleep(5)