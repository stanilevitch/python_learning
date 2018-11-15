number = 23
guess = int(input("Podaj liczbę całkowitą: "))

if guess == number:
    # Blok warunkowy zaczyna się w tym miejscu
    print("Gratulacje, zgadłeś tajemniczą liczbę!")
    print("Ale nie mamy nagrody :)")
    # Tu kończy się blok warunkowy
elif guess < number:
    # Drugi blok
    print("Liczba powinna być większa")
    # Koniec drugiego bloku ...
else:
    print("Liczba powinna być mniejsza")
    # ten blok zostanie wykonany tylko gdy guessed > number
print("KONIEC")
 # Ostatnia instrukcja (print) jest wykonywana zawsze - po zakończeniu instrukcji  warunkowej.