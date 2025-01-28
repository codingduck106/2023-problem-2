# N = number of cows
# M = number of minutes
# RRL = 1st cow passes right, second cow passes right, third cow passes left.
# 1 1 1 = 1st, 2nd, and 3rd cows have only a capacity of 1 in their bucket.

stdin = open('input.txt', 'r')
N, M = [int(x) for x in stdin.readline().split()]
PATTERN = list(stdin.readline().strip('\n'))
CAPACITY = [int(x) for x in stdin.readline().split()]

cows = CAPACITY.copy()

for i in range(M):
    for j in range(N):
        if PATTERN[j] == 'R':
            if j == N-1:
                cows[0] += 1
            else:
                cows[j+1] += 1
        elif PATTERN[j] == 'L':
            if j == 0:
                cows[-1] += 1
            else:
                cows[j-1] += 1
        cows[j] -= 1

for cowIndex in range(N):
    if cows[cowIndex] > CAPACITY[cowIndex]:
        cows[cowIndex] = CAPACITY[cowIndex]

print(sum(cows))