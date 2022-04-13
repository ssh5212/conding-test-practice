# N = '1234'

# for i in range(len(N)):
#     print(N[i]+N[0:i]+N[i+1:])


N = '1234'

for i in range(len(N)):
    for j in range(len(N)):
        N[i], N[j] = N[j], N[i]
        print(N)