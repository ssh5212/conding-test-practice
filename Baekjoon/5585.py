import sys

sys.stdin = open("5585_input.txt", "r")

# input
cost = int(input())

yen = 1000 - cost
count = 0

coins = [500, 100, 50, 10, 5, 1]

# process
for coin in coins:
    if (yen / coin) >= 1:
        count += yen // coin
        yen = yen % coin    

# output
print(count)

    