import sys
import time

def typewriter(message, speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(speed)
        else:
            time.sleep(1)
            
    sys.stdout.write("\n")  # Ensure a newline at the end of the message
    sys.stdout.flush()