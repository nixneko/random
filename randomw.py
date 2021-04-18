import random, string, datetime
from datetime import datetime

input1 = str(input("word : "))
now = datetime.now
y = datetime.now().timestamp()

rangee = len(input1)
if input1 == input1:
    print("porcessing...")
    while(input1 == input1):
        now = datetime.now
        z = datetime.now().timestamp()
        x = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(rangee))
        if input1 == x:
            a = z - y
            end = datetime.utcfromtimestamp(a).strftime('%M:%S')
            print(f"Found : {x} \nTime  : {end}")
            break

        