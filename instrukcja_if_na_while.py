number = 23
running = True
while running:
    guess = int(input('Podaj liczbę całkowitą: '))
    if guess == number:
        # Blok warunkowy zaczyna się w tym miejscu
        print('Gartulacje, zgadłeś liczbę.')
        print('(ale niestety nie ma żadnej nagrody!)')
        # Tu kończy się blok warunkowy. Konczy se także petla!
        running = False
    elif guess < number:
        # Drugi blok
        print('Nie, liczba powinna być większa')
        # Koniec drugiego bloku ...
    else:
        print('Nie, liczba powinna być mniejsza')
        # ten blok zostanie wykonany tylko gdy guessed > number
else:
    print('Koniec')
