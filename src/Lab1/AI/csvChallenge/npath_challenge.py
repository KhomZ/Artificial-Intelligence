# !/usr/bin/env python

import csv
import random
alpha = 'abcdefghijklmnopqrstuvwxyz'
e = range(0,99)
x = random.sample(alpha,14)
print(x)

# c = csv.writer(open("tst.csv", "wb"))
c = csv.writer(open("tst.csv", "w+"))
c.writerow([x])
# c.writerow(x)

# cr = csv.reader(open("tst.csv","rb"))
cr = csv.reader(open("tst.csv","r+"))

for row in cr:
        print(', ').join(row)

print("How many rows?")
l = input()

k = 1

while k < int(l):

        y = random.sample(e,14)
        c.writerow([y])

        # cr = csv.reader(open("tst.csv","rb"))
        cr = csv.reader(open("tst.csv","r+"))
        for row in cr:
                print(', ').join(row)

        k += 1

print('Done')