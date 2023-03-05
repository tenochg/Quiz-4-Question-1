
v2 = 3
while True:
  x = int(input('Enter a number: '))
  if x % 2 == 0 and v2 % 2 == 0:
    print(v2,x,end=' ')
    break
  v2 = x
