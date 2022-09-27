import sys
num = int(sys.argv[1])
sum = 0

for value in range(1, num + 1):
    sum = sum + value
    
print(sum)