import shutil
import math
import time

width = shutil.get_terminal_size((80, 24)).columns
sentence = "+Java sucks major dick++++foreal m8+++++"

rad = 0
while True:
    delimiter = int((math.cos(math.radians(rad)) + 1) * ((width - len(sentence) -1) / 2))
    print((delimiter - 1) * ' ', sentence)
    if rad > 360:
        rad = 5
    else:
        rad += 5
    sentence = sentence[1:] + sentence[:1]
    time.sleep(0.02)
