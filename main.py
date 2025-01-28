def checkPalindrome(num: int):
    reversed = list(str(num))
    reversed.reverse()
    if str(num) == ''.join(reversed):
        return True
    else:
        return False

def optimalPlay(S: int):
    for i in range(S, 0, -1):
        if checkPalindrome(i):
            S -= i
            break
    return S

def runProgram(S):
    while S != 0:
        # Bessie turn
        S = optimalPlay(S)
        if S == 0:
            print('B')
            break
        # Elsie turn
        S = optimalPlay(S)
        if S == 0:
            print('E')
            break
stdin = open('input.txt', 'r')

T = int(stdin.readline())
for i in range(T):
    S = int(stdin.readline())
    runProgram(S)