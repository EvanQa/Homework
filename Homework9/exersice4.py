A = 10
B = 5
C = 7
D = 11
X = 3
Y = 8
Z = 2

#1
result_1 = ((A + B) * C) + (D * X) - (Y / Z)
print("(1):", result_1)
#2
A += ((B+D)*X)- C
print("(2):", A)
#3
result_3 = B == (A*2) + (C-3)
print("(3):",result_3)
#4
result_4 = C != (A * B + D)
print("(4):", result_4)
#5
D *= D + (7 - X - Z)
print("(5):", D)
#6
A %= Y + 1
print("(6):", A)
#7
B += 2*C + D - A
print("(7):", B)
#8
result_8 = (X + Y) * (A - C + D - B)
print("(8):",result_8)
#9
result_9 = (C * A - B * D) + (A * Z)
print("(9):", result_9)
#10
Y = A - B + X * (C < D) + Z * (not(D < A))
print("(10):", Y)
