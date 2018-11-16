#2 Fibonacci sequence
FibSeq =[0,1] 
i = 0
while FibSeq[-1] < 4000000:
    i += 1
    FibSeq.append(FibSeq[i]+FibSeq[i-1])
    print FibSeq