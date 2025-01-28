stdin = open("input.txt", 'r')
N, Q = [int(x) for x in stdin.readline().split()]
closing_times = stdin.readline().split()
times_visit = stdin.readline().split()

able = True
for i in range(Q):
    S, V = [int(x) for x in stdin.readline().split()]
    