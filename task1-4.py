# 1
a = 10
b = 5

# 2
# True
example1 = (a > 0) and (b > 0)
example2 = (a != b) and (a % 2 == 0)

# False
example3 = (a < 0) and (b > 10)
example4 = (a == b) and (a % 2 == 1)

# 3
# True
example5 = (a > 0) or (b > 0)
example6 = (a == b) or (a % 2 == 1)

# False
example7 = (a < 0) and (b < 0)
example8 = (a != b) and (a % 2 == 0)

# 4
c = "привіт"
d = "світ"

# True
example9 = (c[0] == d[0]) or (len(c) > len(d))
example10 = (c != d) and (c.upper() == d.upper())

# False
example11 = (c == d) and (len(c) == len(d))
example12 = (c[0] != d[0]) and (c.lower() == d.lower())