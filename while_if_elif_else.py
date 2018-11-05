a = 10
while a > 0:
    print(a)
    if a > 5:
        print("if_" * 10)
    elif a % 2 != 0:
        print("elif_" * 10)
    else:
        print("else_" * 10)
    a -= 1
    print("else-1_" * 10)
print("KONIEC")
