import sys
from datetime import datetime

if len(sys.argv) > 1:
    print("Hello", sys.argv[1])
else:
    print("Hello World")

# input("Podaj liczbę: ")

now = datetime.today().date()
print(now)

input("Podaj [q - aby zakończyć]")