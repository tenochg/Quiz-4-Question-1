count = 0 
l1 = []
while True:
  x = int(input('Enter a number: '))
  if x % 2 == 0:
    flag = x
    l1.append(flag)
    count = count + 1
  if count == 2:
    break

for i in l1:
  print(i,end=' ')