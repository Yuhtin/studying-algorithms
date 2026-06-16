import sys

count = 0
number = int(input())

while number > 0:
    value = number % 10
    number //= 10
    
    if value == 4 or value == 7:
        count += 1
        
isLucky = True
for i in list(str(count)):
    if i != "4" and i != "7":
        print("NO")
        sys.exit(0)
        
print("YES")