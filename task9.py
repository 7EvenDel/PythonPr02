# 9 

a, b = 0, 1
n = 20
i = 1

while i <= n:
  print(f"{i}: {a}")
  a, b = b, a + b
  i += 1

i = 5
while i <= n:
  print(f"{i}: {a}")
  a, b = b, a + b
  i += 1



i = 0
while i <= 20:
  print(i)
  i += 2


i = -1
count = 0
while i >= -21:
  if count == 3:
    print(i)
    count = 0
  count += 1
  i -= 1
