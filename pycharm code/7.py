
#https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
def matching(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):  # N -M+1 eto gula window possible
        j = 0
        # For current index i, check
        # for pattern match */
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            print("Pattern found at Position ", i+1)
txt = input('Enter Text : ')
print('Text is : ',txt)
pat = input('Enter Pattern : ')
matching(pat, txt)


