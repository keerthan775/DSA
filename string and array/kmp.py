# Naive pattern searching algorithm 
import time
#txt = "THIS IS A TEST TEXT THIS IS A TEST TEXT THIS IS A TEST TEXT"
#pat = "TEST"
#txt =  "AABAACAADAABAABA"
#pat =  "AABA"
txt = 'bacbabababacaca'
pat = 'ababaca'
def naive(txt,pat):
    for i in range(len(txt)-len(pat)+1):
        count = 0
        for j in range(len(pat)):
            if txt[i+j] == pat[j]:
                count += 1
            else:
                break
        if count == len(pat):
            print("pattern found at index ",i)
    
# O((n-m+1)m)
start_time = time.time()
naive(txt,pat)
print("time taken",time.time()-start_time)
    

# kmp alogrithm

def kmp(txt,pat):
    txt_len = len(txt)
    pat_len = len(pat)
    lps = [0] * pat_len
    lps = compute_lps(pat,lps)
    i = 0
    j = 0
    while i < txt_len:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == pat_len:
            print("pattern found at index ",str(i-j))
            j = lps[j-1]
        elif i < txt_len and txt[i] != pat[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

def compute_lps(pat,lps):
    i = 1
    lps_count = 0
    #lps = [0] * len(pat) 

    while i < len(pat):
        if pat[i] == pat[lps_count]:
            lps_count += 1
            lps[i] = lps_count
            i += 1
        else:
            if lps_count == 0:
                i += 1
            else:
                lps_count = lps[lps_count-1]
    return  lps
start_time2 = time.time()
kmp(txt,pat)
print("time taken",time.time()-start_time2)



# if text and pattern is small size then use naive or else use kmp