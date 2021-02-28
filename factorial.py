# This is factorial function.

import time
start = time.time()

result1 = 1
j = 1

while j <= 10000:
    result1 = result1 * j
    j = j + 1

print("The factorial of 100000 is: {}".format(result1))

end = time.time()
time_taken = end - start
print("Total time {} seconds".format(time_taken))
