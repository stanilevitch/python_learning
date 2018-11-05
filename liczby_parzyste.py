x = int(input("Podaj liczbę: "))
print(f"We will show the even numbers up to: {x} ")
y = 1
while y <= x:
    if y % 2 == 0:
        print(f"Liczba parzysta: {y}")
    y += 1
print("Gotowe - wypisałem wszystkie liczby parzyste")
