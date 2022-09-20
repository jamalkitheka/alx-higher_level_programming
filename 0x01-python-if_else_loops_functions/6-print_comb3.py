#!/usr/bin/python3
for t in range(10):
    for i in range(t + 1, 10):
         print("{}".format(str(t) + str(i)), end="")
         if int(str(t) + str(i)) < 89:
              print(", ", end="")
print("")
