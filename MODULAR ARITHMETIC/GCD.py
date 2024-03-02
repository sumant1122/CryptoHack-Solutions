def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

print(gcd(66528,52920))    
print(gcd(26513,32321)) 