Q = [1,2,3,5,4]


moves = 0

Q = [P-1 for P in Q]

for i, P in enumerate(Q):
  if  P - i > 2:
    print("TOO CHAOTIC!")
  
  for j in range(max(P-1,0), i):
    if Q[j] > P:
      moves += 1 