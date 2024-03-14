import random
import time
num=random.random()
print(num)
while 1:
    num=round(random.uniform(100,120),2)
    time.sleep(0.4)
    print(num)
    