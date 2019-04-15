# coding: UTF-8
x = 3
ans = 0
itersLeft = x
while(itersLeft != 0):
  ans = ans + x
  itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))

x = int(input("Enter the number of prints: "))
for i in range(0, x):
  print(i)
  x = 5

x = int(input("Enter an integer:"))
ans = 0
while ans ** 2 < abs(x):
  ans += 1
if ans ** 2 != abs(x):
  print(x, "is not a perfect square")
else:
  if x < 0:
    ans = -ans
  print("Square root of " + str(x) + ' is ' + str(ans))