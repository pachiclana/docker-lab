import time
import sys
import datetime

print(sys.version)

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S') + ('-%02d' % (now.microsecond / 10000)))

while True:
    print("Docker is working!")
    time.sleep(5)